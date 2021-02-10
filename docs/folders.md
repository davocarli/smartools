# Folders class
All of the methods described below can be accessed using the Folders class, per the examples found in the sdk documentation [here](https://smartsheet-platform.github.io/api-docs/?python#folders).

## List Sheets  | `smartsheet_client.Folders.list_sheets_in_folder`
This method allows you to list all of the sheets in a folder, or optionally provide a string to match to sheet names to only retrieve those sheets.
**Parameters:**
- `folder_id:` The ID of the folder from which sheets will be retrieved.
- `contains:` (Optional) A string to match to sheet names for them to be included.
- `exact:` (Optional) If given True, the string must exactly match the sheet name. Otherwise, the sheet name must only contain the match.

**Returns:**
A list containing sheet objects from the folder. They are not full sheets (no grid data), but rather the sheets as they would be returned when making a [get_folder](https://smartsheet-platform.github.io/api-docs/?python#get-folder) call.
**Example Usage**
This example will get all sheets in a folder that contain "Metrics" in the name, then print their sheetnames.
```
folder_id = 4236972823734148

sheets = smart.folders.list_sheets_in_folder(
	folder_id,
	'Metrics'
)

for sheet in sheets:
	print(sheet.name)
```

## List Containers | `smartsheet_client.Folders.list_containers_in_folder`
This method allows you to get all the contents of a folder, separated into lists by container type. You can optionally provide a string to match to container names in order to only retrieve those containers.
**Parameters:**
Parameters are identical to [list_sheets_in_folder](#list-sheets---smartsheet_client.folder.folder). See there.
**Returns:**
Returns a SmartoolsObject that contains the following attributes:
- `sheets:` The list of sheets returned.
- `sights:` The list of dashboards returned.
- `reports:` The list of reports returned.
**Example Usage:**
This example will retrieve all of the containers in the folder that contain 'London' in the name, then print out their names.
```
folder_id = 4236972823734148

containers = smart.Folders.list_containers_in_folder(
	folder_id,
	'London'
)

for sheet in containers.sheets:
	print(sheet.name)
for sight in containers.sights:
	print(sight.name)
for report in containers.reports:
	print(report.name)
```

## Check Folder Access | `smartsheet_client.Folders.check_folder_access`
This method allows you to provide a folder ID and will return a boolean indicating whether you have access to that folder.
**Parameters:**
- `folder_id:` The ID of the folder to check access for.

**Returns:**
A boolean indicating whether you have access to the folder. True if you have access, False if not.
**Example Usage:**
```
folder_id = 204336744687492

can_access = smartsheet_client.Folders.check_folder_access(folder_id)

if can_access:
	You have access to this folder!
else:
	You can't access this folder!
```