# Smartools

smartools is a wrapper around the official [smartsheet-python-sdk]. It monkey patches several classes to add new functionality, and also implements some completely new classes/models as well.

The decision was made to monkey patch the smartsheet sdk rather than fork it because by extending the existing package, this package can be updated independently of the original sdk and sis not dependent on a specific version.

## Installation

The package is available to install from [PyPi](https://pypi.org/project/smartools/) using:

```
pip install smartools
```

Once installed it can be imported with `import smartools` or can more "authentically" replace the official sdk by using `import smartools as smartsheet`

## Usage

In general, usage of smartools is identical to the standard SDK. All original functionality is supported so any existing code should not need to be updated. For more information, see the [Smartsheet API Docs](https://smartsheet.redoc.ly/).

## Extended/Improved Functionality

### Comparison of sharing permissions

smartools allows you to easily compare sharing permissions using the standard >, <, >=, >=, == methods. This can be useful when writing code that will evaluate whether a user has high enough permissions to perform an action. Smartools also has added support for the COMMENTER permission level. It also includes a new permission level, "UNSHARED" that can be used for comparisons. That permission level simply indicates that somethng isn't shared to you, and is only ever returned when using a `get_access_level` method.

```
sheet = smartsheet_client.Sheets.get_sheet(sheet_id)

sheet.access_level                 # EDITOR_SHARE
sheet.access_level >= 'EDITOR'     # True
sheet.access_level == 'OWNER'      # False
sheet.access_level > 'EDITOR'      # True
sheet.access_level != 'UNSHARED'   # True - This is a new "permission level" exclusive to smartools
```

### Easily Retrieve Child Rows

Rows now allow you to get their child rows by accessing row.children.

```
sheet = smartsheet_client.Sheets.get_sheet(sheet_id)

sheet.rows[0].children  # Will return a list of child rows
```

### Indexing sheets/reports

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

Indexing rows can be done utilizing the primary column value or by using a tuple to specify the column that should be searched. Indexing with integers is still possible.

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

### Getting Forms

Calling `get_sheet` with `include='publishedFormContainers'` will now include basic form information (such as its permalink) with the sheet.

## Brand New Functionality

### Cell Formatting

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

### New methods

Several new methods have been added to the various classes within the smartsheet_client, these are listed below and documented in more detail within their respective docs.

### [Sheets](./docs/sheets.md)

-   `Sheets.bulk_add_rows`
-   `Sheets.bulk_update_rows`
-   `Sheets.bulk_delete_rows`
-   `Sheets.get_access_level`

### [Reports](./docs/reports.md)

-   `Reports.update_report`
-   `Reports.move_report`
-   `Reports.get_large_report`
-   `Reports.get_access_level`

### [Home](./docs/home.md)

-   `Home.get_container_from_url`
-   `Home.create_sight`
-   `Home.create_report`

### [Folders](./docs/folders.md)

-   `Folders.list_sheets_in_folder`
-   `Folders.list_containers_in_folder`
-   `Folders.get_access_level`
-   `Folders.create_sight_in_folder`
-   `Folders.create_report_in_folder`

### [Workspaces](./docs/workspaces.md)

-   `Workspaces.list_sheets_in_workspace`
-   `Workspaces.list_containers_in_workspace`
-   `Workspaces.get_access_level`
-   `Workspaces.create_sight_in_workspace`
-   `Workspaces.create_report_in_workspace`

[smartsheet-python-sdk]: https://github.com/smartsheet-platform/smartsheet-python-sdk
