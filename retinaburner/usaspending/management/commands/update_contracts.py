from retinaburner.usaspending.models import Contract
from retinaburner.usaspending.scripts.usaspending.contracts_loader import Loader
from django.core.management.base import BaseCommand
from django.core import management
from django.conf import settings
import os
import csv

class Command(BaseCommand):

    def handle(self, contracts_file, **options):
        print "Downloading links in delta_downloads.txt"
        management.call_command('download_files', settings.PROJECT_ROOT + '/retinaburner/usaspending/downloads/delta_downloads.txt')

        print "processing downloaded files into proper format"
        for fname in os.listdir(settings.CSV_PATH + 'datafeeds/'):
            if 'Delta' in fname:
                management.call_command('convert_usaspending_contracts')


        print"Processing transaction updates in database"
        print "Current number of rows in contract table: {0}".format(Contract.objects.all().count())

        for fname in os.listdir(settings.CSV_PATH + 'out/'):
            if 'contracts' in fname:
                print "processing file {0}".format(fname)
                reader = csv.reader(open(settings.CSV_PATH + 'out/' + fname))
                for line in reader:
                    update_row(line)

        print "New number of rows in contract table: {0}".format(Contract.objects.all().count())


    def update_row(line):

        #check status --> tells us if it's a delete or update
