from smartsheet.home import Home
from smartsheet import fresh_operation

class SmartoolsHome(Home):

	def get_container_from_url(self,
			container_url,
			search_list=None,
		):
		q = container_url.find('?')
		if q != -1:
			container_url = container_url[:q]

		items = []

		if search_list != None:
			if hasattr(search_list, 'data'):
				items = search_list.data
			else:
				items = search_list
		elif '/sheets/' in container_url:
			response = self._base.Sheets.list_sheets(include_all=True)
			items = response.data
		elif '/reports/' in container_url:
			response = self._base.Reports.list_reports(include_all=True)
			items = response.data
		elif '/dashboards/' in container_url:
			response = self._base.Sights.list_sights(include_all=True)
			items = response.data

		for item in items:
			if item.permalink.endswith(container_url):
				return item

		return None

	def create_sight(self, sight_obj):
		"""Create a dashboard from scratch in the user's Sheets folder within
		Home.

		Args:
			sight_obj (Sight): Sight object.
		
		Returns: Result
		"""
		_op = fresh_operation('create_sight')
		_op['method'] = 'POST'
		_op['path'] = '/internal/sights'
		_op['json'] = {}

		expected = ['Result', 'Sight']

		prepped_request = self._base.prepare_request(_op)
		response = self._base.request(prepped_request, expected, _op)
		
		updated_sight = self._base.Sights.update_sight(response.result.id, sight_obj)

		return updated_sight

	def create_report(self, report_obj):
		"""Create a report from scratch in the user's Sheets folder within
		Home.

		Args:
			report_obj (Report): Report object.
		
		Returns: Result
		"""
		_op = fresh_operation('create_report')
		_op['method'] = 'POST'
		_op['path'] = '/internal/reports'
		_op['json'] = {}

		expected = ['Result', 'Report']

		prepped_request = self._base.prepare_request(_op)
		response = self._base.request(prepped_request, expected, _op)
		
		updated_report = self._base.Reports.update_report(response.result.id, report_obj)

		return updated_report
