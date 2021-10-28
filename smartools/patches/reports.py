import smartsheet
from smartsheet import fresh_operation

smart = smartsheet.Smartsheet("INIT")
smart.Reports

class SmartoolsReports(smartsheet.reports.Reports):
	def smartools(self):
		return 'smartools methods are available!'

	def create_report(self):
		"""Creates a report in the "Sheets" folder.
		
		Returns: Result
		"""
		_op = fresh_operation('create_report')
		_op['method'] = 'PUT'
		_op['path'] = '/internal/reports'
		_op['json'] = {}

		expected = ['Result', 'Report']

		prepped_request = self._base.prepare_request(_op)
		response = self._base.request(prepped_request, expected, _op)

		return response
	
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


# Perform Monkey Patch
smartsheet.reports.Reports = SmartoolsReports