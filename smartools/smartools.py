from smartsheet import *
import smartsheet
import os
import time

class Smartsheet(smartsheet.Smartsheet):

	def __init__(self, token=None):
		self.Util = self.SmartsheetUtilities(self)
		super().__init__(token)


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


		def list_sheets_in_workspace(self, parentid, contains=None, exact=False, parent=None):
			sheets = []
			if parent == None:
				parent = self.smart.Workspaces.get_workspace(parentid, load_all=True)
			for sheet in parent.sheets:
				if (contains is None) \
				or (exact and contains == sheet.name) \
				or contains in sheet.name:
					sheets.append(sheet)
			for folder in parent.folders:
				sheets.extend(self.list_sheets_in_workspace(parentid=None, contains=contains, exact=exact, parent=folder))
			return sheets


		def list_containers_in_workspace(self, parentid, contains=None, exact=False, parent=None):
			containers={
				'sheets': [],
				'sights': [],
				'reports': []
			}
			if parent == None:
				parent = self.smart.Workspaces.get_workspace(parentid, load_all=True)
			for sheet in parent.sheets:
				if (contains is None) \
				or (exact and contains == sheet.name) \
				or contains in sheet.name:
					containers['sheets'].append(sheet.name)
			for sight in parent.sights:
				if (contains is None) \
				or (exact and contains == sight.name) \
				or contains in sight.name:
					containers['sights'].append(sight.name)
			for report in parent.reports:
				if (contains is None) \
				or (exact and contains == report.name) \
				or contains in report.name:
					containers['reports'].append(report.name)
			for folder in parent.folders:
				child = self.list_containers_in_workspace(parentid=None, contains=contains, exact=exact, parent=folder)
				containers['sheets'].extend(child.sheets)
				containers['sights'].extend(child.sights)
				containers['reports'].extend(child.reports)
			return DictToObject(containers)


		def list_sheets_in_folder(self, parentid, contains=None, exact=False):
			sheets = []
			parent = self.smart.Folders.get_folder(parentid)
			for sheet in parent.sheets:
				if (contains is None) \
				or (exact and contains == sheet.name) \
				or contains in sheet.name:
					sheets.append(sheet)
			for folder in parent.folders:
				sheets.extend(self.list_sheets_in_folder(parentid=folder.id, contains=contains, exact=exact))
			return sheets


		def list_containers_in_folder(self, parentid, contains=None, exact=False):
			containers = {
				'sheets': [],
				'sights': [],
				'reports': []
			}
			parent = self.smart.Folders.get_folder(parentid)
			for sheet in parent.sheets:
				if (contains is None) \
				or (exact and contains == sheet.name) \
				or contains in sheet.name:
					containers['sheets'].append(sheet)
			for sight in parent.sights:
				if (contains is None) \
				or (exact and contains == sight.name) \
				or contains in sight.name:
					containers['sights'].append(sight)
			for report in parent.reports:
				if (contains is None) \
				or (exact and contains == report.name) \
				or contains in report.name:
					containers['reports'].append(report)
			for folder in parent.folders:
				child = self.list_containers_in_folder(parentid=folder.id, contains=contains, exact=exact)
				containers['sheets'].extend(child.sheets)
				containers['sights'].extend(child.sights)
				containers['reports'].extend(child.reports)
			return DictToObject(containers)


		def bulk_add_rows(self, sheetid, rows, n=500, retries=5):
			result = {
				'responses': [],
				'rows': [],
				'data': [],
				'status': ''
			}

			current_retries = retries

			if n > 500:
				n = 500

			while len(rows) > 0:
				response = self.smart.Sheets.add_rows(sheetid, rows[:n])
				if hasattr(response.result, 'error_code'):
					current_retries -= 1
					if response.result.error_code == 4002:
						n = n//2
					elif response.result.error_code in [4003, 4004]:
						time.sleep(60)
					else:
						if current_retries <= 0:
							result['responses'].append(response)
							result['status'] = 'ERROR'
							result['error_message'] = 'See last response for detailed error.'
							return DictToObject(result)
				else:
					result['data'].extend(response.data)
					rows = rows[n:]
					current_retries = retries
					result['responses'].append(response)
					result['rows'].extend(response.result)
			result['status'] = 'SUCCESS'
			return DictToObject(result)


		def bulk_update_rows(self, sheetid, rows, n=500, retries=5):
			result = {
				'responses': [],
				'rows': [],
				'data': [],
				'status': ''
			}

			current_retries = retries

			if n > 500:
				n = 500

			while len(rows) > 0:
				response = self.smart.Sheets.update_rows(sheetid, rows[:n])
				if hasattr(response.result, 'error_code'):
					current_retries -= 1
					if response.result.error_code == 4002:
						n = n//2
					elif response.result.error_code in [4003, 4004]:
						time.sleep(60)
					else:
						if current_retries <= 0:
							result['responses'].append(response)
							result['status'] = 'ERROR'
							result['error_message'] = 'See last response for detailed error.'
							return DictToObject(result)
				else:
					result['data'].extend(response.data)
					rows = rows[n:]
					current_retries = retries
					result['responses'].append(response)
					result['rows'].extend(response.result)
				result['status'] = 'SUCCESS'
				return DictToObject(result)


		def get_sheet_as_pandas_dataframe(self, sheetid, label_column=None):
			try:
				import pandas as pd
			except ImportError:
				raise RequirementError({'message': 'Import Error: This method requires the pandas module', 'recommended_action': 'Install pandas by using "pip install pandas"'})
			if isinstance(sheetid, int):
				sheet = self.smart.Sheets.get_sheet(sheetid)

				pd_row_data = []
				pd_row_labels = []
				pd_columns = []

				for column in sheet.columns:
					if (label_column is None and column.primary == True):
						label_column = column.id
					elif column.id == label_column or column.title == label_column:
						label_column = column.id
					else:
						pd_columns.append(column.title)

				for row in sheet.rows:
					row_list = []
					for cell in row.cells:
						if cell.column_id == label_column:
							pd_row_labels.append(cell.value)
						else:
							row_list.append(cell.value)
					pd_row_data.append(row_list)

				return pd.DataFrame(pd_row_data, columns=pd_columns, index=pd_row_labels)


		def check_sheet_permissions(self, sheetid, permission_level=None):
			access_levels = self.access_levels
			try:
				sheetid = int(sheetid)
			except:
				return DictToObject({'status': 'ERROR', 'access_met': False, 'Reason': 'Sheet ID is invalid'})

			sheet = self.smart.Sheets.get_sheet(sheetid, column_ids=[0], row_numbers=[0], level=1)

			if hasattr(sheet, 'result') and hasattr(sheet.result, 'error_code'):
				return DictToObject({'status': 'ERROR', 'access_met': False, 'sheet': sheet})

			if isinstance(permission_level, str):
				permission_level = access_levels[permission_level]

			if permission_level is None:
				return DictToObject({'status': 'ERROR', 'access_met': False, 'access_level': sheet.access_level})
			else:
				permission_met = permission_level <= access_levels[str(sheet.access_level)]
				return DictToObject({'status': 'SUCCESS', 'access_met': permission_met, 'access_level': sheet.access_level, 'sheet_response': sheet})


		def check_workspace_permissions(self, spaceid, permission_level=None):
			access_levels = self.access_levels
			try:
				spaceid = int(spaceid)
			except:
				return DictToObject({'status': 'ERROR', 'access_met': False, 'Reason': 'Workspace ID is invalid'})

			space = self.smart.Workspaces.get_workspace(spaceid)

			if hasattr(space, 'result') and hasattr(space.result, 'error_code'):
				return DictToObject({'status': 'ERROR', 'access_met': False, 'Reason': 'This workspace could not be found', 'workspace_response': space})

			if isinstance(permission_level, str):
				permission_level = access_levels[permission_level]

			if permission_level is None:
				return space.access_level
			else:
				permission_met = permission_level <= access_levels[str(space.access_level)]
				return DictToObject({'status': 'SUCCESS', 'access_met': permission_met, 'access_level': space.access_level, 'workspace_response': space})


		def check_folder_access(self, folderid):
			folder = self.smart.Folders.get_folder(folderid)
			if hasattr(folder, 'result') and hasattr(folder.result, 'error_code'):
				return False
			return True

class DictToObject(object):
	def __init__(self, *initial_data, **kwargs):
		for dictionary in initial_data:
			for key in dictionary:
				setattr(self, key, dictionary[key])
		for key in kwargs:
			setattr(self, key, kwargs[key])

class RequirementError(Exception):
	pass