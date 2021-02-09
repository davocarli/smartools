import smartsheet
from .__smartools import SmartoolsObject

smart = smartsheet.Smartsheet("INIT")
smart.Workspaces

class SmartoolsWorkspaces(smartsheet.workspaces.Workspaces):
	def smartools(self):
		return 'smartools methods are available!'

	# Returns a list of all the sheets in a workspace. Optionally only includes sheets with specific Strings contained in the sheet name
	def list_sheets_in_workspace(self,
			workspace_id,  # The ID of the workspace whose sheets should be returned
			contains=None,  # (Optional) A String that should be contained in the sheet's sheet names to be included in the return
			exact=False,  # If set to True, will only return sheets with exactly the the name provided in the "contains" argument, rather than a partial match
			parent=None,  # Used for recursively providing information to this method. Should not be provided by users
		**kwargs):
		sheets = []
		if parent == None:
			parent = self.get_workspace(workspace_id, load_all=True, **kwargs)
		for sheet in parent.sheets:
			if (contains is None) \
			or (exact and contains == sheet.name) \
			or contains in sheet.name:
				sheets.append(sheet)
		for folder in parent.folders:
			sheets.extend(self.list_sheets_in_workspace(workspace_id=None, contains=contains, exact=exact, parent=folder))
		return sheets

	# Returns an object with lists of all containers in a workspace. Optionally only includes containers with specific Strings contained in the sheet name
	def list_containers_in_workspace(self,
				workspace_id,  # The ID of the workspace whose containers should be returned
				contains=None,  # (Optional) A String that should be contained in the container's name to be included in the return
				exact=False,  # If set to True, will only return sheets with exactly the name provided in the "contains" argument, rather than a partial match
				parent=None,  # Used for recursively providing information to this method. Should not be provided by users
		**kwargs):
		containers = {
			'sheets': [],
			'sights': [],
			'reports': []
		}
		if parent == None:
			parent = self.get_workspace(workspace_id, load_all=True, **kwargs)
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
			child = self.list_containers_in_workspace(workspace_id=None, contains=contains, exact=exact, parent=folder)
			containers['sheets'].extend(child.sheets)
			containers['sights'].extend(child.sights)
			containers['reports'].extend(child.reports)
		return SmartoolsObject(containers)

# Perform Monkey Patch
smartsheet.workspaces.Workspaces = SmartoolsWorkspaces
