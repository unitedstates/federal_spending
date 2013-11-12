from django.core.management.base import CommandError, BaseCommand
from django.db import connections, transaction
from django.conf import settings
from retinaburner.usaspending.scripts.usaspending.config import INDEX_COLS_BY_TABLE


class Command(BaseCommand):

    @transaction.commit_on_success
    def handle(self, *args, **kwargs):
        """
        Takes a relation name and a fiscal year and creates a partition for it.
        Current relation names for spending data are:
            usaspending_contract
            usaspending_grant
        """
        grants_base = 'usaspending_grant'
        contracts_base = 'usaspending_contract'

        for fy in settings.FISCAL_YEARS:
            self.create_partition_indexes(contracts_base, "{0}_{1}".format(contracts_base, fy))
            self.create_partition_indexes(grants_base, "{0}_{1}".format(grants_base, fy))

    def create_partition_indexes(self, base_table, partition_name):
        c = connections['default'].cursor()
        for i, colname in enumerate(INDEX_COLS_BY_TABLE[base_table]):
            if 'using' in colname or '(' in colname:
                idx_stmt = 'create index {0} on {1} {2}; commit;'.format(
                    partition_name + '_{0}'.format(i),
                    partition_name,
                    colname
                )
            else:
                idx_stmt = 'create index {0} on {1} ({2}); commit;'.format(
                    partition_name + '_{0}'.format(i),
                    partition_name,
                    colname
                )
            c.execute(idx_stmt)