import time

from smartsheet.sheets import Sheets
from smartsheet.types import TypedList

from smartools.models.enums import SmartoolsAccessLevel
from smartools.types import RowList, BulkOperationResult
from smartools.types.enumerated_value import SmartoolsEnumeratedValue

class SmartoolsSheets(Sheets):

	def bulk_add_rows(
		self,
		sheet_id,
		rows,
		n=500,
		retries=5,
		sleep=60,
		**kwargs,
		):
		result = BulkOperationResult('rows')
		current_retries = retries
		if n > 500:
			n = 500

		if not isinstance(rows, (list, tuple, TypedList, RowList)):
			rows = [rows]

		while len(rows) > 0:
			response = self.add_rows(sheet_id, rows[:n], **kwargs)
			if hasattr(response.result, 'error_code'):
				current_retries -= 1
				if response.result.error_code == 4002:
					n = n//2
				elif response.result.error_code in [4003, 4004]:
					time.sleep(sleep)
				else:
					if current_retries <= 0:
						result.responses.append(response)
						result.status = 'ERROR'
						result.error = response
						return result
			else:
				rows = rows[n:]
				current_retries = retries
				result.responses.append(response)
				result.rows.extend(response.result)
		result.status = 'SUCCESS'
		return result

	def bulk_update_rows(
		self,
		sheet_id,
		rows,
		n=500,
		retries=5,
		sleep=60,
		**kwargs,
		):
		result = BulkOperationResult('rows')
		current_retries = retries
		if n > 500:
			n = 500

		if not isinstance(rows, (list, tuple, TypedList, RowList)):
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
						result.responses.append(response)
						result.status = 'ERROR'
						result.error = response
						return result
			else:
				rows = rows[n:]
				current_retries = retries
				result.responses.append(response)
				result.rows.extend(response.result)
		result.status = 'SUCCESS'
		return result

	def get_access_level(
		self,
		sheet_id,
		):
		sheet = self.get_sheet(sheet_id, column_ids=[0], row_numbers=[0], level=1)
		if hasattr(sheet, 'result') and hasattr(sheet.result, 'error_code'):
			level = SmartoolsEnumeratedValue(SmartoolsAccessLevel)
			level.set('UNSHARED')
			return level
		return sheet.access_level
