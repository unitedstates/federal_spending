from federal_spending.usaspending.models import Contract
from federal_spending.usaspending.scripts.usaspending.contracts_loader import Loader
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):

    @transaction.commit_on_success
    def handle(self, contracts_file, **options):
        #print "Current number of rows in contract table: {0}".format(Contract.objects.all().count())

        Loader().insert_fpds(contracts_file)
        #transaction.set_dirty()

        #print "New number of rows in contract table: {0}".format(Contract.objects.all().count())