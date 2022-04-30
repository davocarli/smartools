from smartsheet.models import Sheet, Report, Sight, Folder, Template

from smartools.types import ContainerList

class WorkspaceContent:

    def __init__(self):
        self.sheets = ContainerList(Sheet)
        self.reports = ContainerList(Report)
        self.sights = ContainerList(Sight)
        self.folders = ContainerList(Folder)
        self.templates = ContainerList(Template)

    @property
    def dashboards(self):
        return self.sights
    
    @dashboards.setter
    def dashboards(self, val):
        self.sights = val

    @property
    def containers(self):
        result = []
        result.extend(self.sheets)
        result.extend(self.reports)
        result.extend(self.sights)
        result.extend(self.templates)
        result.extend(self.folders)
        return result

class FolderContent:

    def __init__(self):
        self.sheets = ContainerList(Sheet)
        self.reports = ContainerList(Report)
        self.sights = ContainerList(Sight)
        self.folders = ContainerList(Folder)
        self.templates = ContainerList(Template)

    @property
    def dashboards(self):
        return self.sights
    
    @dashboards.setter
    def dashboards(self, val):
        self.sights = val

    @property
    def containers(self):
        result = []
        result.extend(self.sheets)
        result.extend(self.reports)
        result.extend(self.sights)
        result.extend(self.templates)
        result.extend(self.folders)
        return result
