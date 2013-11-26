from federal_spending.usaspending.management.base.usaspending_importer import BaseUSASpendingConverter
from federal_spending.usaspending.models import Grant
from federal_spending.usaspending.scripts.usaspending import faads


class Command(BaseUSASpendingConverter):
    modelclass = Grant
    outfile_basename = 'grants'
    module = faads

    def __init__(self):
        super(Command, self).__init__()

    
    def file_is_right_type(self, file_):
        if 'Grants' in file_: return True
        if 'Loans' in file_: return True
        if 'DirectPayments' in file_: return True
        if 'Insurance' in file_: return True

        return False