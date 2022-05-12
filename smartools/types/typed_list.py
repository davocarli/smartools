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

	def __getattr__(self, key):
		return getattr(self._store, key)

	def __iter__(self):
		self._current_index = 0
		return self

	def __next__(self):
		if len(self) <= self._current_index:
			raise StopIteration
		item = self._store[self._current_index]
		self._current_index += 1
		return item

	def __getitem__(self, idx):
		try:
			item = self._store[idx]
			if isinstance(item, (TypedList, list)):
				return self.__class__(item)
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

	def __contains__(self, key):
		try:
			self.__getitem__(key)
			return True
		except KeyError:
			return False
