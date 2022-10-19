from .typed_list import TypedListWrapper

class RowList(TypedListWrapper):

    def __init__(self, typed_list, columns=None, parent_list=None):
        super().__init__(typed_list)
        self._columns = columns
        self._parent_list = parent_list

    def __next__(self):
        item = super().__next__()
        item._columns = self._columns
        item._list = self
        return item

    def __getitem__(self, idx):
        item = super().__getitem__(idx)
        item._columns = self._columns
        item._list = self if self._parent_list is None else self._parent_list
        return item

    def __get_children__(self, row_id):
        if self._parent_list is not None:
            return self._parent_list.__get_children__(row_id)
        if row_id not in self._ref:
            self._index_items(row_id)
        result = []
        counter = self._ref[row_id] + 1
        current_row = None
        while counter < len(self._store):
            current_row = self._store[counter]
            if current_row.parent_id == row_id:
                result.append(current_row)
            counter +=1
        return RowList(result, self._columns, self._parent_list if self._parent_list is not None else self)

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
