from django.core.management.base import BaseCommand
import subprocess
from django.conf import settings


class Command(BaseCommand):

    def handle(self, download_file, **options):
    	#walk through download file and store everything in CSVs folder.
    	root_path = settings.PROJECT_ROOT
    	print root_path
    	for line in open(download_file).xreadlines():
	    	outfile_name = root_path + '/usaspending/downloads/csvs/' + line.split('/')[-1]
	    	subprocess.Popen(["wget", line, "-O", outfile_name ])