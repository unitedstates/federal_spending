from django.core.management.base import CommandError, BaseCommand
from django.db import connections, transaction
from optparse import make_option
from django.conf import settings
import requests
from xml.etree import ElementTree as et

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-t', '--test',
            action='store',
            dest='test',
            help='Test to run on data'
        ),
    )

    def handle(self, *args, **kwargs):
        if kwargs.has_key('test'):
            test = kwargs['test']
        else:
            test = 'all'

        self.transaction_number()


    def transaction_number(self):
        #compare the total number of transactions to USASpending via API
        fpds_base = 'http://www.usaspending.gov/faads/faads.php'
        print "making request"
        resp = requests.get(fpds_base, params={'detail': 's'})
        tree= et.fromstring(resp.text).find('{http://www.usaspending.gov/schemas/}data')
        tree = tree.find('{http://www.usaspending.gov/schemas/}record')
        totals = tree.find('{http://www.usaspending.gov/schemas/}totals').getchildren()
        for t in totals:
            print t.text

        fys = tree.find('{http://www.usaspending.gov/schemas/}fiscal_years').getchildren()
        for f in fys:
            print f.text

