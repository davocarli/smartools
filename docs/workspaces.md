##### [Back to README](/README.md)
# Workspaces class
All of the methods described below can be accessed using the Workspaces class, per the examples found in the sdk documentation [here](https://smartsheet-platform.github.io/api-docs/?python#workspaces).

## List Sheets  | `smartsheet_client.Workspaces.list_sheets_in_workspace`
This method allows you to list all of the sheets in a workspace, or optionally provide a string to match to sheet names to only retrieve those sheets.
**Parameters:**
- `workspace_id:` The ID of the workspace from which sheets will be retrieved.
- `contains:` (Optional) A string to match to sheet names for them to be included.
- `exact:` (Optional) If given True, the string must exactly match the sheet name. Otherwise, the sheet name must only contain the match.

**Returns:**
A list containing sheet objects from the workspace. They are not full sheets (no grid data), but rather the sheets as they would be returned when making a [get_workspace](https://smartsheet-platform.github.io/api-docs/?python#get-workspace) call.
**Example Usage**
This example will get all sheets in a workspace that contain "Metrics" in the name, then print their sheetnames.
```
workspace_id = 4236972823734148

sheets = smart.Workspaces.list_sheets_in_workspace(
	workspace_id,
	'Metrics'
)

for sheet in sheets:
	print(sheet.name)
```

## List Containers | `smartsheet_client.Workspaces.list_containers_in_workspace`
This method allows you to get all the contents of a workspace, separated into lists by container type. You can optionally provide a string to match to container names in order to only retrieve those containers.
**Parameters:**
Parameters are identical to [list_sheets_in_workspace](#list-sheets---smartsheet_clientworkspaceslist_sheets_in_workspace). See there.
**Returns:**
Returns a SmartoolsObject that contains the following attributes:
- `sheets:` The list of sheets returned.
- `sights:` The list of dashboards returned.
- `reports:` The list of reports returned.
**Example Usage:**
This example will retrieve all of the containers in the workspace that contain 'Project Alpha' in the name, then print out their names.
```
workspace_id = 4236972823734148

containers = smart.Workspaces.list_containers_in_workspace(
	workspace_id,
	'Project Alpha'
)

for sheet in containers.sheets:
	print(sheet.name)
for sight in containers.sights:
	print(sight.name)
for report in containers.reports:
	print(report.name)
```

## Check Workspace Permissions | `smartsheet_client.Workspaces.check_workspace_permissions`
A method that performs the most efficient API call possible and check whether you have certain permissions on a sheet.
**Parameters:**
`workspace_id`: The ID of the sheet whose permissions are being checked.
`permission_level`: The minimum permission level you are checking for. Can be an integer (VIEWER=1, OWNER=5) or a string ("VIEWER", "EDITOR", "EDITOR_SHARE", "ADMIN", "OWNER").
**Returns:**
An object with the following attributes:
- `status:` A string indicating success of the operation.
- `access_met:` A boolean indicating if the specified permission level was met.
- `access_level:` The sheet's actual/specific permission level.
- `sheet_response:` A sheet object that was retrieved as part of the operation. This object contains very minimal information (no rows, no columns).

**Example Usage:**
This example will check if the user has at least "Admin" permissions on a workspace.
```
workspace_id = 8008241872430980

permission_check = smart.Workspaces.check_workspace_permissions(workspace_id, 4)

if permission_check.access_met:
	print('You have Admin access')
else:
	print('You don't have Admin access')
```