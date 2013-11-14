from retinaburner.usaspending.models import Contract
from retinaburner.usaspending.scripts.usaspending.contracts_loader import Loader
from retinaburner.usaspending.scripts.fpds import FIELDS, CALCULATED_FIELDS
from django.core.management.base import BaseCommand
from django.core import management
from django.conf import settings
from itertools import izip
import os
import csv

class Command(BaseCommand):
    
    ALL_FIELDS = [ x[0] for x in FIELDS ] + [ x[0] for x in CALCULATED_FIELDS ]

    def handle(self, contracts_file='delta_downloads.txt', **options):

        OUTPATH = settings.CSV_PATH + 'out/'

        confirm = raw_input("Clearing out the csvs in the out folder, continue? y/n")
        if confirm != 'y': 
            return

        #remove any csvs so we don't reprocess everything
        for f in os.listdir(OUTPATH):
            os.remove(f)

        print "Downloading links in {0}".format(contracts_file)
        management.call_command('download_files', settings.PROJECT_ROOT + '/retinaburner/usaspending/downloads/' + contracts_file)

        print "processing downloaded files into proper format"
        for fname in os.listdir(settings.CSV_PATH + 'datafeeds/'):
            if 'Delta' in fname:
                management.call_command('convert_usaspending_contracts')


        print"Processing transaction updates in database"
        print "Current number of rows in contract table: {0}".format(Contract.objects.all().count())

        for fname in os.listdir(OUTPATH):
            if 'contracts' in fname:
                print "processing file {0}".format(fname)
                reader = csv.reader(open(OUTPATH + fname))
                for line in reader:
                    update_row(line)

        print "New number of rows in contract table: {0}".format(Contract.objects.all().count())


    def update_row(line):

        status = line[1]
        if status.strip().lower() == 'inactive':
            c = Contract.objects.get(unique_transaction_id=line[0])
            c.delete()
        else:
            c = Contract.objects.get_or_create(unique_transaction_id=line[0])

            for (column_name, value) in izip(ALL_FIELDS, line):
                setattr(c, column_name, value)
            c.save()
