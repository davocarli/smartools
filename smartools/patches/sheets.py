import smartsheet
from .__smartools import SmartoolsObject

smart = smartsheet.Smartsheet("INIT")
smart.Sheets

class SmartoolsSheets(smartsheet.sheets.Sheets):
	def smartools(self):
		return 'smartools methods are available!'

	def get_sheet(self, *args, **kwargs):
		sheet = super().get_sheet(*args, **kwargs)

		if 'exclude' in kwargs and 'dicts' in kwargs['exclude']:
			return sheet
		
		coldict = {}

		primary_index = None

		for column in sheet.columns:
			coldict[column.title] = column.index
			if column.primary:
				primary_index = column.index

		sheet.columns.index_reference = coldict

		rowdict = {}

		for row in sheet.rows:
			row.cells.index_reference = coldict
			primary_value = str(row.cells[primary_index].value or '')
			if primary_value not in rowdict:
				rowdict[primary_value] = row.index

		sheet.rows.index_reference = rowdict

		return sheet

	# Adds rows to a sheet. Allows you to pass a list of more than 500 rows, and automatically handles timeout errors using exponentially smaller requests
	def bulk_add_rows(self,
			sheet_id,  # The ID of the sheet the rows should be added to
			rows,  # The list of rows that should be added to the sheet
			n=500,  # The number of rows per request to begin with. Will usually be 500, but if working with a large sheet where timeouts are expected you can start smaller
			retries=5,  # The number of consecutive errors adding rows before the operation is cancelled
			sleep=60,  # The amount of time to sleep in case of rate limiting error
		**kwargs):
		result = {
			'responses': [],
			'rows': [],
			'data': [],
			'status': '',
			'error_message': None
		}

		current_retries = retries

		if n > 500:
			n = 500

		if not isinstance(rows, list):
			rows = [rows]

		while len(rows) > 0:
			response = self.add_rows(sheet_id, rows[:n], **kwargs)
			if hasattr(response.result, 'error_code'):
				current_retries -= 1:
				if response.result.error_code == 4002:
					n = n//2
				elif response.result.error_code in [4003, 4004]:
					time.sleep(sleep)
				else:
					if current_retries <= 0:
						result['responses'].append(response)
						result['status'] = 'ERROR'
						result['error_message'] = 'See last response for detailed error.'
						return SmartoolsObject(result)
			else:
				result['data'].extend(response.data)
				rows = rows[n:]
				current_retries = retries
				result['responses'].append(response)
				result['rows'].extend(response.result)
		result['status'] = 'SUCCESS'
		return SmartoolsObject(result)

	# Updates rows on a sheet. Allows you to pass a list of more than 500 rows, and automatically handles timeout errors using exponentially smaller requests 
	def bulk_update_rows(self,
			sheet_id,  # The ID of the sheet whose rows should be updated
			rows,  # The list of rows that should be updated
			n=500,  # The number of rows per request to begin with. Will usually be 500, but if working with a large sheet where timeouts are expected you can start smaller
			retries=5,  # The number of consecutive errors adding rows before the operation is cancelled
			sleep=60,  # The amount of time to sleep in case of rate limiting error
		**kwargs):
		result = {
			'responses': [],
			'rows': [],
			'data': [],
			'status': '',
			'error_message': None
		}

		current_retries = retries

		if n > 500:
			n = 500

		if not isinstance(rows, list):
			rows = [rows]

		while len(rows) > 0:
			response = self.update_rows(sheet_id, rows[:n], **kwargs)
			if hasattr(response.result, 'error_code'):
				current_retries -= 1
				if response.result.error_code == 4002:
					n = n//2
				elif response.result.error_code in [4003, 4004]:
					time.sleep(sleep)
				else:
					if current_retries <= 0:
						result['responses'].append(response)
						result['status'] = 'ERROR'
						result['error_message'] = 'See last response for detailed error.'
						return SmartoolsObject(result)
			else:
				result['data'].extend(response.data)
				rows = rows[n:]
				current_retries = retries
				result['responses'].append(response)
				result['rows'].extend(response.result)
			result['status'] = 'SUCCESS'
			return SmartoolsObject(result)

	# Takes a sheet ID and minimum permission level as arguments, then returns an object including a confirmation of whether the permission level is met
	def check_sheet_permissions(self,
			sheet_id,  # The ID of the sheet to check for permission requirements
			permission_level=None  # The minimum permission level required. Can be a number from 1-5, or a String. If None, method will just return the sheet permission level
		):
		access_levels = .__smartools.access_levels
		try:
			sheet_id = int(sheet_id)
		except:
			return SmartoolsObject({'status': 'ERROR', 'access_met': False, 'Reason': 'Sheet ID is invalid'})

		sheet = self.get_sheet(sheet_id, column_ids=[0], row_numbers=[0], level=1, exclude='dicts')

		if hasattr(sheet, 'result') and hasattr(sheet.result, 'error_code'):
			return SmartoolsObject({'status': 'ERROR', 'access_met': False, 'sheet': sheet})

		if isinstance(permission_level, str):
			permission_level = access_levels[permission_level]

		if permission_level is None:
			return SmartoolsObject({'status': 'ERROR', 'access_met': False, 'access_level': sheet.access_level})
		else:
			permission_met = permission_level <= access_levels[str(sheet.access_level)]
			return SmartoolsObject({'status': 'SUCCESS', 'access_met': permission_met, 'access_level': sheet.access_level, 'sheet_response': sheet})

# Perform Monkey Patch
smartsheet.sheets.Sheets = SmartoolsSheets