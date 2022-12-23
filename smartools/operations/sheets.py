import time
from typing import TYPE_CHECKING
from json.decoder import JSONDecodeError

from smartsheet.sheets import Sheets
from smartsheet.types import TypedList

from smartools.models.enums import SmartoolsAccessLevel
from smartools.types import RowList, BulkOperationResult
from smartools.types.enumerated_value import SmartoolsEnumeratedValue

if TYPE_CHECKING:
	from smartools.models.row import SmartoolsRow
	from typing import Iterable

class SmartoolsSheets(Sheets):

	def bulk_add_rows(
		self,
		sheet_id: int,
		rows: "SmartoolsRow | Iterable[SmartoolsRow]",
		n: int=500,
		retries: int=5,
		sleep: int=60,
		**kwargs,
	) -> BulkOperationResult:
		"""Adds rows in bulk, automatically handling pagination.

		This method will add a list of rows to a sheet. If more than 500
		rows are in the list, it will automatically be separated into
		requests of 500 rows each. If an error is encountered, the number of
		rows per request will be halved and re-attempted. If *specifically* a
		rate limiting error is encountered, the method will automatically pause
		to adjust to the rate limit.

		Args:
			sheet_id (int): The ID of the sheet to add the rows to.
			rows (Row): A list of rows to be added.
			n (int, optional): Number of rows per request. Defaults to 500.
			retries (int, optional): Number of times to retry before
			    raising an exception. Defaults to 5.
			sleep (int, optional): Number of seconds to wait before retrying
			    when encountering a rate limiting error. Defaults to 60.
			**kwargs: Additional keyword arguments to be passed to the add_rows
				method.

		Returns:
			BulkOperationResult: A Smartools BulkOperationResult.
		"""
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
		sheet_id: int,
		rows: "SmartoolsRow | Iterable[SmartoolsRow]",
		n: int=500,
		retries: int=5,
		sleep: int=60,
		**kwargs,
	) -> BulkOperationResult:
		"""Updates rows in bulk, automatically handling pagination.

		This method will update a list of rows in a sheet. If more than 500
		rows are in the list, it will automatically be separated into
		requests of 500 rows each. If an error is encountered, the number of
		rows per request will be halved and re-attempted. If *specifically* a
		rate limiting error is encountered, the method will automatically pause
		to adjust to the rate limit.

		Args:
			sheet_id (int): The ID of the sheet to add the rows to.
			rows (Row): A list of rows to be added.
			n (int, optional): Number of rows per request. Defaults to 500.
			retries (int, optional): Number of times to retry before
			    raising an exception. Defaults to 5.
			sleep (int, optional): Number of seconds to wait before retrying
			    when encountering a rate limiting error. Defaults to 60.
			**kwargs: Additional keyword arguments to be passed to the add_rows
				method.

		Returns:
			BulkOperationResult: A Smartools BulkOperationResult.
		"""
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

	def bulk_delete_rows(
		self,
		sheet_id: int,
		ids: "int | Iterable[int]",
		n: int=375,
		retries: int=5,
		sleep: int=60,
		**kwargs,
	) -> BulkOperationResult:
		"""Deletes rows from a sheet in bulk, automatically handling pagination.

		Will automatically delete rows with a page size of 380 rows per request.
		The limit for the number of rows that can be deleted in one request is
		based on the total length of the request url. 380 rows should not exceed
		the limit. If the method encounters a rate limiting error, it will sleep
		to reset the limit. If it encounters another error, it will halve the
		number of rows being deleted.

		Args:
			sheet_id (int): The ID of the sheet the rows will be deleted from.
			ids (Iterable[int]): A list of ids of the rows to be deleted.
			n (int, optional): The number of rows to delete per request. Defaults to 375.
			retries (int, optional): The number of times to retry before
			    throwing an error.. Defaults to 5.
			sleep (int, optional): The number of seconds to wait in
			    the case of a rate limit error. Defaults to 60.

		Returns:
			BulkOperationResult: A BulkOperationResult containing the data from
				all the requests.
		"""
		result = BulkOperationResult('data')
		current_retries = retries
		if n > 385:
			n = 385

		if isinstance(ids, int):
			ids = [ids]
		
		while len(ids) > 0:
			try:
				response = self.delete_rows(sheet_id, ids[:n], **kwargs)
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
					ids = ids[n:]
					current_retries = retries
					result.responses.append(response)
					result.data.extend(response.data)
			except JSONDecodeError:
				current_retries -= 1
				n = n//2
				if current_retries <= 0:
					result.responses.append(response)
					result.status = 'ERROR'
					result.error = response
					return result
		result.status = 'SUCCESS'
		return result
	def get_access_level(
		self,
		sheet_id,
	) -> SmartoolsAccessLevel:
		"""Returns the access level for a sheet, making the request/response size as small as possible.

		Makes a respons to get a sheet without including any columns or rows, to keep the request
		as small as possible, then returns the access level to the sheet.

		Args:
			sheet_id (int): The ID of the sheet whose access level should be returned.

		Returns:
			SmartoolsAccessLevel: The Access Level for the sheet.
		"""
		sheet = self.get_sheet(sheet_id, column_ids=[0], row_numbers=[0], level=1)
		if hasattr(sheet, 'result') and hasattr(sheet.result, 'error_code'):
			level = SmartoolsEnumeratedValue(SmartoolsAccessLevel)
			level.set('UNSHARED')
			return level
		return sheet.access_level
