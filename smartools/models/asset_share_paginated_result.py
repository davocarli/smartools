from smartsheet.models import Share


class SmartoolsAssetSharesPaginatedResult:
    """Result object for list_asset_shares.

    Exposes .items (new unified API convention) and .data (.items alias for
    backward compatibility with old per-asset-type list_shares callers).
    """

    def __init__(self, props, dynamic_type=None, base_obj=None):
        self._base = base_obj
        self.next_page_token = props.get("nextPageToken")
        self.items = [Share(item, base_obj) for item in props.get("data", [])]

    @property
    def data(self):
        return self.items
