from smartsheet.models import Column
from .cell_format import CellFormat

class SmartoolsColumn(Column):

    def __getattr__(self, key):
        if key == 'format':
            return CellFormat(self._format_)
        elif key == 'id':
            return self.id_
        elif key == 'type':
            return self.type_
        else:
            super(SmartoolsColumn, self).__getattr__(key)
        
    def __setattr__(self, key, value):
        if key == 'format':
            self._format_ = str(value) 
        elif key == 'id':
            self.id_ = value
        elif key == 'type':
            self.type_ = value
        else:
            super(Column, self).__setattr__(key, value)

