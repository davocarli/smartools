from .share import SmartoolsShare


class SmartoolsAssetSharesPaginatedResult:
    """Result object for list_asset_shares.

    Exposes .items (new unified API convention) and .data (.items alias for
    backward compatibility with old per-asset-type list_shares callers).

    The new /shares endpoint returns the share list under the "items" key;
    the old per-asset endpoints used "data". We check "items" first.
    """

    def __init__(self, props, dynamic_type=None, base_obj=None):
        self._base = base_obj
        self.next_page_token = props.get("nextPageToken")
        raw = props.get("items") or props.get("data", [])
        self.items = [SmartoolsShare(item, base_obj) for item in raw]

    @property
    def data(self):
        return self.items
