
# Smartools

smartools is a wrapper around the official [smartsheet-python-sdk]. It monkey patches several classes to add new functionality, and also implements some completely new classes/models as well.

The decision was made to monkey patch the smartsheet sdk rather than fork it because by extending the existing package, this package can be updated independently of the original sdk and sis not dependent on a specific version.

## Installation
The package is being submited to PyPI soon (when docs are complete), and can currently be installed using:
```
pip install git+https://github.com/davocarli/smartools.git
```
Once installed it can be imported with `import smartools` or can more "authentically" replace the official sdk by using `import smartools as smartsheet`

## Usage
In general, usage of smartools is identical to the standard SDK. All original functionality is supported so any existing code should not need to be updated. For more information, see the [Smartsheet API Docs](https://smartsheet.redoc.ly/).

## Extended/Improved Functionality
Some of the greatest improvements to smartools are in the indexing of lists. Rows, Columns, and Cells can now be indexed using strings, as explained below.

#### Columns
Index a list of columns by utilizing the column name. You can also find the primary column with an empty string `''`. Indexing with integers (based on positioning) is still possible.
```
sheet = smartshet_client.Sheets.get_sheet(sheet_id)

sheet.columns['Date'].type  # DATE
sheet.columns[''].primary   # True
sheet.columns[3].title      # Column4
```

#### Rows
Indexing rows can be done utilizing the primary column value. Indexing with integers is still possible.

NOTE: If multiple rows have the same primary column value, the **first** row with this value will be returned. If indexing with an empty string `''` the first row with no primary column value will be returned.
```
sheet = smartsheet_client.Sheets.get_sheet(sheetid)

sheet.rows['Task Name'].id  # 12345678910
```

#### Cells
Indexing a list of cells can be done utilizing column names. Indexing with integers is still possible. 

NOTE: Indexing this way is only possible in requests where columns have been obtained, such as when getting a sheet or report, but will not work if columns are not included in the response, such as when getting a row.
```
sheet = smartsheet_client.Sheets.get_sheet(sheetid)

sheet.rows['Phase 1'].cells['Start Date'].value  # 01/01/20222
```

## Cell Formatting
smartools includes a CellFormat model that allows you to apply formatting in a more user-friendly way. To use this, create a `CellFormat` object and update its various properties, such as `font_family`, `thousands_separator`, etc. A short usage example can be seen below, and a full list of all the properties that can be updated can be found [here](./docs/cell_format.md).
```
formatting = smartsheet.models.CellFormat()
formatting.font_type = 'TAHOMA'
formatting.font_size = 'TWELVE'
formatting.bold = 1  # Will apply the "1" setting of legacy formatting management using strings, which is "ON"

new_row = smartsheet.models.Row()
new_row.cells.append({
    'column_id': 12345678910,
    'value': 'My Value',
    'format': formatting,
})
new_row.cells.append({
    'column_id': 23456789101,
    'value': 'My Other Value',
    'format': smartsheet.models.CellFormat({
        'italic': 'ON',
        'strikethrough': 'ON',
        'background_color': 'FFFEE6',
    })
})

smartsheet_client.Sheets.add_rows(sheet_id, new_row)
```

# Smartools

smartools is a wrapper that extends the official [smartsheet-python-sdk]. It monkey patches several classes to add new functionality, and adds a new "SmartsheetUtilities" subclass (accessible at smartsheet_client.Util) that contains several methods that perform more complex but common operations. The decision was made to monkey patch the smartsheet sdk, rather than fork it, because:
- The official sdk does what it is designed to do very well - it allows you to perform calls to the Smartsheet API. Many of my additions instead perform some amount of processing of the data, or multiple API calls, so they are outside the scope of the SDK.
- By subclassing the existing package, this package can be updated independently of the original sdk, and is not dependent on a specific version.

## Installation
This package has not (yet) been added to PyPI, but can be installed using:
```
pip install git+https://github.com/davocarli/smartools.git
```
Once installed it can be imported with `import smartools` or for a more authentic replacement to the official sdk `import smartools as smartsheet`

## Usage
In general, usage of smartools is identical to the standard SDK. All original functionality is supported. For more information see the [Smartsheet API Docs](https://smartsheet-platform.github.io/api-docs/?python#). With that being said, smartools also adds several improved or new methods:

### [Sheets](./docs/sheets.md)
- Altered methods
    - [Get Sheet](./docs/sheets.md#get-sheet---smartsheet_clientsheetsget_sheet)
- New methods
    - [Bulk Add Rows](./docs/sheets.md#bulk-add-rows--smartsheet_clientsheetsbulk_add_rows)
    - [Bulk Update Rows](./docs/sheets.md#bulk-update-rows--smartsheet_clientsheetsbulk_update_rows)
    - [Check Sheet Permissions](./docs/sheets.md#check-sheet-permissions--smartsheet_clientsheetscheck_sheet_permissions)
    - [Get Pandas DataFrame](./docs/sheets.md#get-pandas-dataframe--smartsheet_clientsheetsget_sheet_as_pandas_dataframe)

### [Workspaces](./docs/workspaces.md)
- New methods
    - [List Sheets](./docs/workspaces.md#list-sheets---smartsheet_clientworkspaceslist_sheets_in_workspace)
    - [List Containers](./docs/workspaces.md#list-containers--smartsheet_clientworkspaceslist_containers_in_workspace)
    - [Check Workspace Permissions](./docs/workspaces.md#check-workspace-permissions--smartsheet_clientworkspacescheck_workspace_permissions)

### [Folders](./docs/folders.md)
- New methods
    - [List Sheets](./docs/folders.md#list-sheets---smartsheet_clientfolderslist_sheets_in_folder)
    - [List Containers](./docs/folders.md#list-containers--smartsheet_clientfolderslist_containers_in_folder)
    - [Check Folder Access](./docs/folders.md#check-folder-access--smartsheet_clientfolderscheck_folder_access)

### [Home](./docs/home.md)
- New methods
    - [Get Container Using URL](./docs/home.md#get-container-using-url--smartsheet_clienthomeget_container_from_url)

## The "Util" class
A prior version of smartools did not patch the SDK's classes directly, but instead added a new class at smartsheet_client.Util.*method_name*. The use of this class has been deprecated, and calling these methods will now make a deprecation warning then call the newly-patched method directly. These methods may be completely removed in a future release.


[smartsheet-python-sdk]: <https://github.com/smartsheet-platform/smartsheet-python-sdk>
