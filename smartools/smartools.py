from smartsheet import *
import smartsheet
import os
import time
import warnings

"""
	In an earlier version of this module, all of the added methods were in this Util class, instead
	of being monkey patched into their more logical classes (Sheets, Workspaces, etc.). To ensure
	compatibility with prior-written software, this Util class remains, but calling methods here will
	issue a deprecation warning.
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
			self.include_all = 'shares,workspaceShares,parentObjectFavorite,data,ownerInfo,columnType,proofs,cellLinks,source,groups,rules,format,objectValue,children,profileImage,discussions,lastLogin,filterDefinitions,favorite,scope,writerInfo,attachments,filters,comments,ruleRecipients,permalinks,ganttConfig,sourceSheets,crossSheetReferences,forms,sheetVersion'


		def list_sheets_in_workspace(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Workspaces.list_sheets_in_workspace instead.', DeprecationWarning)
			return self.smart.Workspaces.list_sheets_in_workspace(*args, **kwargs)


		def list_containers_in_workspace(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Workspaces.list_containers_in_workspace instead.', DeprecationWarning)
			return self.smart.Workspaces.list_containers_in_workspace(*args, **kwargs)


		def list_sheets_in_folder(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Folders.list_sheets_in_folder instead.', DeprecationWarning)
			return self.smart.Folders.list_sheets_in_folder(*args, **kwargs)


		def list_containers_in_folder(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Folders.list_containers_in_folder instead.', DeprecationWarning)
			return self.smart.Folders.list_containers_in_folder(*args, **kwargs)


		def bulk_add_rows(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Sheets.bulk_add_rows instead.', DeprecationWarning)
			return self.smart.Sheets.bulk_add_rows(*args, **kwargs)


		def bulk_update_rows(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Sheets.bulk_update_rows instead.', DeprecationWarning)
			return self.smart.Sheets.bulk_update_rows(*args, **kwargs)


		def get_sheet_as_pandas_dataframe(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Sheets.get_sheet_as_pandas_dataframe instead.', DeprecationWarning)
			return self.smart.Sheets.get_sheet_as_pandas_dataframe(*args, **kwargs)


		def check_sheet_permissions(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Sheets.check_sheet_permissions instead.', DeprecationWarning)
			return self.smart.Sheets.check_sheet_permissions(*args, **kwargs)


		def check_workspace_permissions(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Workspaces.check_workspace_permissions instead.', DeprecationWarning)
			return self.smart.Workspaces.check_workspace_permissions(*args, **kwargs)


		def check_folder_access(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Folders.check_folder_access instead.', DeprecationWarning)
			return self.smart.Folders.check_folder_access(*args, **kwargs)


		def get_container_from_url(self, *args, **kwargs):
			warnings.warn('Util methods have been deprecated. Please use .Home.get_container_from_url instead.', DeprecationWarning)
			return self.smart.Home.get_container_from_url(*args, **kwargs)
