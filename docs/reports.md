# SmartoolsReports Class
Smartools adds several new methods to the Reports class. All of these can be accessed through `smartsheet_client.Reports.<method_name>`

### `update_report`
This method allows you to update the specified report. Please note that only the name of the report can be updated, and none of its criteria/content can be modified.

**Args**
- report_id
    - ID of the report to update
- report_obj
    - A `smartsheet.models.Report` object with the new name to assign to the report.

### `move_report`
This method allows you to move a report to a new location. It functions very similarly to the `sights.move_sight` method.

**Args**
- report_id
    - ID of the report to move
- container_destination_obj
    - A `smartsheet.models.ContainerDestination` object specifying where the report should be moved.

### `get_large_report`
This method functions identically to the regular `get_report` method, but will automatically retrieve additional pages until the entire report has been retrieved, and return the report as one large report object with many rows.

**Args**
- report_id
    - The ID of the report to retrieve
- page_size (Optional - Default `None`)
    - The number of rows to retrieve in each request. Defaults to `None` which will retrieve 100 rows. For large reports, it's recommended to increase this to something ~ 2500.
- include (Optional - Default `None`)
    - The include parameter to pass on when retrieving the report.
- level (Optional - Default `None`)
    - The level parameter to pass on when retrieving the report.

### `get_access_level`
The `get_access_level` method makes the smallest request to get a report possible (include no rows), and returns report access level of the authenticated user to the report. If the sheet cannot be retrieved, it will return an 'UNSHARED' access level.

**Args**
- report_id
	- The ID of the report to get your access level for.
