from smartsheet.models import Cell
from .cell_format import CellFormat

class SmartoolsCell(Cell):

    @property
    def format(self):
        return CellFormat(self.format_)

    @format.setter
    def format(self, value):
        if isinstance(value, CellFormat):
            value = str(value)
        self.format_ = value

    def __setattr__(self, key, value):
        if key == 'format':
            self.format_ = value
        super(SmartoolsCell, self).__setattr__(key, value)
