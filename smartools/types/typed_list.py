from smartsheet.types import TypedList
from smartsheet.smartsheet import serialize

class TypedListWrapper:

	def __init__(
		self,
		typed_list: TypedList,
		):
		self._store = typed_list
		self._ref = {}
		self._idx = 0

	def __getattr__(self, val):
		return self._store.__getattribute__(val)

	def __iter__(self):
		return self._store.__iter__()

	def __next__(self):
		return self._store.__next__()

	def __getitem__(self, idx):
		try:
			return self._store[idx]
		except (IndexError, TypeError):
			if idx in self._ref:
				return self._store[self._ref[idx]]
			else:
				return self._index_items(idx)

	def serialize(self):
		return serialize(self._store)

	# Method should be overwritten by subclasses
	def _index_items(self, idx):
		raise KeyError(idx)

	def __len__(self):
		return self._store.__len__()
