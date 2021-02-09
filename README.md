# Smartools

smartools is a wrapper that extends the official [smartsheet-python-sdk]. It monkey patches several classes to add new functionality, and adds a new "SmartsheetUtilities" subclass (accessible at smartsheet_client.Util) that contains several methods that perform more complex but common operations. The decision was made to monkey patch the smartsheet sdk, rather than fork it, because:
- The official sdk does what it is designed to do very well - it allows you to perform calls to the Smartsheet API. Many of my additions instead perform some amount of processing of the data, or multiple API calls, so they are outside the scope of the SDK.
- By subclassing the existing package, this package can be updated independently of the original sdk, and is not dependent on a specific version.

## Installation
This package has not (yet) been added to PyPI, but can be installed using:
```
pip install -e git+https://github.com/davocarli/smartools.git#egg=smartools
```
Once installed it can be imported with `import smartools` or for a more authentic replacement to the official sdk `import smartools as smartsheet`

### Monkey-patched classes
#### smartsheet.types.TypedList
This method was monkey-patched to allow for getting of items using a string, provided that an index_reference attribute has been set on the TypedList. This is used in the other classes below.

#### smartsheet_client.Sheets
- `get_sheet()`
    - The get_sheet method has been modified to incorporate the monkey-patched TypedList. Columns and cells can now be obtained using column names. For example:
        ```
        sheet = smartsheet_client.Sheets.get_sheet(sheetid)
        
        start_column = sheet.columns['Start Date']  # Get column named "Start Date"
        new_name = sheet.rows[0].cells['Start Date']  # Get value of first row for column named "Start Date"
        ```
    - **Performance:** A stress test loading a maximum-size sheet (20,000 rows x 25 columns = 500,000 cells) 100 times with and without the new method revealed that a get_sheet operation only takes on average ~0.12 seconds longer with these changes, and network performance likely has a greater effect on total time. However, if you want to preserve maximum performance you can pass list_dict=False to the method to skip these operations. For example 
    
    `smartsheet_client.Sheets.get_sheet(sheetid, include='ColumnType', list_dict=False)`

### Util class methods
All of these methods can be accessed through the "Util" class. For example, `smartsheet_client.Util.list_sheets_in_workspace(6058237884688260, "Metrics")`
- `list_sheets_in_workspace(parentid, contains=None, exact=False)`
    - Lists all the sheets inside of the workspace. Arguments are:
        - `parentid`: The Workspace ID that you want to retrieve from.
        - `contains` (Optional): Only return sheets that contain this string in their sheet name.
        - `exact` (Optional): If contains is specified, return sheets that are *exactly* the string provided for contains.
    - Returns a list of the obtained sheets.
- `list_containers_in_workspace(parentid, contains=None, exact=False)`
    - Usage is the same as `list_sheets_in_workspace`, but returns *all* containers matching criteria, not just sheets.
- `list_sheets_in_folder(parentid, contains=None, exact=False)`
    - Usage is the same as `list_sheets_in_workspace`, but checks a specific folder instead of entire workspace. `parentid` should now be the folder ID.
- `list_containers_in_folder(parentid, contains=None, exact=False)`
    - Usage is the same as `list_sheets_in_folder`, but returns *all* containers matching criteria, not just sheets.
- `bulk_add_rows(sheetid, rows, n=500, retries=5)`
    - A method that allows you to pass a list of more than 500 rows to be added. It will then add the rows in batches of n (500 by default), and if it encounters a timeout error will automatically retry in smaller batches. This allows for some easy implementation of common error handling. Arguments are:
        - `sheetid`: The sheet to add the rows to.
        - `rows`: A list of smartsheet Row() objects to be added.
        - `n`: The batch size that rows should be added in (default 500)
        - `retries`: The number of consecutive failures before the operation is aborted (default 5).
    - Returns an object with the following attributes: "responses" (a list of the individual responses received when adding rows), "rows" (a list of rows, similar to the usual response received when adding rows using the sdk), "data" (a list containing all of the data received in responses), and "status" (a string indicating success of the operation).
- `bulk_update_rows(sheetid, rows, n=500, retries=5)`
    - Usage is the same as `bulk_add_rows`, but updates existing rows instead of adding them.
- `get_sheet_as_pandas_dataframe(sheetid, label_column=None)`
    - A method that will get a sheet and return it as a pandas dataframe of its values. Arguments are:
        - `sheetid`: The sheet to get.
        - `label_column`: The column to be used for row labels in the pandas dataframe. If `None`, the Primary Column of the sheet will be used.
    - Note: Requires that pandas be installed, which is *not* a requirement of this package. If unable to import, the method will raise a `RequirementError` exception.
    - Returns a pandas DataFrame
- `check_sheet_permissions(sheetid, permission_level)`
    - A method that allows you to quickly check if a certain access permission is met for a given sheet. Arguments are:
        - `sheetid`: The sheet to check permissions against.
        - `permission_level`: The desired permission level. Can be either of the string or int in the following dictionary: {"VIEWER": 1, "EDITOR": 2, "EDITOR_SHARE": 3, "ADMIN": 4, or "OWNER": 5}.
    - Returns an object with attributes "status" (whether the sheet was retrieved successfully), "access_met" (boolean indicating if at least the specified permission is met), "access_level" (the actual sheet's access_level) and "sheet_response" (the full response that was obtained when getting the sheet information).
- `check_workspace_permissions(spaceid, permission_level)`
    - Usage is the same as `check_sheet_permissions` but spaceid should be a Workspace ID instead.
- `check_folder_access(folderid)`
    - A method that checks whether the user has access to the specified folder ID. Returns a Boolean with `True` indicating that the a 'legitimate' Folder ID was provided.
- `get_container_from_url(container_url, search_list)`
    - A method that will return a container (sheets, dashboards & reports supported) provided a url:
        - `container_url`: The url of the container to be retrieved.
        - `search_list` (Optional): A list of containers to search through, or an IndexResult retrieved with a list_x method call. Will VERY GREATLY speed up the retrieval of the container if provided, as an API call to retrieve all the containers will not need to be made.
    - Note: This method is very slow, as it will retrieve a list of all the containers of the url's type (report, sheet, etc.) and iterate through them to locate the correct one. If using this method to retrieve multiple containers of the same type, it's recommended that you retrieve the container list separately and pass it as the search_list parameter. This can be done by using `search_list = smartsheet_client.Container.list_container(include_all=True)`, where "Container" is "Sheets", "Reports", or "Sights" respectively.

## Example Usage
This example use-case will create rows numbered 1-2000
```
import smartools as smartsheet  # Will import the entire smartsheet sdk for use.

smart = smartsheet.Smartsheet(<<YOUR API TOKEN>>)
rows_to_be_added = []

for i in range(2000):
    newrow = smartsheet.models.Row()
    newrow.to_bottom = True
    newrow.cells.append({
        'column_id': 6058237884688260,
        'value': i
    })
    rows_to_be_added.append(newrow)

response = smart.Util.bulk_add_rows(sheetid, rows_to_be_added)
added_rows = response.rows
```

   [smartsheet-python-sdk]: <https://github.com/smartsheet-platform/smartsheet-python-sdk>
