from smartsheet.models import SummaryField
from .cell_format import CellFormat

class SmartoolsSummaryField(SummaryField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._format_ = CellFormat(self._format_)

    @property
    def format_(self):
        return self._format_

    @format_.setter
    def format_(self, value):
        self._format_ = CellFormat(value)
