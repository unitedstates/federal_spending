from django.core.management.base import CommandError, BaseCommand
from federal_spending.usaspending.scripts.usaspending.fpds import FIELDS as CONTRACT_FIELDS, CALCULATED_FIELDS as CONTRACT_CALCULATED_FIELDS
from federal_spending.usaspending.scripts.usaspending.faads import FIELDS as GRANT_FIELDS, CALCULATED_FIELDS as GRANT_CALCULATED_FIELDS
from django.db import connections, transaction
from federal_spending.usaspending.models import Contract, Grant
from django.core import management
from django.conf import settings
import datetime
import requests
import cStringIO
import csv
import os
import sys
import time
from itertools import izip
from dateutil.parser import parse
import logging

logging.basicConfig(filename=settings.LOGGING_DIRECTORY + "/daily_update.log", level=logging.DEBUG)

class Command(BaseCommand):
    
    ALL_CONTRACT_FIELDS = [ x[0] for x in CONTRACT_FIELDS ] + [ x[0] for x in CONTRACT_CALCULATED_FIELDS ]
    ALL_GRANT_FIELDS = [ x[0] for x in GRANT_FIELDS ] + [ x[0] for x in GRANT_CALCULATED_FIELDS ]
 
    def notnull(self, val):
        if val and val != '' and 'null' not in val.strip().lower():
            return True
        return False
   
    def handle(self, day=None, type='all', *args, **kwargs):

        try:
            print "deleting files in /datafeeds and /out"
            
            OUTPATH = settings.CSV_PATH + 'out/'
            
            for f in os.listdir(OUTPATH):
                os.remove(OUTPATH + f)
            
            INPATH = settings.CSV_PATH + 'datafeeds/'
            for f in os.listdir(INPATH):
                os.remove(INPATH + f)

            base_url = 'http://www.usaspending.gov/customcode/build_feed.php?data_source=PrimeAward&detail_level=Complete&ou_code=All&is_dept=false&recipient_state=All&pop_state=All&format=CSV&recovery_only=&record_count=10000000000'

            if not day:
                day = datetime.datetime.now() - datetime.timedelta(days=1)
                day = day.strftime("%Y-%m-%d")

            print "Downloading new files"

            for fy in settings.FISCAL_YEARS:
                url = base_url + '&fiscal_year=' + str(fy) + '&since=' + day
                #grant files
                c = requests.get(url + '&spending_category=Grants')
                outf = open(INPATH + str(fy) + '_All_Grants_Delta_' + day + '.csv', 'w')
                outf.write(c.content)

                c = requests.get(url + '&spending_category=DirectPayments')
                if c.content:
                    outf.write(c.content[c.content.index('\n')+1:])

                c = requests.get(url + '&spending_category=Insurance')
                if c.content:
                    outf.write(c.content[c.content.index('\n')+1:])

                c = requests.get(url + '&spending_category=Loans')
                if c.content:
                    outf.write(c.content[c.content.index('\n')+1:])

                c = requests.get(url + '&spending_category=Contracts')
                outf = open(INPATH + str(fy) + '_All_Contracts_Delta_' + day + '.csv', 'w')
                outf.write(c.content)


            print "sleeping for a minute"
            time.sleep(60)

            print "processing downloaded files into proper format"
            management.call_command('convert_usaspending_contracts')
            management.call_command('convert_usaspending_grants')

            print "looping through files"
            for sname in os.listdir(OUTPATH):
                if 'contracts' in sname:
                    self.process_contract_file(sname, OUTPATH)

                if 'grants' in sname:   
                    self.process_grant_file(sname, OUTPATH)
        except Exception as e:
            logging.debug("An exception was thrown: %s" % e)

    @transaction.commit_on_success
    def process_contract_file(self, sname, OUTPATH):
        print "processing file {0}".format(sname)
        line_total = 0
        with open(OUTPATH + sname) as f:
            reader = csv.reader(f, delimiter='|')
            for line in reader:
                self.update_contract_row(line)
                if line_total % 1000 == 0: print "... on line {0}".format(line_total)
                line_total += 1

            line = None

    @transaction.commit_on_success
    def process_grant_file(self, sname, OUTPATH):
        print "processing file {0}".format(sname)
        line_total = 0
        with open(OUTPATH + sname) as f:
            reader = csv.reader(f, delimiter='|')
            for line in reader:
                self.update_grant_row(line)
                if line_total % 1000 == 0: print "... on line {0}".format(line_total)
                line_total += 1

    def check_fiscal_year(self, line, num):
        if len(line) >= (num):
            fy = line[num]
            if fy and fy != '' and len(fy) == 4:
                return True
            else: 
                print "it failed! {0}".format(line[0])
            return False
        else: 
            print "length failed {0} it's only {1}".format(line[0], len(line))
        return False

    def update_contract_row(self, line):
        c = None
        status = line[1]
        if status.strip().lower() == 'inactive':
            #means that this update deletes a record
            try:
                c = Contract.objects.get(unique_transaction_id=line[0], fiscal_year=line[97])
                print "Deleting {0}".format(line[0])
                c.delete()
            except Contract.DoesNotExist as e:
                pass
            except Contract.MultipleObjectsReturned as e:
                for con in Contract.objects.filter(unique_transaction_id=line[0], fiscal_year=line[97]):
                    con.delete()
            return
        else:
            if not self.check_fiscal_year(line, 97):
                self.contracts_failed.append(line)
                return
            try:
                c = Contract.objects.get(unique_transaction_id=line[0], fiscal_year=line[97])
            except Contract.DoesNotExist as e:
                c = Contract(unique_transaction_id=line[0], fiscal_year=line[97])
            except Contract.MultipleObjectsReturned as e:
                # delete extra objects
                cset = Contract.objects.filter(unique_transaction_id=line[0], fiscal_year=line[97]).order_by('-id')
                for i, obj in enumerate(cset):
                    if i == 0:
                        c = obj
                    else:
                        obj.delete()

            for (i, (column_name, value)) in enumerate(izip(self.ALL_CONTRACT_FIELDS, line)):
                if i in [13,14,15,16, 68, 69, 158]:
                    if self.notnull(value): 
                        #parse date fields into python date objects
                        try:
                            value = parse(value)
                        except OverflowError as e:
                            value = None
                    else:
                        value = None
                if value == 'NULL': #convert CSV/Postgresql null values to python null
                    value = None

                setattr(c, column_name, value)
            c.save()


    def update_grant_row(self, line):

        #To Do: add logging for transactions that fail
        c = None

        status = line[1]
        #print "processing {0}".format(line[0])

        if status.strip().lower() == 'inactive':
            #means that this update deletes a record
            try:
                c = Grant.objects.get(unique_transaction_id=line[0], fiscal_year=line[46])
                print "Deleting {0}".format(line[0])
                c.delete()
            except Grant.DoesNotExist as e:
                pass
            except Grant.MultipleObjectsReturned as e:
                for c in Grant.objects.filter(unique_transaction_id=line[0], fiscal_year=line[46]):
                    c.delete()
            return
        else:
            if not self.check_fiscal_year(line, 46):
                self.contracts_failed.append(line)
                return

            try:
                c = Grant.objects.get(unique_transaction_id=line[0], fiscal_year=line[46])

            except Grant.DoesNotExist as e:
                c = Grant(unique_transaction_id=line[0], fiscal_year=line[46])

            except Grant.MultipleObjectsReturned as f:
                print f
                cset = Grant.objects.filter(unique_transaction_id=line[0], fiscal_year=line[46]).order_by('-id')
                # delete extra objects
                for i, obj in enumerate(cset):
                    print obj
                    if i == 0:
                        c = obj
                    else:
                        obj.delete()

            for (i, (column_name, value)) in enumerate(izip(self.ALL_GRANT_FIELDS, line)):
                if i in [21, 22, 23, 55]:
                    if self.notnull(value): 
                        #parse date fields into python date objects
                        try:
                            value = parse(value).date()
                        except OverflowError as e:
                            value = None
                    else:
                        value = None
                if value == 'NULL': #convert CSV/Postgresql null values to python null
                    value = None

                setattr(c, column_name, value)
            c.save()

        # clear out dailies dir
        # for each FY, download the csv
        # convert each csv to normal format
        # open converted csvs and import each row
    
