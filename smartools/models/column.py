from smartsheet.models import Column
from .cell_format import CellFormat

class SmartoolsColumn(Column):

    def __getattr__(self, key):
        if key == 'format':
            return CellFormat(self._format_)
        else:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        if key == 'format':
            self._format_ = str(value)
        else:
            super(SmartoolsColumn, self).__setattr__(key, value)
