from federal_spending.usaspending.models import Contract, Grant
from federal_spending.usaspending.scripts.usaspending.contracts_loader import Loader
from django.core.management.base import BaseCommand
from federal_spending.usaspending.management.commands.create_indexes import contracts_idx, grants_idx
from federal_spending.usaspending.scripts.usaspending.config import INDEX_COLS_BY_TABLE
from django.core import management
from django.db import connection
from django.conf import settings
import os
import csv
import time

class Command(BaseCommand):

    contracts_idx_drop = contracts_idx[:12]
    contracts_idx_add = contracts_idx[12:]
    grants_idx_drop = grants_idx[:5]
    grants_idx_add = grants_idx[5:]


    def handle(self, import_file='all_downloads.txt', update=False, **options):

        if update:
            warn_text = "This will delete USASpending tables and indexes for years {0}. Proceed? y\\n".format(settings.UPDATE_YEARS)
        else:
            warn_text = "This will delete all USASpending related tables, indexes, etc. Are you sure you want to proceed? y\\n "
        
        confirm = raw_input(warn_text)
        if confirm != 'y':
            return
        a="""
        print "deleting out files"
        OUTPATH = settings.CSV_PATH + 'out/'
        for f in os.listdir(OUTPATH):
            os.remove(OUTPATH + f)"""

        
        print "deleting old tables and indexes"
        cursor = connection.cursor()
        if update:
            sql = ""
            for fy in settings.UPDATE_YEARS:
                sql += "Drop table if exists usaspending_contract_{0} cascade; commit; Drop table if exists usaspending_grant_{1} cascade;commit;".format(fy, fy)

            #deleting overall indexes
            sql += ''.join(self.contracts_idx_drop)
            sql += ''.join(self.grants_idx_drop)

        else:
            sql = "Drop table if exists usaspending_contract cascade; commit; Drop table if exists usaspending_grant cascade; commit;"

        print sql
        cursor.execute(sql);

        print "Regenerating tables"
        management.call_command('syncdb')

        print "Creating partition tables"
        if update:
            for fy in settings.UPDATE_YEARS:
                management.call_command('create_partition', fiscal_year=fy, table='usaspending_contract')
                management.call_command('create_partition', fiscal_year=fy, table='usaspending_grant')
        else:
            management.call_command('create_partition', fiscal_year='all')

        a="""
        print "Downloading links in {0}".format(import_file) 
        management.call_command('download_files', settings.PROJECT_ROOT + '/usaspending/downloads/' + import_file)

        print "sleeping for a minute to allow files to close out"
        time.sleep(60)

        print "processing downloaded files into proper format"
        management.call_command('convert_usaspending_contracts', '--traceback')"""
        management.call_command('convert_usaspending_grants', '--traceback')

        print "Putting processed Contract CSVs in database"
        print settings.CSV_PATH + 'out/'
        for fname in os.listdir(settings.CSV_PATH + 'out/'):
            print fname
            if 'contracts' in fname:
                management.call_command('loadcontracts', settings.CSV_PATH + 'out/' + fname)

        print"Putting processed Grant CSVs in database"
        for fname in os.listdir(settings.CSV_PATH + 'out/'):
            print fname
            if 'grants' in fname:
                management.call_command('loadgrants', settings.CSV_PATH + 'out/' + fname)

        print "Creating partition indexes"
        management.call_command('create_indexes')

