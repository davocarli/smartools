from smartsheet.types import TypedList

from .typed_list import TypedListWrapper

class ContainerList(TypedListWrapper):

    def __init__(self, container_type):
        super().__init__(TypedList(container_type))

    def _index_items(self, idx):        
        for i in range(self._idx, len(self._store)):
            cont = self._store[i]
            self._ref[cont.id] = i
            self._ref[cont.name] = i
            if idx in self._ref:
                return cont
        
        raise KeyError(idx)
