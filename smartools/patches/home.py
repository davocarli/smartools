import smartsheet

smart = smartsheet.Smartsheet("INIT")
smart.Home

class SmartoolsHome(smartsheet.home.Home):
	def smartools(self):
		return 'smartools methods are available!'

	# def get_container_from_url(self,
	# 		container_url,  # THe url to be matched to an existingSmartsheet item
	# 		search_list=None  # (Optional) A list of items to search through. If provided will not reload Home.
	# 	):
	# 	q = container_url.find('?')
	# 	if q != -1:
	# 		container_url = container_url[:q]

	# 	items = []

	# 	if search_list != None:
	# 		if hasattr(search_list, 'data'):
	# 			items = search_list.data
	# 		else:
	# 			items = search_list
	# 	elif '/sheets/' in container_url:
	# 		response = self.smart.Sheets.list_sheets(include_all=True)
	# 		items = response.data
	# 	elif '/reports/' in container_url:
	# 		response = self.smart.Reports.list_reports(include_all=True)
	# 		items = response.data
	# 	elif '/dashboards/' in container_url:
	# 		response = self.smart.Sights.list_sights(include_all=True)
	# 		items = response.data

	# 	for item in items:
	# 		if item.permalink.endswith(container_url):
	# 			return item

	# 	return None

# Perform Monkey Patch
smartsheet.home.Home = SmartoolsHome