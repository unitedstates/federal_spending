from retinaburner.usaspending.models import Contract, Grant
from retinaburner.usaspending.scripts.usaspending.contracts_loader import Loader
from django.core.management.base import BaseCommand
from django.core import management
from django.db import connection
from django.conf import settings
import os
import csv
import time

class Command(BaseCommand):

    def handle(self, **options):

        #put a check in here -- are you sure?
        confirm = raw_input("This will delete all USASpending related tables, indexes, etc. Are you sure you want to proceed? y\\n ")
        if confirm != 'y':
            return

        print "deleting old tables and indexes"
        cursor = connection.cursor()
        sql = "Drop table if exists usaspending_contract cascade; commit; Drop table if exists usaspending_grant cascade; commit;"
        cursor.execute(sql);

        print "Regenerating tables"
        management.call_command('syncdb')

        print "Creating partition tables"
        management.call_command('create_partition', fiscal_year='all')

        b = """  print "Downloading links in all_downloads.txt"
        management.call_command('download_files', settings.PROJECT_ROOT + '/usaspending/downloads/all_downloads.txt')"""

        print "sleeping for a minute to allow files to close out"
        time.sleep(60)

        print "processing downloaded files into proper format"
        management.call_command('convert_usaspending_contracts', '--traceback')
        management.call_command('convert_usaspending_grants', '--traceback')

        print "Putting processed Contract CSVs in database"
        print "Current number of rows in contract table: {0}".format(Contract.objects.all().count())

        print settings.CSV_PATH + 'out/'
        for fname in os.listdir(settings.CSV_PATH + 'out/'):
            print fname
            if 'contracts' in fname:
                management.call_command('loadcontracts', settings.CSV_PATH + 'out/' + fname)

        print "New number of rows in contract table: {0}".format(Contract.objects.all().count())

        print"Putting processed Grant CSVs in database"
        print "Current number of rows in grant table: {0}".format(Grant.objects.all().count())

        for fname in os.listdir(settings.CSV_PATH + 'out/'):
            print fname
            if 'grants' in fname:
                management.call_command('loadgrants', settings.CSV_PATH + 'out/' + fname)
                
        print "New number of rows in grant table: {0}".format(Grant.objects.all().count())

    