from django.core.management.base import BaseCommand
from django.conf import settings
import os
import urllib
import zipfile

class Command(BaseCommand):

    def handle(self, download_file, **options):
        #walk through download file and store everything in CSVs folder.
        csv_path = settings.CSV_PATH
        for line in open(download_file).xreadlines():
            line = line.strip()
            print "Reading file " + line
            outfile_name = csv_path + line.split('/')[-1]
            print "saving to " + outfile_name
            urllib.urlretrieve(line, outfile_name)

        for f in os.listdir(csv_path):
            if f[-3:] == 'zip':
                print "unzipping " + f
                zf = zipfile.ZipFile(csv_path + f)
                zf.extractall(csv_path)
