import smartsheet
from .__smartools import SmartoolsObject

smart = smartsheet.Smartsheet("INIT")
smart.Folders

class SmartoolsFolders(smartsheet.folders.Folders):
	def smartools(self):
		return 'smartools method are available!'

	# Returns a list of all the sheets in a folder. Optionally only includes sheets with specific Strings contained in the sheet name
	def list_sheets_in_folder(self,
			folder_id,  # The ID of the folder whose sheets should be returned
			contains=None,  # (Optional) A String that should be contained in the sheet's name to be included in the returned list
			exact=False,  # If set to True, will only return sheets with exactly the name provided in the "contains" argument, rather than a partial match
		**kwargs):
		sheets = []
		parent = self.get_folder(folder_id, **kwargs)
		for sheet in parent.sheets:
			if (contains is None) \
			or (exact and contains == sheet.name) \
			or contains in sheet.name:
				sheets.append(sheet)
		for folder in parent.folders:
			sheets.extend(self.list_sheets_in_folder(folder_id=folder.id, contains=contains, exact=exact, **kwargs))
		return sheets

	# Returns an object with lists of all containers in a workspace. Optionally only includes containers with specific Strings contained in the sheet name
	def list_containers_in_folder(self,
			folder_id,  # The ID of the folder whose containers should be returned
			contains=None,  # (Optional) A String that should be contained in the container's name to be included in the returned object
			exact=False,  # If set to True, will only return containers with exactly the name provided in the "contains" argument, rather than a partial match
		**kwargs):
		containers = {
			'sheets': [],
			'sights': [],
			'reports': [],
			'folders': [],
		}
		parent = self.get_folder(folder_id, **kwargs)
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
			if (contains is None) \
			or (exact and contains == folder.name) \
			or contains in folder.name:
				containers['folders'].append(folder)
			child = self.list_containers_in_folder(folder_id=folder.id, contains=contains, exact=exact, **kwargs)
			containers['sheets'].extend(child.sheets)
			containers['sights'].extend(child.sights)
			containers['reports'].extend(child.reports)
		return SmartoolsObject(containers)

	# Takes a folder ID as an argument, and returns a boolean indicating whether it is a valid folder that the user has access to
	def check_folder_access(self,
			folder_id  # The ID of the folder to check for access.
		):
		folder = self.get_folder(folder_id)
		if hasattr(folder, 'result') and hasattr(folder.result, 'error_code'):
			return False
		return True

# Perform Monkey Patch
smartsheet.folders.Folders = SmartoolsFolders