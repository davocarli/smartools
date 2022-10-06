from .typed_list import TypedListWrapper

class RowList(TypedListWrapper):

    def __init__(self, typed_list, columns=None):
        super().__init__(typed_list)
        self._columns = columns

    def __next__(self):
        item = super().__next__()
        item._columns = self._columns
        return item

    def __getitem__(self, idx):
        item = super().__getitem__(idx)
        item._columns = self._columns
        return item

    def _index_items(self, idx):
        primary_idx = self._columns[''].index
        for i in range(self._idx, len(self._store)):
            row = self._store[i]
            primary_value = str(row.cells[primary_idx].value or '')
            self._ref[row.id] = i
            if primary_value not in self._ref:
                self._ref[primary_value] = i
            if primary_value == idx or idx == row.id:
                return row
        raise KeyError(idx)
