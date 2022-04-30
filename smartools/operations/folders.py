from smartsheet.folders import Folders
from smartsheet.models import ContainerDestination

from smartools.types import ContainerList
from smartools.types.enumerated_value import SmartoolsEnumeratedValue
from smartools.models import FolderContent
from smartools.models.enums import SmartoolsAccessLevel

from smartsheet.models import Sheet

class SmartoolsFolders(Folders):

	def list_sheets_in_folder(
			self,
			folder_id,
			contains = None,
			exact = False,
			**kwargs
			):
			"""Return all sheets inside the specified folder in an easily iterable format.

			Args:
				folder_id (int): Folder ID.
				contains (str - optional): String to match sheets by name.
				exact (bool - optional): Whether "contains" should be an exact match.
			"""
			sheets = ContainerList(Sheet)
			parent = self.get_folder(folder_id, **kwargs)
			for sheet in parent.sheets:
				if (contains is None) \
				or (exact and contains == sheet.name) \
				or contains in sheet.name:
					sheets.append(sheet)
			for folder in parent.folders:
				sheets.extend(self.list_sheets_in_folder(folder_id=folder.id, contains=contains, exact=exact))
			return sheets

	def list_containers_in_folder(
		self,
		folder_id,
		contains=None,
		exact=False,
		**kwargs,
		):
		"""Return all containers inside the specified folder in an easily iterable format.

		Args:
			folder_id (int): Folder ID.
			contains (str - optional): String to match items by name.
			exact (bool - optional): Whether "contains" should be an exact match.
			parent (folder - optional): Folder to search through. Used to call this method recursively.
		"""
		containers = FolderContent()
		parent = self.get_folder(folder_id, **kwargs)
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
			child = self.list_containers_in_folder(folder_id=folder.id, contains=contains, exact=exact)
			containers.sheets.extend(child.sheets)
			containers.sights.extend(child.sights)
			containers.reports.extend(child.reports)
			containers.templates.extend(child.templates)
			containers.folders.extend(child.folders)
		return containers

	def get_access_level(
		self,
		folder_id
		):
		folder = self.get_folder(folder_id)
		level = SmartoolsEnumeratedValue(SmartoolsAccessLevel)
		if hasattr(folder, 'result') and hasattr(folder.result, 'error_code'):
			level.set('UNSHARED')
		else:
			level.set('SHARED')
		return level

	def create_sight_in_folder(self, folder_id, sight_obj):
		"""Create a Sight from scratch in the specified Folder.

		Args:
			folder_id (int): Folder ID
			sight_obj (Sight): Sight object.

		Returns: Result
		"""
		created_sight = self._base.Home.create_sight(sight_obj)
		response = self._base.Sights.move_sight(
				created_sight.result.id,
				ContainerDestination({
					'destination_type': 'folder',
					'destination_id': folder_id,
				})
		)

		return response

	def create_report_in_folder(self, folder_id, report_obj):
		"""Create a Report from scratch in the specified Folder.
		
		Args:
			folder_id (int): Folder ID
			report_obj (Report): Report object.
			
		Returns: Result
		"""
		created_report = self._base.Home.create_report(report_obj)
		response = self._base.Reports.move_report(
				created_report.result.id,
				ContainerDestination({
					'destination_type': 'folder',
					'destination_id': folder_id,
				})
		)

		return response
