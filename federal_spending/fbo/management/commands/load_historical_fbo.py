from django.core.management.base import CommandError, BaseCommand
from federal_spending.fbo.models import Notice
from django.conf import settings
import os 
from zipfile import ZipFile

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # unzip bulk csv
        # read/process each record
        # save to database/postgres copy command?

        ZIP_PATH = settings.PROJECT_ROOT + '/fbo/bulk_csvs/'

        for fi in os.listdir(ZIP_PATH):
            if fi[-3:] == "zip":
                z = ZipFile(ZIP_PATH + fi, 'r')
                z.extractall(ZIP_PATH)

        #for csvfile in os.listdir(ZIP_PATH):
         #   if csvfile[-3] == "csv":
                #process csv