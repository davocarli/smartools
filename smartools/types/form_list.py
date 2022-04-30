from .typed_list import TypedListWrapper

class FormList(TypedListWrapper):

    def __init__(self, typed_list):
        super().__init__(typed_list)

    def _index_items(self, idx):
        if idx in self._ref:
            return self._store[self._ref[idx]]
        
        for i in range(self._idx, len(self._store)):
            form = self._store[i]
            self._ref[form.title] = i
            if str(form.title) == idx:
                return form
        
        raise KeyError(idx)
