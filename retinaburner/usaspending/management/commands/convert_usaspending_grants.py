from retinaburner.usaspending.management.base.usaspending_importer import BaseUSASpendingConverter
from retinaburner.usaspending.grants.models import Grant
from retinaburner.usaspending.scripts.usaspending import faads


class Command(BaseUSASpendingConverter):
    modelclass = Grant
    outfile_basename = 'grants'
    module = faads


    def __init__(self):
        super(Command, self).__init__()

    
    def file_is_right_type(self, file_):
        return 'Contracts' not in file_