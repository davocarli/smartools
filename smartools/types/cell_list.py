from .typed_list import TypedListWrapper

class CellList(TypedListWrapper):

    def __init__(self, typed_list, columns=None):
        super().__init__(typed_list)
        self._columns = columns

    def _index_items(self, idx):
        if self._columns is not None:
            index = self._columns[idx].index
            return self._store[index]
        return super()._index_items(idx)
