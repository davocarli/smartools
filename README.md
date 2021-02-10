
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
A prior version of smartools did not patch the SDK's classes directly, but instead added a new class at smartsheet_client.Util.*method_name*. The use of this class has been deprecated, and calling these methods will now make a deprecation warning then call the newly-patched method directly. The one current exception is the get_container_from_url method, which can still only be called from the Util class.


[smartsheet-python-sdk]: <https://github.com/smartsheet-platform/smartsheet-python-sdk>
