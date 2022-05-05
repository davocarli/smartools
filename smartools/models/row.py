from smartsheet.models import Row
from smartools.types import CellList
from .cell_format import CellFormat

class SmartoolsRow(Row):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cells = CellList(self._cells)

    @property
    def cells(self):
        self._cells._columns = self._columns
        return self._cells

    @cells.setter
    def cells(self, value):
        if isinstance(self._cells, CellList):
            self._cells._store.load(value)
        else:
            self._cells.load(value)

    def __getattr__(self, key):
        if key == 'format':
            return CellFormat(self._format_)
        else:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        if key == 'format':
            self._format_ = str(value)
        else:
            super(SmartoolsRow, self).__setattr__(key, value)
