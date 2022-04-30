import math

from smartsheet import fresh_operation
from smartsheet.reports import Reports

from smartools.types.enumerated_value import SmartoolsEnumeratedValue
from smartools.models.enums import SmartoolsAccessLevel

class SmartoolsReports(Reports):
	
	def update_report(self, report_id, report_obj):
		"""Updates the specified Report.

		Args:
			report_id (int): Report ID
			report_obj (Report): Report object

		Returns:
			Result
		"""
		_op = fresh_operation('update_report')
		_op['method'] = 'PUT'
		_op['path'] = '/reports/' + str(report_id)
		_op['json'] = report_obj

		expected = ['Result', 'Report']

		prepped_request = self._base.prepare_request(_op)
		response = self._base.request(prepped_request, expected, _op)

		return response

	def move_report(self, report_id, container_destination_obj):
		"""Creates a copy of the specified Report

		Args:
			report_id (int): Report ID
			container_destination_obj
				(ContainerDestination): Container Destination object.

		Returns:
			Result
		"""
		_op = fresh_operation('move_report')
		_op['method'] = 'POST'
		_op['path'] = '/reports/' + str(report_id) + '/move'
		_op['json'] = container_destination_obj

		expected = ['Result', 'Report']

		prepped_request = self._base.prepare_request(_op)
		response = self._base.request(prepped_request, expected, _op)

		return response

	def get_large_report(self, report_id, page_size=None, include=None, level=None, **kwargs):
		"""Load a large report by automatically handling paging
		
		Args:
			Same as get_report with 'page' removed.
			**kwargs are passed to get_report for future compatibility.

		Returns:
			Report
		"""
		if 'page' in kwargs:
			raise TypeError("You may not specify 'page' when using get_large_report")
		
		report = self.get_report(
			report_id=report_id,
			page_size=page_size,
			page=1,
			include=include,
			level=level,
			**kwargs,
		)

		total_pages = math.ceil(report.total_row_count / len(report.rows))

		for i in range(2, total_pages + 1):
			print(f'getting page {i}')
			next_page = self.get_report(
				report_id=report_id,
				page_size=page_size,
				page=i,
				include=include,
				level=level,
				**kwargs,
			)
			report.rows.extend(next_page.rows)
		
		return report

	def get_access_level(
		self,
		report_id,
		):
		report = self.get_report(report_id, page=0)
		if hasattr(report, 'result') and hasattr(report.result, 'error_code'):
			level = SmartoolsEnumeratedValue(SmartoolsAccessLevel)
			level.set('UNSHARED')
			return level
		return report.access_level
