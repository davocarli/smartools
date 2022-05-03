# SmartoolsFolders Class
Smartools adds several new methods to the Folders class. All of these can be accessed through `smartsheet_client.Folders.<method_name>`

### `list_sheets_in_folder`
The `list_sheets_in_folder` method will return a list of all the sheets inside a folder and its subfolders. This list is a `ContainerList` object that can be indexed by sheet name.
```
# Example
sheets = smart.Folders.list_sheets_in_folder(folder_id)

target_sheet = sheets['My Sheet Name']

target_sheet.name  # "My Sheet Name"
```

**Args**
- folder_id
	- The ID of the folder you will be retrieving sheets from
- contains (Optional - default `None`)
	- A partial match to the names of the sheets that will be retrieved. For example, providing `contains='Project Plan'` will return a list of all the sheets that contain "Project Plan" in their sheet name.
- exact (Optional - default `False`)
	- If `contains` is provided and `exact = True`, only sheets with a perfect match to the provided name will be returned, rather than a partial match.
- **kwargs
	- You may provide any additional keyword arguments to be passed on when retrieving the folder.

### `list_containers_in_folder`
The `list_containers_in_folder` method functions similarly to the `list_sheets_in_folder` method, but will instead return a `smartsheet.models.FolderContent` object. This object has attributes separating the lists of `sheets`, `sights`, `reports`, `templates`, and `folders`.
```
# Example

# Retrieve all items in the folder that contain "Project A" in the name.
items = smart.Folders.list_containers_in_folder(folder_id, contains='Project A')

items.folders  # ["Project A"]
items.sheets   # ["Project Plan - Project A", "Project A Budget"]
items.reports  # ["Project A Summary Report"]
```

**Args**
- folder_id
	- The ID of the folder you will be retrieving items from
- contains (Optional - default `None`)
	- A partial match to the names of the items that will be retrieved. For example, providing `contains='Project Plan'` will return a list of all the items that contain "Project Plan" in their name.
- exact (Optional - default `False`)
	- If `contains` is provided and `exact = True`, only items with a perfect match to the provided name will be returned, rather than a partial match.
- **kwargs
	- You may provide any additional keyword arguments to be passed on when retrieving the folder.

### `get_access_level`
The `get_access_level` method makes the smallest request to get a folder possible (don't load subfolders), and returns the access level of the authenticated user to the folder. Because folders cannot be directly shared, and therefore don't have an actual sharing permission, this will return either "SHARED" (an alias of "VIEWER") or "UNSHARED".

**Args**
- folder_id
	- The folder to get your access level for.

### `create_sight_in_folder`
The `create_sight_in_folder` method will create a sight/dashboard at the root of the specified folder. Only the name of the sight/dashboard can be specified.

**Args**
- folder_id
	- The ID of the folder where the sight will be created.
- sight_obj
	- A `smartsheet.models.Sight` object that will be created. Only the "name" attribute will be used.

### `create_report_in_folder`
The `create_report_in_folder` method will create a report at the root of the specified folder. Only the name of the report can be specified.

**Args**
- folder_id
	- The ID of the folder where the report will be created.
- report_obj
	- A `smartsheet.models.Report` object that will be created. Only the "name" attribute will be used.
