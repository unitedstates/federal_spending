from faads import FIELDS, CALCULATED_FIELDS
import os.path
from django.db import connection
from django.db import transaction

class Loader():
    def fields(self):
        return [ x[0] for x in FIELDS ] + [ x[0] for x in CALCULATED_FIELDS ]

    def sql_str(self, infile):
        table = 'usaspending_grant'
        return self.sql_template_postgres(infile, table, self.fields())

    def print_sql(self, infile):
        print self.sql_str(infile)

    def sql_template_postgres(self, file_, table, fields):
        return """
            copy {1} \
            ({2}) \
            FROM '{0}' \
            DELIMITER '|' \
            CSV QUOTE '"' \
            NULL 'NULL' \
            (PARTITIONING)
        """.format(os.path.abspath(file_), table, ', '.join(fields))

    @transaction.commit_on_success
    def insert_faads(self, infile):
        sql = self.sql_str(infile)
        cursor = connection.cursor()
        cursor.execute(sql);