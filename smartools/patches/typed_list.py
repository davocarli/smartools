import smartsheet

class SmartoolsTypedList(smartsheet.types.TypedList):

	def __init__(self, item_type, column_indexes=None):
		self.column_indexes = column_indexes
		super().__init__(item_type)

	def smartools(self):
		return 'smartools methods are available!'

	def __getitem__(self, idx):
		if isinstance(idx, str) and self.column_indexes is not None:
			idx = self.column_indexes[idx]
		return super().__getitem__(idx)

# Perform Monkey Patch
smartsheet.types.TypedList = SmartoolsTypedList
smartsheet.models.sheet.TypedList = SmartoolsTypedList
smartsheet.models.row.TypedList = SmartoolsTypedList
