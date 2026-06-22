import logging

from smartsheet import fresh_operation


class SmartoolsSharing:
    """Unified sharing operations for sheets, reports, sights, and workspaces.

    Implements the Smartsheet unified sharing API (POST/GET/PATCH/DELETE /shares)
    which replaces the deprecated per-asset-type sharing methods
    (Sheets.list_shares, Workspaces.share_workspace, Sights.share_sight, etc.).
    """

    def __init__(self, smartsheet_obj):
        self._base = smartsheet_obj
        self._log = logging.getLogger(__name__)

    def list_asset_shares(self, asset_type, asset_id, max_items=None, last_key=None,
                          include_all=False):
        """List all shares for the specified asset.

        Args:
            asset_type (str): Asset type — 'sheet', 'report', 'sight', or 'workspace'.
            asset_id (int): Asset ID.
            max_items (int): Maximum number of items per page.
            last_key (str): Pagination token from a previous response.
            include_all (bool): When True, auto-paginates to collect all shares.

        Returns:
            SmartoolsAssetSharesPaginatedResult: Result with .items and .data (alias).
        """
        _op = fresh_operation("list_asset_shares")
        _op["method"] = "GET"
        _op["path"] = "/shares"
        _op["query_params"]["assetType"] = asset_type
        _op["query_params"]["assetId"] = asset_id
        _op["query_params"]["maxItems"] = max_items
        _op["query_params"]["lastKey"] = last_key

        expected = ["AssetSharesPaginatedResult", "Share"]
        prepped = self._base.prepare_request(_op)
        result = self._base.request(prepped, expected, _op)

        if include_all:
            while result.next_page_token:
                next_page = self.list_asset_shares(
                    asset_type=asset_type,
                    asset_id=asset_id,
                    last_key=result.next_page_token,
                )
                result.items.extend(next_page.items)
                result.next_page_token = next_page.next_page_token

        return result

    def share_asset(self, share_obj, asset_type, asset_id, send_email=None):
        """Share an asset with one or more users or groups.

        Args:
            share_obj (Share | list[Share]): Share object or list of Share objects.
            asset_type (str): Asset type — 'sheet', 'report', 'sight', or 'workspace'.
            asset_id (int): Asset ID.
            send_email (bool): Whether to notify the user by email.

        Returns:
            Result: Result with .result[0] containing the created Share.
        """
        if not isinstance(share_obj, list):
            share_obj = [share_obj]

        _op = fresh_operation("share_asset")
        _op["method"] = "POST"
        _op["path"] = "/shares"
        _op["query_params"]["assetType"] = asset_type
        _op["query_params"]["assetId"] = asset_id
        _op["query_params"]["sendEmail"] = send_email
        _op["json"] = share_obj

        expected = ["Result", "Share"]
        prepped = self._base.prepare_request(_op)
        return self._base.request(prepped, expected, _op)

    def update_asset_share(self, share_obj, asset_type, asset_id, share_id):
        """Update the access level of an existing share.

        Args:
            share_obj (Share): Share object with updated access_level.
            asset_type (str): Asset type — 'sheet', 'report', 'sight', or 'workspace'.
            asset_id (int): Asset ID.
            share_id (str): Share ID to update.

        Returns:
            Share: The updated Share object.
        """
        _op = fresh_operation("update_asset_share")
        _op["method"] = "PATCH"
        _op["path"] = "/shares/" + str(share_id)
        _op["query_params"]["assetType"] = asset_type
        _op["query_params"]["assetId"] = asset_id
        _op["json"] = share_obj

        expected = "Share"
        prepped = self._base.prepare_request(_op)
        return self._base.request(prepped, expected, _op)

    def delete_asset_share(self, asset_type, asset_id, share_id):
        """Remove a share from an asset.

        Args:
            asset_type (str): Asset type — 'sheet', 'report', 'sight', or 'workspace'.
            asset_id (int): Asset ID.
            share_id (str): Share ID to delete.

        Returns:
            Result: Result object (resultCode 0 on success).
        """
        _op = fresh_operation("delete_asset_share")
        _op["method"] = "DELETE"
        _op["path"] = "/shares/" + str(share_id)
        _op["query_params"]["assetType"] = asset_type
        _op["query_params"]["assetId"] = asset_id

        expected = ["Result", None]
        prepped = self._base.prepare_request(_op)
        return self._base.request(prepped, expected, _op)

    def get_asset_share(self, asset_type, asset_id, share_id):
        """Retrieve a specific share for an asset.

        Args:
            asset_type (str): Asset type — 'sheet', 'report', 'sight', or 'workspace'.
            asset_id (int): Asset ID.
            share_id (str): Share ID to retrieve.

        Returns:
            Share: The Share object.
        """
        _op = fresh_operation("get_asset_share")
        _op["method"] = "GET"
        _op["path"] = "/shares/" + str(share_id)
        _op["query_params"]["assetType"] = asset_type
        _op["query_params"]["assetId"] = asset_id

        expected = "Share"
        prepped = self._base.prepare_request(_op)
        return self._base.request(prepped, expected, _op)
