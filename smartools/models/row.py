from smartsheet.models import Row
from smartools.types import CellList
from .cell_format import CellFormat

class SmartoolsRow(Row):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cells = CellList(self._cells)
        self._format_ = CellFormat(self._format_)

    @property
    def format_(self):
        return self._format_

    @format_.setter
    def format_(self, value):
        self._format_ = CellFormat(value)

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
        if key == 'children':
            return self._get_children()
        return super().__getattr__(key)

    def _get_children(self):
        if hasattr(self, '_list') is not None:
            return self._list.__get_children__(self.id)
        return None
        
    # def __getattr__(self, key):
    #     if key == 'format':
    #         return CellFormat(self._format_)
    #     elif key == 'id':
    #         return self.id_
    #     else:
    #         super(SmartoolsRow, self).__getattr__(key)

    # def __setattr__(self, key, value):
    #     if key == 'format':
    #         self._format_ = str(value)
    #     elif key == 'id':
    #         self.id_ = value
    #     else:
    #         super(SmartoolsRow, self).__setattr__(key, value)
