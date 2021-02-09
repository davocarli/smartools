import smartsheet

class SmartoolsTypedList(smartsheet.types.TypedList):

	def __init__(self, item_type, index_reference=None):
		self.index_reference = index_reference
		super().__init__(item_type)

	def smartools(self):
		return 'smartools methods are available!'

	def __getitem__(self, idx):
		if isinstance(idx, str) and self.index_reference is not None:
			idx = self.index_reference[idx]
		return super().__getitem__(idx)

# Perform Monkey Patch
smartsheet.types.TypedList = SmartoolsTypedList
smartsheet.models.sheet.TypedList = SmartoolsTypedList
smartsheet.models.row.TypedList = SmartoolsTypedList
