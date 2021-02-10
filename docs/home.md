# Home class
All of the methods described below can be accessed using the Home class, per the examples found in the sdk documentation [here](https://smartsheet-platform.github.io/api-docs/?python#home).

## Get Container using URL | `smartsheet_client.Home.get_container_from_url`
This method allows you to use a url to a container and get the container.
**Parameters:**
- `container_url:` The url of the container that you will be retrieving.
- `search_list:` A list of Smartsheet items to search through for the the given container. If not provided, a list will be retrieved through an API call. However, providing a search list can be useful when you will be using this method multiple times, as it will save having to perform a lengthy API call every time.
**Example Usage:**
This example will retrieve a sheet using its url, then print out the sheet name.
```
sheet_url = "https://app.smartsheet.com/sheets/2Hr2Pgpwc7g6XMXMJpMV999gMQwQ2FXCGxvV5Mc1?view=grid"

sheet = smart.Home.get_container_from_url(sheet_url)

print(sheet.name)
```