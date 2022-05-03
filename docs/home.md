# SmartoolsHome Class
Smartools adds several new methods to the Home class. All of these can be accessed through `smartsheet_client.Home.<method_name>`

### `get_container_from_url`
The `get_container_from_url` method will search your entire Smartsheet account for an item, based on its url. Please note that if you are shared to many items, this can be a slow operation, since your entire account will need to be loaded and iterated through until finding the item.
```
# Example
sheet_url = 'https://app.smartsheet.com/sheets/R4qfP3CrGVWJMHcRQpWrH66v44WR6Q7wRp4M7Hj1?view=grid'
sheet = smartsheet_client.Home.get_container_from_url(sheet_url)

sheet.name  # "My Sheet"

dashboard_url = 'https://app.smartsheet.com/dashboards/W9H8JF7vmc75mp2Mj7wwmmhg7Fc6pW48cjrpvXG1'
dashboard = smartsheet_client.Home.get_container_from_url(dashboard_url)

dashboard.name  # "A Dashboard!"
```

**Args**
- container_url
    - The url of the item that is being searched for.
- search_list (Optional - Default `None`)
    - If provided, the method will search through the provided list, rather than make an API request to search the list. This can be useful if needing to retrieve multiple items by url.

### `create_sight`
The `create_sight` method creates a sight inside of the user's Sheets folder within Home. Please note that only the sight's name can be specified.

**Args**
- sight_obj
    - A `smartsheet.models.Sight` object to be created. Please note that only the sight name can be specified.

### `create_report`
The `create_report` method creates a report inside of the user's Sheets folder within Home. Please note that only the report's name can be specified.

**Args**
- report_obj
    - A `smartsheet.models.Report` object to be created. Please note that only the report name can be specified.
