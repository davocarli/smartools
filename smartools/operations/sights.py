from smartsheet.sights import Sights


class SmartoolsSights(Sights):
    """Extended Sights operations with backward-compatible sharing methods
    routed through the unified sharing API.
    """

    def list_shares(self, sight_id, page_size=None, page=None, include_all=None):
        """List all shares for a sight (dashboard) via the unified sharing API.

        Replaces the deprecated Sights.list_shares endpoint.

        Returns:
            SmartoolsAssetSharesPaginatedResult: Result with .items and .data.
        """
        return self._base.Sharing.list_asset_shares(
            asset_type="sight",
            asset_id=sight_id,
            include_all=bool(include_all),
        )

    def share_sight(self, sight_id, share_obj, send_email=False):
        """Share a sight (dashboard) via the unified sharing API.

        Replaces the deprecated Sights.share_sight endpoint.
        Accepts a single Share object (old API signature) or a list.

        Returns:
            Result: Result with .result[0] containing the created Share.
        """
        return self._base.Sharing.share_asset(
            share_obj=share_obj,
            asset_type="sight",
            asset_id=sight_id,
            send_email=send_email,
        )

    def update_share(self, sight_id, share_id, share_obj):
        """Update a sight share via the unified sharing API.

        Replaces the deprecated Sights.update_share endpoint.
        """
        return self._base.Sharing.update_asset_share(
            share_obj=share_obj,
            asset_type="sight",
            asset_id=sight_id,
            share_id=share_id,
        )

    def delete_share(self, sight_id, share_id):
        """Delete a sight share via the unified sharing API.

        Replaces the deprecated Sights.delete_share endpoint.
        """
        return self._base.Sharing.delete_asset_share(
            asset_type="sight",
            asset_id=sight_id,
            share_id=share_id,
        )
