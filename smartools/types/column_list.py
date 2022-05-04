from .typed_list import TypedListWrapper

class ColumnList(TypedListWrapper):

    def _index_items(self, idx):
        if idx in self._ref:
            return self._store[self._ref[idx]]
        
        for i in range(self._idx, len(self._store)):
            column = self._store[i]
            self._ref[column.title] = i
            self._ref[column.id] = i
            if column.primary:
                self._ref[''] = i
            self._idx += 1
            if idx in self._ref:
                return column
        raise KeyError(idx)
