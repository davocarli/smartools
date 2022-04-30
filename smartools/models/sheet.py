from smartsheet.models import Sheet
from smartsheet.types import TypedList

from smartools.types import ColumnList, RowList, FormList
from .sheet_form import SheetForm

class SmartoolsSheet(Sheet):

    def __init__(self, *args, **kwargs):
        self._forms = TypedList(SheetForm)
        super().__init__(*args, **kwargs)
        self._columns = ColumnList(self._columns)
        self._rows = RowList(self._rows, columns=self._columns)
        self._forms = FormList(self._forms)

    @property
    def forms(self):
        return self._forms
    
    @forms.setter
    def forms(self, value):
        self._forms.load(value)
