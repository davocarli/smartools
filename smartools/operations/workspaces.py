from smartsheet.workspaces import Workspaces
from smartsheet.models import ContainerDestination
from smartsheet.models import Sheet

from smartools.types import ContainerList
from smartools.types.enumerated_value import SmartoolsEnumeratedValue
from smartools.models import WorkspaceContent
from smartools.models.enums import SmartoolsAccessLevel

class SmartoolsWorkspaces(Workspaces):

	def list_sheets_in_workspace(
		self,
		workspace_id,
		contains = None,
		exact = False,
		parent = None,
		**kwargs
		):
		"""Return all sheets inside the specified workspace in an easily iterable format.

		Args:
			workspace_id (int): Workspace ID.
			contains (str - optional): String to match sheets by name.
			exact (bool - optional): Whether "contains" should be an exact match.
			parent (folder - optional): Folder to search through. Used to call this method recursively.
		"""
		sheets = ContainerList(Sheet)
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

	def list_containers_in_workspace(
		self,
		workspace_id,
		contains=None,
		exact=False,
		parent=None,
		**kwargs,
		):
		"""Return all containers inside the specified workspace in an easily iterable format.

		Args:
			workspace_id (int): Workspace ID.
			contains (str - optional): String to match items by name.
			exact (bool - optional): Whether "contains" should be an exact match.
			parent (folder - optional): Folder to search through. Used to call this method recursively.
		"""
		containers = WorkspaceContent()
		if parent == None:
			parent = self.get_workspace(workspace_id, load_all=True, **kwargs)
		for sheet in parent.sheets:
			if (contains is None) \
			or (exact and contains == sheet.name) \
			or contains in sheet.name:
				containers.sheets.append(sheet)
		for sight in parent.sights:
			if (contains is None) \
			or (exact and contains == sight.name) \
			or contains in sight.name:
				containers.sights.append(sight)
		for report in parent.reports:
			if (contains is None) \
			or (exact and contains == report.name) \
			or contains in report.name:
				containers.reports.append(report)
		for template in parent.templates:
			if (contains is None) \
			or (exact and contains == template.name) \
			or contains in template.name:
				containers.templates.append(template)
		for folder in parent.folders:
			if (contains is None) \
			or (exact and contains == folder.name) \
			or contains in folder.name:
				containers.folders.append(folder)
			child = self.list_containers_in_workspace(workspace_id=None, contains=contains, exact=exact, parent=folder)
			containers.sheets.extend(child.sheets)
			containers.sights.extend(child.sights)
			containers.reports.extend(child.reports)
			containers.templates.extend(child.templates)
			containers.folders.extend(child.folders)
		return containers

	def get_access_level(
		self,
		workspace_id,
		):
		"""Return the access level of the authenticated user for the specified workspace.

		Args:
			workspace_id (int): Workspace ID
		"""
		space = self.get_workspace(workspace_id)
		if hasattr(space, 'result') and hasattr(space.result, 'error_code'):
			level = SmartoolsEnumeratedValue(SmartoolsAccessLevel)
			level.set('UNSHARED')
			return level
		return space.access_level

	def create_sight_in_workspace(self, workspace_id, sight_obj):
		"""Create a Sight from scratch in the specified Workspace.

		Args:
			workspace_id (int): Workspace ID.
			sight_obj (Sight): Sight object.

		Returns: Result
		"""
		created_sight = self._base.Home.create_sight(sight_obj)
		response = self._base.Sights.move_sight(
				created_sight.result.id,
				ContainerDestination({
					'destination_type': 'workspace',
					'destination_id': workspace_id,
				})
		)

		return response

	def create_report_in_workspace(self, workspace_id, report_obj):
		"""Create a Report from scratch in the specified Workspace.
		
		Args:
			workspace_id (int): Workspace ID.
			report_obj (Report): Report object.
			
		Returns: Result
		"""
		created_report = self._base.Home.create_report(report_obj)
		response = self._base.Reports.move_report(
				created_report.result.id,
				ContainerDestination({
					'destination_type': 'workspace',
					'destination_id': workspace_id,
				})
		)

		return response
