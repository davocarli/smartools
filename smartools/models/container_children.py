class SmartoolsContainerChildren:
    """Parses the paginated response from /workspaces/{id}/children
    or /folders/{id}/children.

    Children are returned as a flat list with a "resourceType" field
    distinguishing sheets, folders, reports, sights, and templates.

    Raw dicts are stored (not pre-created model objects) so that TypedList
    on the receiving Workspace/Folder can instantiate using the monkey-patched
    model class (e.g. SmartoolsSheet) rather than the original SDK class.
    """

    def __init__(self, props, dynamic_type=None, base_obj=None):
        self._base = base_obj
        self.next_page_token = props.get("nextPageToken")

        self.sheets = []
        self.folders = []
        self.reports = []
        self.sights = []
        self.templates = []

        for item in props.get("data", []):
            resource_type = item.get("resourceType")
            if resource_type == "sheet":
                self.sheets.append(item)
            elif resource_type == "folder":
                self.folders.append(item)
            elif resource_type == "report":
                self.reports.append(item)
            elif resource_type in ("sight", "dashboard"):
                self.sights.append(item)
            elif resource_type == "template":
                self.templates.append(item)
