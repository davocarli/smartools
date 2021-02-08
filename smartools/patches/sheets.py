import smartsheet

smart = smartsheet.Smartsheet("INIT")
smart.Sheets

class SmartoolsSheets(smartsheet.sheets.Sheets):
	def smartools(self):
		return 'smartools methods are available!'

	def get_sheet(self, *args, **kwargs):
		if not ('list_dict' in kwargs and not kwargs.pop('list_dict')):
			sheet = super().get_sheet(*args, **kwargs)
			coldict = {}
			for column in sheet.columns:
				coldict[column.title] = column.index

			sheet.columns.index_reference = coldict

			for row in sheet.rows:
				row.cells.index_reference = coldict
		else:
			sheet = super().get_sheet(*args, **kwargs)

		return sheet

# Perform Monkey Patch
smartsheet.sheets.Sheets = SmartoolsSheets
