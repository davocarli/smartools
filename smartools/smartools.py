from smartsheet import *
import smartsheet
import os
import time
import warnings

"""
	In an earlier version of this module, all of the added methods were in this Util class, instead
	of being monkey patched into their more logical classes (Sheets, Workspaces, etc.). To ensure
	compatibility with prior-written software, this Util class remains, but calling methosd here will
	issue a deprecation warning.

	Most of the original code for this class has been commented out, and will be removed at a later date.
"""

class Smartsheet(smartsheet.Smartsheet):

	def __init__(self, *args, **kwargs):
		self.Util = self.SmartsheetUtilities(self)
		super().__init__(*args, **kwargs)


	class SmartsheetUtilities():

		def __init__(self, smart):
			self.smart = smart
			self.access_levels = {
				'VIEWER': 1,
				'EDITOR': 2,
				'EDITOR_SHARE': 3,
				'ADMIN': 4,
				'OWNER': 5
			}
			self.include_all = 'attachments,cellLinks,data,discussions,filters,forms,rules,ruleRecipients,all,columnType,format,objectValue,rowPermalink,rowWriterInfo,writerInfo'


		# # Returns a list of all the sheets in a workspace. Optionally only includes sheets with specific Strings contained in the sheet name
		# def list_sheets_in_workspace(self,
		# 		workspace_id,  # The ID of the workspace whose sheets should be returned
		# 		contains=None,  # (Optional) A String that should be contained in the sheet's sheet names to be included in the return
		# 		exact=False,  # If set to True, will only return sheets with exactly the the name provided in the "contains" argument, rather than a partial match
		# 		parent=None  # Used for recursively providing information to this method. Should not be provided by users
		# 	):
		# 	sheets = []
		# 	if parent == None:
		# 		parent = self.smart.Workspaces.get_workspace(workspace_id, load_all=True)
		# 	for sheet in parent.sheets:
		# 		if (contains is None) \
		# 		or (exact and contains == sheet.name) \
		# 		or contains in sheet.name:
		# 			sheets.append(sheet)
		# 	for folder in parent.folders:
		# 		sheets.extend(self.list_sheets_in_workspace(workspace_id=None, contains=contains, exact=exact, parent=folder))
		# 	return sheets

		def list_sheets_in_workspace(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Workspaces.list_sheets_in_workspace instead.', DeprecationWarning)
			return self.smart.Workspaces.list_sheets_in_workspace(*args, **kwargs)


		# # Returns an object with lists of all containers in a workspace. Optionally only includes containers with specific Strings contained in the sheet name
		# def list_containers_in_workspace(self,
		# 		workspace_id,  # The ID of the workspace whose containers should be returned
		# 		contains=None,  # (Optional) A String that should be contained in the container's name to be included in the return
		# 		exact=False,  # If set to True, will only return sheets with exactly the name provided in the "contains" argument, rather than a partial match
		# 		parent=None  # Used for recursively providing information to this method. Should not be provided by users
		# 	):
		# 	containers={
		# 		'sheets': [],
		# 		'sights': [],
		# 		'reports': []
		# 	}
		# 	if parent == None:
		# 		parent = self.smart.Workspaces.get_workspace(workspace_id, load_all=True)
		# 	for sheet in parent.sheets:
		# 		if (contains is None) \
		# 		or (exact and contains == sheet.name) \
		# 		or contains in sheet.name:
		# 			containers['sheets'].append(sheet.name)
		# 	for sight in parent.sights:
		# 		if (contains is None) \
		# 		or (exact and contains == sight.name) \
		# 		or contains in sight.name:
		# 			containers['sights'].append(sight.name)
		# 	for report in parent.reports:
		# 		if (contains is None) \
		# 		or (exact and contains == report.name) \
		# 		or contains in report.name:
		# 			containers['reports'].append(report.name)
		# 	for folder in parent.folders:
		# 		child = self.list_containers_in_workspace(workspace_id=None, contains=contains, exact=exact, parent=folder)
		# 		containers['sheets'].extend(child.sheets)
		# 		containers['sights'].extend(child.sights)
		# 		containers['reports'].extend(child.reports)
		# 	return SmartoolsObject(containers)

		def list_containers_in_workspace(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Workspaces.list_containers_in_workspace instead.', DeprecationWarning)
			return self.smart.Workspaces.list_containers_in_workspace(*args, **kwargs)


		# # Returns a list of all the sheets in a folder. Optionally only includes sheets with specific Strings contained in the sheet name
		# def list_sheets_in_folder(self,
		# 		folder_id,  # The ID of the folder whose sheets should be returned
		# 		contains=None,  # (Optional) A String that should be contained in the sheet's name to be included in the returned list
		# 		exact=False  # If set to True, will only return sheets with exactly the name provided in the "contains" argument, rather than a partial match
		# 	):
		# 	sheets = []
		# 	parent = self.smart.Folders.get_folder(folder_id)
		# 	for sheet in parent.sheets:
		# 		if (contains is None) \
		# 		or (exact and contains == sheet.name) \
		# 		or contains in sheet.name:
		# 			sheets.append(sheet)
		# 	for folder in parent.folders:
		# 		sheets.extend(self.list_sheets_in_folder(folder_id=folder.id, contains=contains, exact=exact))
		# 	return sheets

		def list_sheets_in_folder(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Folders.list_sheets_in_folder instead.', DeprecationWarning)
			return self.smart.Folders.list_sheets_in_folder(*args, **kwargs)


		# # Returns an object with lists of all containers in a workspace. Optionally only includes containers with specific Strings contained in the sheet name
		# def list_containers_in_folder(self,
		# 		folder_id,  # The ID of the folder whose containers should be returned
		# 		contains=None,  # (Optional) A String that should be contained in the container's name to be included in the returned object
		# 		exact=False  # If set to True, will only return containers with exactly the name provided in the "contains" argument, rather than a partial match
		# 	):
		# 	containers = {
		# 		'sheets': [],
		# 		'sights': [],
		# 		'reports': []
		# 	}
		# 	parent = self.smart.Folders.get_folder(folder_id)
		# 	for sheet in parent.sheets:
		# 		if (contains is None) \
		# 		or (exact and contains == sheet.name) \
		# 		or contains in sheet.name:
		# 			containers['sheets'].append(sheet)
		# 	for sight in parent.sights:
		# 		if (contains is None) \
		# 		or (exact and contains == sight.name) \
		# 		or contains in sight.name:
		# 			containers['sights'].append(sight)
		# 	for report in parent.reports:
		# 		if (contains is None) \
		# 		or (exact and contains == report.name) \
		# 		or contains in report.name:
		# 			containers['reports'].append(report)
		# 	for folder in parent.folders:
		# 		child = self.list_containers_in_folder(folder_id=folder.id, contains=contains, exact=exact)
		# 		containers['sheets'].extend(child.sheets)
		# 		containers['sights'].extend(child.sights)
		# 		containers['reports'].extend(child.reports)
		# 	return SmartoolsObject(containers)

		def list_containers_in_folder(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Folders.list_containers_in_folder instead.', DeprecationWarning)
			return self.smart.Folders.list_containers_in_folder(*args, **kwargs)


		# # Adds rows to a sheet. Allows you to pass a list of more than 500 rows, and automatically handles timeout errors using exponentially smaller requests
		# def bulk_add_rows(self,
		# 		sheet_id,  # The ID of the sheet the rows should be added to
		# 		rows,  # The list of rows that should be added to the sheet
		# 		n=500,  # The number of rows per request to begin with. Will usually be 500, but if working with a large sheet where timeouts are expected you can start smaller
		# 		retries=5  # The number of consecutive errors adding rows before the operation is cancelled
		# 	):
		# 	result = {
		# 		'responses': [],
		# 		'rows': [],
		# 		'data': [],
		# 		'status': '',
		# 		'error_message': None
		# 	}

		# 	current_retries = retries

		# 	if n > 500:
		# 		n = 500

		# 	if not isinstance(rows, list):
		# 		rows = [rows]

		# 	while len(rows) > 0:
		# 		response = self.smart.Sheets.add_rows(sheet_id, rows[:n])
		# 		if hasattr(response.result, 'error_code'):
		# 			current_retries -= 1
		# 			if response.result.error_code == 4002:
		# 				n = n//2
		# 			elif response.result.error_code in [4003, 4004]:
		# 				time.sleep(60)
		# 			else:
		# 				if current_retries <= 0:
		# 					result['responses'].append(response)
		# 					result['status'] = 'ERROR'
		# 					result['error_message'] = 'See last response for detailed error.'
		# 					return SmartoolsObject(result)
		# 		else:
		# 			result['data'].extend(response.data)
		# 			rows = rows[n:]
		# 			current_retries = retries
		# 			result['responses'].append(response)
		# 			result['rows'].extend(response.result)
		# 	result['status'] = 'SUCCESS'
		# 	return SmartoolsObject(result)

		def bulk_add_rows(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Sheets.bulk_add_rows instead.', DeprecationWarning)
			return self.smart.Sheets.bulk_add_rows(*args, **kwargs)


		# # Updates rows on a sheet. Allows you to pass a list of more than 500 rows, and automatically handles timeout errors using exponentially smaller requests 
		# def bulk_update_rows(self,
		# 		sheet_id,  # The ID of the sheet whose rows should be updated
		# 		rows,  # The list of rows that should be updated
		# 		n=500,  # The number of rows per request to begin with. Will usually be 500, but if working with a large sheet where timeouts are expected you can start smaller
		# 		retries=5  # The number of consecutive errors adding rows before the operation is cancelled
		# 	):
		# 	result = {
		# 		'responses': [],
		# 		'rows': [],
		# 		'data': [],
		# 		'status': '',
		# 		'error_message': None
		# 	}

		# 	current_retries = retries

		# 	if n > 500:
		# 		n = 500

		# 	if not isinstance(rows, list):
		# 		rows = [rows]

		# 	while len(rows) > 0:
		# 		response = self.smart.Sheets.update_rows(sheet_id, rows[:n])
		# 		if hasattr(response.result, 'error_code'):
		# 			current_retries -= 1
		# 			if response.result.error_code == 4002:
		# 				n = n//2
		# 			elif response.result.error_code in [4003, 4004]:
		# 				time.sleep(60)
		# 			else:
		# 				if current_retries <= 0:
		# 					result['responses'].append(response)
		# 					result['status'] = 'ERROR'
		# 					result['error_message'] = 'See last response for detailed error.'
		# 					return SmartoolsObject(result)
		# 		else:
		# 			result['data'].extend(response.data)
		# 			rows = rows[n:]
		# 			current_retries = retries
		# 			result['responses'].append(response)
		# 			result['rows'].extend(response.result)
		# 		result['status'] = 'SUCCESS'
		# 		return SmartoolsObject(result)

		def bulk_update_rows(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Sheets.bulk_update_rows instead.', DeprecationWarning)
			return self.smart.Sheets.bulk_update_rows(*args, **kwargs)


		# # Retrieves a sheet then returns a pandas DataFrame of the sheet's data
		# def get_sheet_as_pandas_dataframe(self,
		# 		sheet_id,  # The ID of the sheet to be returned
		# 		label_column=None  # The column to be used for row labels of the DataFrame. If not provided the primary column will be used
		# 	):
		# 	try:
		# 		import pandas as pd
		# 	except ImportError:
		# 		raise RequirementError({'message': 'Import Error: This method requires the pandas module', 'recommended_action': 'Install pandas by using "pip install pandas"'})
		# 	if isinstance(sheet_id, int):
		# 		sheet = self.smart.Sheets.get_sheet(sheet_id)

		# 		pd_row_data = []
		# 		pd_row_labels = []
		# 		pd_columns = []

		# 		for column in sheet.columns:
		# 			if (label_column is None and column.primary == True):
		# 				label_column = column.id
		# 			elif column.id == label_column or column.title == label_column:
		# 				label_column = column.id
		# 			else:
		# 				pd_columns.append(column.title)

		# 		for row in sheet.rows:
		# 			row_list = []
		# 			for cell in row.cells:
		# 				if cell.column_id == label_column:
		# 					pd_row_labels.append(cell.value)
		# 				else:
		# 					row_list.append(cell.value)
		# 			pd_row_data.append(row_list)

		# 		return pd.DataFrame(pd_row_data, columns=pd_columns, index=pd_row_labels)


		def get_sheet_as_pandas_dataframe(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Sheets.get_sheet_as_pandas_dataframe instead.', DeprecationWarning)
			return self.smart.Sheets.get_sheet_as_pandas_dataframe(*args, **kwargs)

		# # Takes a sheet ID and minimum permission level as arguments, then returns an object including a confirmation of whether the permission level is met
		# def check_sheet_permissions(self,
		# 		sheet_id,  # The ID of the sheet to check for permission requirements
		# 		permission_level=None  # The minimum permission level required. Can be a number from 1-5, or a String. If None, method will just return the sheet permission level
		# 	):
		# 	access_levels = self.access_levels
		# 	try:
		# 		sheet_id = int(sheet_id)
		# 	except:
		# 		return SmartoolsObject({'status': 'ERROR', 'access_met': False, 'Reason': 'Sheet ID is invalid'})

		# 	sheet = self.smart.Sheets.get_sheet(sheet_id, column_ids=[0], row_numbers=[0], level=1)

		# 	if hasattr(sheet, 'result') and hasattr(sheet.result, 'error_code'):
		# 		return SmartoolsObject({'status': 'ERROR', 'access_met': False, 'sheet': sheet})

		# 	if isinstance(permission_level, str):
		# 		permission_level = access_levels[permission_level]

		# 	if permission_level is None:
		# 		return SmartoolsObject({'status': 'ERROR', 'access_met': False, 'access_level': sheet.access_level})
		# 	else:
		# 		permission_met = permission_level <= access_levels[str(sheet.access_level)]
		# 		return SmartoolsObject({'status': 'SUCCESS', 'access_met': permission_met, 'access_level': sheet.access_level, 'sheet_response': sheet})

		def check_sheet_permissions(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Sheets.check_sheet_permissions instead.', DeprecationWarning)
			return self.smart.Sheets.check_sheet_permissions(*args, **kwargs)

		# # Takes a workspace ID and minimum permission level as arguments, then returns an object including a confirmation of whether the permission level is met
		# def check_workspace_permissions(self,
		# 		workspace_id,  # The ID of the workspace to check for permission requirements
		# 		permission_level=None  # The minimum permission level required. Can be a number from 1-5, or a String. If None, method will just return the workspace permisson level
		# 	):
		# 	access_levels = self.access_levels
		# 	try:
		# 		workspace_id = int(workspace_id)
		# 	except:
		# 		return SmartoolsObject({'status': 'ERROR', 'access_met': False, 'Reason': 'Workspace ID is invalid'})

		# 	space = self.smart.Workspaces.get_workspace(workspace_id)

		# 	if hasattr(space, 'result') and hasattr(space.result, 'error_code'):
		# 		return SmartoolsObject({'status': 'ERROR', 'access_met': False, 'Reason': 'This workspace could not be found', 'workspace_response': space})

		# 	if isinstance(permission_level, str):
		# 		permission_level = access_levels[permission_level]

		# 	if permission_level is None:
		# 		return space.access_level
		# 	else:
		# 		permission_met = permission_level <= access_levels[str(space.access_level)]
		# 		return SmartoolsObject({'status': 'SUCCESS', 'access_met': permission_met, 'access_level': space.access_level, 'workspace_response': space})

		def check_workspace_permissions(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Workspaces.check_workspace_permissions instead.', DeprecationWarning)
			return self.smart.Workspaces.check_workspace_permissions(*args, **kwargs)

		# # Takes a folder ID as an argument, and returns a boolean indicating whether it is a valid folder ID that the user has access to
		# def check_folder_access(self,
		# 		folder_id  # The ID of the folder to check for access.
		# 	):
		# 	folder = self.smart.Folders.get_folder(folder_id)
		# 	if hasattr(folder, 'result') and hasattr(folder.result, 'error_code'):
		# 		return False
		# 	return True

		def check_folder_access(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Folders.check_folder_access instead.', DeprecationWarning)
			return self.smart.Folders.check_folder_access(*args, **kwargs)


		# NOT YET DEPRECATED
		# Takes the url to a Smartsheet item then returns its ID. Please note this is a very slow operation as it iterates through all items in the account
		def get_container_from_url(self,
				container_url,  # The url to be matched to an existing Smartsheet item
				search_list=None  # (Optional) A list of items to search through. If provided, will speed up execution as the list will not need to be retrieved.
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
				response = self.smart.Sheets.list_sheets(include_all=True)
				items = response.data
			elif '/reports/' in container_url:
				response = self.smart.Reports.list_reports(include_all=True)
				items = response.data
			elif '/dashboards/' in container_url:
				response = self.smart.Sights.list_sights(include_all=True)
				items = response.data

			for item in items:
				if item.permalink.endswith(container_url):
					return item
			
			return None

		# def get_container_from_url(self, *args, **kwargs):
		# 	warnings.warn('Util methods have been deprecated. Please use .Home.get_container_from_url instead.', DeprecationWarning)
		# 	return self.smart.Home.get_container_from_url(*args, **kwargs)
