from retinaburner.usaspending.models import Contract
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

def notnull(val):
    if val and val != '' and 'null' not in val.strip().lower():
        return True
    return False

class Command(BaseCommand):
    
    ALL_CONTRACT_FIELDS = [ x[0] for x in CONTRACT_FIELDS ] + [ x[0] for x in CONTRACT_CALCULATED_FIELDS ]
    ALL_GRANT_FIELDS = [ x[0] for x in GRANT_FIELDS ] + [ x[0] for x in GRANT_CALCULATED_FIELDS ]

    def handle(self, contracts_file='delta_downloads.txt', **options):

        OUTPATH = settings.CSV_PATH + 'out/'

        a="""confirm = raw_input("Clearing out the csvs in the out folder, continue? y/n")
        if confirm != 'y': 
            return

        #remove any csvs so we don't reprocess everything
        for f in os.listdir(OUTPATH):
            os.remove(OUTPATH + f)

        print "Downloading links in {0}".format(contracts_file)
        management.call_command('download_files', settings.PROJECT_ROOT + '/usaspending/downloads/' + contracts_file)

        print "processing downloaded files into proper format"
        for fname in os.listdir(settings.CSV_PATH + 'datafeeds/'):
            if 'Delta' in fname:
                management.call_command('convert_usaspending_contracts')


        print"Processing transaction updates in database"
        print "Current number of rows in contract table: {0}".format(Contract.objects.all().count())
        print "Current number of rows in grant table: {0}".format(Grant.objects.all().count())

"""
        for sname in os.listdir(OUTPATH):
            if 'contracts' in sname:
                print "processing file {0}".format(sname)
                reader = csv.reader(open(OUTPATH + sname))
                for line in reader:
                    self.update_contract_row(line[0].split('|'))

            if 'grants' in sname:
                print "processing file {0}".format(sname)
                reader = csv.reader(open(OUTPATH + sname))
                for line in reader:
                    self.update_grant_row(line[0].split('|'))

        print "New number of rows in contract table: {0}".format(Contract.objects.all().count())
        print "New number of rows in grant table: {0}".format(Grant.objects.all().count())

    def update_contract_row(self, line):

        status = line[1]
        if status.strip().lower() == 'inactive':
            #means that this update deletes a record
            c = Contract.objects.get(unique_transaction_id=line[0])
            print "deleting {0}".format(c.unique_transaction_id)
            c.delete()
        else:
            c, created = Contract.objects.get_or_create(unique_transaction_id=line[0])
            print "adding {0}".format(line[0])
            for (i, (column_name, value)) in enumerate(izip(self.ALL_CONTRACT_FIELDS, line)):
                print i
                print value

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

                print "{0} - {1}".format(column_name, value)

                setattr(c, column_name, value)
            c.save()

    def update_grant_row(self, line):

        status = line[1]
        if status.strip().lower() == 'inactive':
            #means that this update deletes a record
            c = Grant.objects.get(unique_transaction_id=line[0])
            print "deleting {0}".format(c.unique_transaction_id)
            c.delete()
        else:
            c, created = Grant.objects.get_or_create(unique_transaction_id=line[0])
            print "adding {0}".format(line[0])
            for (i, (column_name, value)) in enumerate(izip(self.ALL_GRANT_FIELDS, line)):
                print i
                print value

                if i in [0, 23, 50, 53]:
                    if notnull(value): 
                        #parse date fields into python date objects
                        value = parse(value)
                    else:
                        value = None
                if value == 'NULL': #convert CSV/Postgresql null values to python null
                    value = None

                print "{0} - {1}".format(column_name, value)

                setattr(c, column_name, value)
            c.save()
