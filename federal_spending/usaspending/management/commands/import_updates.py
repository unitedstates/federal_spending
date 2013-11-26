from federal_spending.usaspending.models import Contract, Grant
from federal_spending.usaspending.scripts.usaspending.contracts_loader import Loader
from federal_spending.usaspending.scripts.usaspending.fpds import FIELDS as CONTRACT_FIELDS, CALCULATED_FIELDS as CONTRACT_CALCULATED_FIELDS
from federal_spending.usaspending.scripts.usaspending.faads import FIELDS as GRANT_FIELDS, CALCULATED_FIELDS as GRANT_CALCULATED_FIELDS
from django.core.management.base import BaseCommand
from django.core import management
from django.conf import settings
from django.db import connections, connection, transaction
from django.db.models import sql
from itertools import izip
from dateutil.parser import parse
import os
import csv
import datetime
import time
from federal_spending.usaspending.management.commands.create_indexes import contracts_idx, grants_idx
from federal_spending.usaspending.scripts.usaspending.config import INDEX_COLS_BY_TABLE

def notnull(val):
    if val and val != '' and 'null' not in val.strip().lower():
        return True
    return False

class Command(BaseCommand):
    
    ALL_CONTRACT_FIELDS = [ x[0] for x in CONTRACT_FIELDS ] + [ x[0] for x in CONTRACT_CALCULATED_FIELDS ]
    ALL_GRANT_FIELDS = [ x[0] for x in GRANT_FIELDS ] + [ x[0] for x in GRANT_CALCULATED_FIELDS ]

    contracts_failed = []
    grants_failed = []

    contracts_idx_drop = contracts_idx[:10]
    contracts_idx_add = contracts_idx[12:22]
    grants_idx_drop = grants_idx[:3]
    grants_idx_add = grants_idx[5:8]

    @transaction.commit_manually
    def handle(self, download_file='delta_downloads.txt', **options):

        OUTPATH = settings.CSV_PATH + 'out/'

        a="""confirm = raw_input("Clearing out the csvs in the out folder, continue? y/n")
        if confirm != 'y': 
            return

        #remove any csvs so we don't reprocess everything
        for f in os.listdir(OUTPATH):
            os.remove(OUTPATH + f)

        print "Downloading links in {0}".format(download_file)
        management.call_command('download_files', settings.PROJECT_ROOT + '/usaspending/downloads/' + download_file)

        print "sleeping for a minute"
        time.sleep(60)

        print "processing downloaded files into proper format"
        for fname in os.listdir(settings.CSV_PATH + 'datafeeds/'):
            if 'Delta' in fname and 'Contracts' in fname:
                management.call_command('convert_usaspending_contracts')

            elif 'Delta' in fname and ('Grants' in fname or 'Loans' in fname or 'Insurance' in fname or 'Direct_Payments' in fname):
                management.call_command('convert_usaspending_grants')


        print "Processing transaction updates in database"
        #print "Current number of rows in contract table: {0}".format(Contract.objects.all().count())
        #print "Current number of rows in grant table: {0}".format(Grant.objects.all().count())
"""
        c = connections['default'].cursor()

        print 'deleting unecessary indexes'
        for x in self.contracts_idx_drop:
            print x
            c.execute(x)

        for x in self.grants_idx_drop:
            print x
            c.execute(x)

        for tab in ['usaspending_grant', 'usaspending_contract']:
            for fy in settings.FISCAL_YEARS:
                for i, colname in enumerate(INDEX_COLS_BY_TABLE[tab]):
                    if 'fiscal_year' not in colname and 'unique_transaction_id' not in colname:
                        del_stmt = 'drop index if exists {0}_{1}_{2}; commit;'.format(tab, fy, i)
                        print del_stmt
                        c.execute(del_stmt)

        for sname in os.listdir(OUTPATH):
            line_total = 0
            if 'contracts' in sname:
                print "processing file {0}".format(sname)
                reader = csv.reader(open(OUTPATH + sname), delimiter='|')
                for line in reader:
                    self.update_contract_row(line)
                    if line_total % 1000 == 0: print "... on line {0}".format(line_total)
                    line_total += 1

            line_total = 0
            if 'grants' in sname:   
                print "processing file {0}".format(sname)
                reader = csv.reader(open(OUTPATH + sname), delimiter='|')
                for line in reader:
                    self.update_grant_row(line)
                    if line_total % 1000 == 0: 
                        print "... on line {0}".format(line_total)
                        transaction.commit()
                    line_total += 1

        print 'recreating unecessary indexes'
        for x in self.contracts_idx_add:
            print x
            c.execute(x)

        for x in self.grants_idx_add:
            print x
            c.execute(x)

        #print "New number of rows in contract table: {0}".format(Contract.objects.all().count())
        #print "New number of rows in grant table: {0}".format(Grant.objects.all().count())
        
        self.write_log()


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
                    if notnull(value): 
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
            #print connection.queries[-1]

            for (i, (column_name, value)) in enumerate(izip(self.ALL_GRANT_FIELDS, line)):
                if i in [21, 22, 23, 55]:
                    if notnull(value): 
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
            #print connection.queries[-1]

    def write_log(self):
        today = datetime.datetime.now()
        print "Writing Log"
        writer = csv.writer(open(settings.LOGGING_DIRECTORY + '/failed_contracts_{0}.csv'.format(today.strftime('%Y%m%d')), 'w+'))
        for line in self.contracts_failed:
            writer.writerow(line)

        gwriter = csv.writer(open(settings.LOGGING_DIRECTORY + '/failed_grants_{0}.csv'.format(today.strftime('%Y%m%d')), 'w+'))
        for line in self.grants_failed:
            gwriter.writerow(line)

