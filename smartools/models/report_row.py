from smartsheet.models import ReportRow
from smartools.types import CellList

class SmartoolsReportRow(ReportRow):

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
