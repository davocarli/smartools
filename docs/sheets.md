# Sheets class
All of the methods described below can be accessed using the Sheets class, per the examples found in the sdk documentation [here](https://smartsheet-platform.github.io/api-docs/?python#sheets).

## Get Sheet  | `smartsheet_client.Sheets.get_sheet`
Usage of the get_sheet method is identical to the [original sdk](https://smartsheet-platform.github.io/api-docs/#get-sheet). However, the TypedLists have been modified to allow for retrieval of data using strings. In practice, this means that columns and cells can now be obtained using column names, and rows can be obtained using a stringified value found in the primary column (first match). For example:
```
sheet = smartsheet_client.Sheets.get_sheet(sheetid)

start_column = sheet.columns['Start Date']  # Get column named "Start Date"

new_name = sheet.rows[0].cells['Name']  # Get value of first row for column named "Name"

summary_row = sheet.rows['Summary']  # Get the first row on the sheet that says "Summary" in the primary column.
```
**Performance:** A stress test loading a maximum-size sheet (20,000 rows x 25 columns = 500,000 cells) 100 times revealed that a get_sheet operation only takes on average ~0.12 seconds longer with these changes. However, if you want to omit the extra processing, "dicts" can be added to the exclude parameter of the method.
## Bulk add Rows | `smartsheet_client.Sheets.bulk_add_rows`
Usage of the bulk_add_rows method is similar to the [original sdk](https://smartsheet-platform.github.io/api-docs/?python#add-rows), but it is not limited to 500 rows. If more than 500 rows are provided, this method will add them in batches and perform some common error handling on behalf of the user.
**Parameters:**
	    - `sheetid`: The ID of the sheet to add the rows to.
	    - `rows`: A list of smartsheet Row() objects to be added.
	    - `n`: The batch size that rows should be added in (default 500)
	    - `retries`: The number of consecutive failures before the operation is aborted (default 5).
	    - `sleep`: The amount of time to wait before retrying if a rate limiting error is encountered (default 60 seconds).
	**Returns:**
	An object with the following attributes:
	- `responses:` A list of the individual responses received when adding rows.
	- `rows`: A list of all the rows added (similar to the usual response received when adding rows via the sdk).
	- `data:` A list containing all of the data received fro responses.
	- `status:` A string indicating success of the operation.
**Example Usage:**
```
rows = []
for i in range(2000):
	new_row = smartsheet.models.Row()
	new_row.to_bottom = True
	new_row.cells.append({
		'column_id': 6058237884688260,
		'value': i
	rows.append(new_row)
smart.Sheets.bulk_update_rows(sheetid, rows)
```
## Bulk Update Rows | `smartsheet_client.Sheets.bulk_update_rows`
A method similar to the bulk add rows method, but updates rows instead of adding them. See [Bulk Add Rows (smartools)](#bulk-add-rows--smartsheet_client.sheets.bulk_add_rows) and [Update Rows (Smartsheet API Docs)](https://smartsheet-platform.github.io/api-docs/?python#update-rows) for more details.
## Check Sheet Permissions | `smartsheet_client.Sheets.check_sheet_permissions`
A method that allows you to perform the most efficient API call possible and check whether you have certain permissions on a sheet.
**Parameters:**
`sheet_id`: The ID of the sheet whose permissions are being checked.
`permission_level`: The minimum permission level you are checking for. Can be an integer (VIEWER=1, OWNER=5) or a string ("VIEWER", "EDITOR", "EDITOR_SHARE", "ADMIN", "OWNER").