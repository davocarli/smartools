# SmartoolsSheets Class
Smartools adds several new methods to the Sheets class. All of these can be accessed through `smartsheet_client.Sheets.<method_name>`

### `bulk_add_rows` / `bulk_update_rows`
The `bulk_add_rows` & `bulk_update_rows` methods function just like the `add_rows` & `update_rows` methods, with the exception that your list of rows can have more than 500 rows in it. The method will automatically split the rows into smaller requests, and perform some basic error handling. If an error is encountered, the method will halve the size of the requests to avoid timeouts, and if a rate limiting error is encountered it will pause for one minute before continuing.

**Args**
- sheet_id
	- ID of sheet to add/update rows on
- rows
	- List of rows to be added/updated on the sheet
- n (optional - default 500)
	- The number of rows to be sent in each request
- retries (optional - default 5)
	- The number of times to retry a failed request before throwing an Exception
- sleep (optional - default 60)
	- The number of seconds to wait if a rate limit error is encountered.

### `get_access_level`
The `get_access_level` method makes the smallest request to get a sheet possible (include no columns or rows), and returns the access level of the authenticated user to the sheet. If the sheet cannot be retrieved, it will return an 'UNSHARED' access level.

**Args**
- sheet_id
	- The sheet to get your access level for.
