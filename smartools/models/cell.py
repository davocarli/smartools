from smartsheet.models import Cell
from .cell_format import CellFormat

class SmartoolsCell(Cell):
    # # @property
    # # def format_(self):
    # #     print('getting format')
    # #     return CellFormat(self._format_)

    # # @format_.setter
    # # def format_(self, value):
    # #     print('setting format')
    # #     if isinstance(value, CellFormat):
    # #         value = str(value)
    # #     self._format_ = value

    def __getattr__(self, key):
        if key in ('format', 'format_'):
            return CellFormat(self._format_)
        else:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        if key == 'format':
            self._format_ = str(value)
        else:
            super(Cell, self).__setattr__(key, value)

    # # def __getattr__(self, key):
    # #     print('getting ' + key)
    # #     print()
    # #     super(SmartoolsCell, self).__getattr__(key)

    # # def __setattr__(self, key, value):
    # #     print(f'setting {key}')
    # #     try:
    # #         print(f'setting to {value}')
    # #     except:
    # #         print('cant print')
    # #     print()
    # #     super(SmartoolsCell, self).__setattr__(key, value)

    # # def __setattr__(self, key, value):
    # #     super(SmartoolsCell, self).__setattr__(key, value)
