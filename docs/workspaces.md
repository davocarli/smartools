# SmartoolsWorkspaces Class
Smartools adds several new methods to the Workspaces class. All of these can be accessed through `smartsheet_client.Workspaces.<method_name>`

### `list_sheets_in_workspace`
The `list_sheets_in_workspace` method will return a list of all the sheets inside a workspace, its folders, and subfolders. This list is a `ContainerList` object that can be indexed by sheet name.
```
# Example
sheets = smart.Workspaces.list_sheets_in_workspace(workspace_id)

target_sheet = sheets['My Sheet Name']

target_sheet.name  # "My Sheet Name"
```

**Args**
- workspace_id
	- The ID of the workspace you will be retrieving sheets from
- contains (Optional - default `None`)
	- A partial match to the names of the sheets that will be retrieved. For example, providing `contains='Project Plan'` will return a list of all the sheets that contain "Project Plan" in their sheet name.
- exact (Optional - default `False`)
	- If `contains` is provided and `exact = True`, only sheets with a perfect match to the provided name will be returned, rather than a partial match.
- **kwargs
	- You may provide any additional keyword arguments to be passed on when retrieving the workspace.

### `list_containers_in_workspace`
The `list_containers_in_workspace` method functions similarly to the `list_sheets_in_workspace` method, but will instead return a `smartsheet.models.WorkspaceContent` object. This object has attributes separating the lists of `sheets`, `sights`, `reports`, `templates`, and `folders`.
```
# Example

# Retrieve all items in the workspace that contain "Project A" in the name.
items = smart.Workspaces.list_containers_in_workspace(workspace_id, contains='Project A')

items.folders  # ["Project A"]
items.sheets   # ["Project Plan - Project A", "Project A Budget"]
items.reports  # ["Project A Summary Report"]
```

**Args**
- workspace_id
	- The ID of the workspace you will be retrieving items from
- contains (Optional - default `None`)
	- A partial match to the names of the items that will be retrieved. For example, providing `contains='Project Plan'` will return a list of all the items that contain "Project Plan" in their name.
- exact (Optional - default `False`)
	- If `contains` is provided and `exact = True`, only items with a perfect match to the provided name will be returned, rather than a partial match.
- **kwargs
	- You may provide any additional keyword arguments to be passed on when retrieving the workspace.

### `get_access_level`
The `get_access_level` method makes the smallest request to get a workspace possible (don't load subfolders), and returns the access level of the authenticated user to the workspace. If the workspace cannot be retrieved, it will return an 'UNSHARED' access level.

**Args**
- workspace_id
	- The workspace to get your access level for.

### `create_sight_in_workspace`
The `create_sight_in_workspace` method will create a sight/dashboard at the root of the specified workspace. Only the name of the sight/dashboard can be specified.

**Args**
- workspace_id
	- The ID of the workspace where the sight will be created.
- sight_obj
	- A `smartsheet.models.Sight` object that will be created. Only the "name" attribute will be used.

### `create_report_in_workspace`
The `create_report_in_workspace` method will create a report at the root of the specified workspace. Only the name of the report can be specified.

**Args**
- workspace_id
	- The ID of the workspace where the report will be created.
- report_obj
	- A `smartsheet.models.Report` object that will be created. Only the "name" attribute will be used.
