from smartsheet.models import Column
from .cell_format import CellFormat

class SmartoolsColumn(Column):

    @property
    def format(self):
        return CellFormat(self.format_)

    @format.setter
    def format(self, value):
        if isinstance(value, CellFormat):
            value = str(value)
        self.format_ = value

    def __setattr__(self, key, value):
        super(Column, self).__setattr__(key, value)
