from retinaburner.usaspending.models import Contract, Grant
from retinaburner.usaspending.scripts.usaspending.contracts_loader import Loader
from retinaburner.usaspending.scripts.usaspending.fpds import FIELDS as CONTRACT_FIELDS, CALCULATED_FIELDS as CONTRACT_CALCULATED_FIELDS
from retinaburner.usaspending.scripts.usaspending.faads import FIELDS as GRANT_FIELDS, CALCULATED_FIELDS as GRANT_CALCULATED_FIELDS
from django.core.management.base import BaseCommand
from django.core import management
from django.conf import settings
from itertools import izip
from dateutil.parser import parse
import os
import csv
import datetime
import time

def notnull(val):
    if val and val != '' and 'null' not in val.strip().lower():
        return True
    return False

class Command(BaseCommand):
    
    ALL_CONTRACT_FIELDS = [ x[0] for x in CONTRACT_FIELDS ] + [ x[0] for x in CONTRACT_CALCULATED_FIELDS ]
    ALL_GRANT_FIELDS = [ x[0] for x in GRANT_FIELDS ] + [ x[0] for x in GRANT_CALCULATED_FIELDS ]

    contracts_failed = []
    grants_failed = []

    def handle(self, contracts_file='delta_downloads.txt', **options):

        OUTPATH = settings.CSV_PATH + 'out/'

        #confirm = raw_input("Clearing out the csvs in the out folder, continue? y/n")
        #if confirm != 'y': 
        #    return

        #remove any csvs so we don't reprocess everything
        for f in os.listdir(OUTPATH):
            os.remove(OUTPATH + f)

        print "Downloading links in {0}".format(contracts_file)
        management.call_command('download_files', settings.PROJECT_ROOT + '/usaspending/downloads/' + contracts_file)

        print "sleeping for a minute"
        time.sleep(60)

        print "processing downloaded files into proper format"
        for fname in os.listdir(settings.CSV_PATH + 'datafeeds/'):
            if 'Delta' in fname:
                management.call_command('convert_usaspending_contracts')


        print"Processing transaction updates in database"
        print "Current number of rows in contract table: {0}".format(Contract.objects.all().count())
        print "Current number of rows in grant table: {0}".format(Grant.objects.all().count())


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
                    if line_total % 1000 == 0: print "... on line {0}".format(line_total)
                    line_total += 1


        print "New number of rows in contract table: {0}".format(Contract.objects.all().count())
        print "New number of rows in grant table: {0}".format(Grant.objects.all().count())
        
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

        status = line[1]
        if status.strip().lower() == 'inactive':
            #means that this update deletes a record
            print "inactive"
            c = Contract.objects.get(unique_transaction_id=line[0], fiscal_year=line[97])
            print "Deleting {0}".format(line[0])
            c.delete()
        else:
            if not self.check_fiscal_year(line, 97):
                self.contracts_failed.append(line)
                return
            try:
                c = Contract.objects.get(unique_transaction_id=line[0], fiscal_year=line[97])
            except Contract.ObjectDoesNotExist as e:
                c = Contract(unique_transaction_id=line[0], fiscal_year=line[97])
            except Contract.MultipleObjectsReturned as e:
                # delete extra objects
                cset = Contract.objects.filter(unique_transaction_id=line[0], fiscal_year=line[97])
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

        status = line[54]
        if status.strip().lower() == 'inactive':
            #means that this update deletes a record
            c = Grant.objects.get(unique_transaction_id=line[55], fiscal_year=line[1])
            if not self.check_fiscal_year(line):
                self.grants_failed.append(line)
                return
            c.delete()
        else:
            if not self.check_fiscal_year(line, 1):
                self.contracts_failed.append(line)
                return
            c, created = Grant.objects.get_or_create(unique_transaction_id=line[55], fiscal_year=line[1])
            for (i, (column_name, value)) in enumerate(izip(self.ALL_GRANT_FIELDS, line)):
                if i in [0, 23, 50, 53]:
                    if notnull(value): 
                        #parse date fields into python date objects
                        value = parse(value)
                    else:
                        value = None
                if value == 'NULL': #convert CSV/Postgresql null values to python null
                    value = None
                setattr(c, column_name, value)
            c.save()

    def write_log(self):
        today = datetime.datetime.now()
        print "Writing Log"
        writer = csv.writer(open(settings.LOGGING_DIRECTORY + '/failed_contracts_{0}.csv'.format(today.strftime('%Y%m%d')), 'w+'))
        for line in self.contracts_failed:
            writer.writerow(line)

        gwriter = csv.writer(open(settings.LOGGING_DIRECTORY + '/failed_grants_{0}.csv'.format(today.strftime('%Y%m%d')), 'w+'))
        for line in self.grants_failed:
            gwriter.writerow(line)

