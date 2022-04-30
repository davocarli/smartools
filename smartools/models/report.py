from smartsheet.models import Report

from smartools.types import ColumnList, RowList

class SmartoolsReport(Report):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._columns = ColumnList(self._columns)
        self._rows = RowList(self._rows, columns=self._columns)
        
