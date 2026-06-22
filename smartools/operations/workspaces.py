from types import SimpleNamespace

from smartsheet import fresh_operation
from smartsheet.workspaces import Workspaces
from smartsheet.models import ContainerDestination, Folder
from smartsheet.models import Sheet

from smartools.types import ContainerList
from smartools.types.enumerated_value import SmartoolsEnumeratedValue
from smartools.models import WorkspaceContent
from smartools.models.enums import SmartoolsAccessLevel

def _get_container_children(base, path):
	"""Fetch all children from a /children endpoint, handling token-based pagination."""
	all_sheets, all_folders, all_reports, all_sights, all_templates = [], [], [], [], []
	last_key = None
	while True:
		_op = fresh_operation("get_children")
		_op["method"] = "GET"
		_op["path"] = path
		if last_key:
			_op["query_params"]["lastKey"] = last_key
		prepped = base.prepare_request(_op)
		page = base.request(prepped, ["ContainerChildren", None], _op)
		all_sheets.extend(page.sheets)
		all_folders.extend(page.folders)
		all_reports.extend(page.reports)
		all_sights.extend(page.sights)
		all_templates.extend(page.templates)
		if not page.next_page_token:
			break
		last_key = page.next_page_token

	from smartools.models.container_children import SmartoolsContainerChildren
	result = object.__new__(SmartoolsContainerChildren)
	result.sheets, result.folders, result.reports = all_sheets, all_folders, all_reports
	result.sights, result.templates = all_sights, all_templates
	result.next_page_token = None
	return result


def _populate_folders(base, folders):
	"""Recursively fetch and populate contents for each folder in the list."""
	for folder in (folders or []):
		folder_data = base.Folders.get_folder(folder.id)
		folder.sheets = folder_data.sheets
		folder.folders = folder_data.folders
		folder.reports = folder_data.reports
		folder.sights = folder_data.sights
		folder.templates = folder_data.templates
		_populate_folders(base, folder.folders)


class SmartoolsWorkspaces(Workspaces):

	def get_workspace(self, workspace_id, load_all=False, include=None):
		"""Get the specified Workspace and its contents.

		Replaces the deprecated GET /workspaces/{id} and loadAll=true param.
		Uses the new /metadata + /children endpoints with token-based pagination.

		Args:
			workspace_id (int): Workspace ID.
			load_all (bool): Load all contents including nested folders.
			include (list[str]): Optional elements to include (ownerInfo, sheetVersion, source).

		Returns:
			Workspace
		"""
		_op = fresh_operation("get_workspace_metadata")
		_op["method"] = "GET"
		_op["path"] = "/workspaces/" + str(workspace_id) + "/metadata"
		_op["query_params"]["include"] = include
		prepped = self._base.prepare_request(_op)
		workspace = self._base.request(prepped, "Workspace", _op)

		children = _get_container_children(
			self._base, "/workspaces/" + str(workspace_id) + "/children"
		)
		workspace.sheets = children.sheets
		workspace.folders = children.folders
		workspace.reports = children.reports
		workspace.sights = children.sights
		workspace.templates = children.templates

		if load_all:
			_populate_folders(self._base, workspace.folders)

		return workspace

	def list_workspaces(self, page_size=None, page=None, include_all=None):
		"""List workspaces the authenticated user may access.

		Replaces the deprecated includeAll parameter by iterating pages
		automatically when include_all=True.

		Returns:
			IndexResult (single page) or SimpleNamespace with .data (all pages).
		"""
		if not include_all:
			return super().list_workspaces(page_size=page_size, page=page, include_all=None)

		effective_page_size = page_size or 100
		all_workspaces = []
		current_page = 1
		while True:
			result = super().list_workspaces(
				page_size=effective_page_size, page=current_page, include_all=None
			)
			all_workspaces.extend(result.data)
			if current_page >= result.total_pages:
				break
			current_page += 1

		return SimpleNamespace(data=all_workspaces)

	def list_folders(self, workspace_id, page_size=None, page=None, include_all=None):
		"""List top-level folders in a workspace.

		Replaces deprecated GET /workspaces/{id}/folders and the deprecated
		includeAll parameter. Always returns all folders via token-based pagination.

		Returns:
			SimpleNamespace with .data containing a list of Folder objects.
		"""
		children = _get_container_children(
			self._base, "/workspaces/" + str(workspace_id) + "/children"
		)
		folders = [Folder(item, self._base) for item in children.folders]
		return SimpleNamespace(data=folders)

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

	def list_shares(self, workspace_id, page_size=None, page=None, include_all=None):
		"""List all shares for a workspace via the unified sharing API.

		Replaces the deprecated Workspaces.list_shares endpoint.

		Returns:
			SmartoolsAssetSharesPaginatedResult: Result with .items and .data.
		"""
		return self._base.Sharing.list_asset_shares(
			asset_type="workspace",
			asset_id=workspace_id,
			include_all=bool(include_all),
		)

	def share_workspace(self, workspace_id, share_obj, send_email=False):
		"""Share a workspace via the unified sharing API.

		Replaces the deprecated Workspaces.share_workspace endpoint.
		Accepts a single Share object (old API signature) or a list.

		Returns:
			Result: Result with .result[0] containing the created Share.
		"""
		return self._base.Sharing.share_asset(
			share_obj=share_obj,
			asset_type="workspace",
			asset_id=workspace_id,
			send_email=send_email,
		)

	def update_share(self, workspace_id, share_id, share_obj):
		"""Update a workspace share via the unified sharing API.

		Replaces the deprecated Workspaces.update_share endpoint.
		"""
		return self._base.Sharing.update_asset_share(
			share_obj=share_obj,
			asset_type="workspace",
			asset_id=workspace_id,
			share_id=share_id,
		)

	def delete_share(self, workspace_id, share_id):
		"""Delete a workspace share via the unified sharing API.

		Replaces the deprecated Workspaces.delete_share endpoint.
		"""
		return self._base.Sharing.delete_asset_share(
			asset_type="workspace",
			asset_id=workspace_id,
			share_id=share_id,
		)

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
