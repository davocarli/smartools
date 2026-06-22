from smartsheet.models import Share


class SmartoolsShare(Share):
    """Share model that handles the new unified API's string-typed numeric IDs.

    The new /shares endpoint returns userId and groupId as JSON strings
    (e.g. "967346962622340") instead of integers. The base Share model's
    Number validator rejects strings, so we intercept those setters here.

    Monkey-patching in smartools/__init__.py will replace smartsheet.models.Share
    with this class, so all code paths (Result, list responses) benefit
    automatically.
    """

    @Share.user_id.setter
    def user_id(self, value):
        if isinstance(value, str):
            try:
                value = int(value)
            except (ValueError, TypeError):
                return
        self._user_id.value = value

    @Share.group_id.setter
    def group_id(self, value):
        if isinstance(value, str):
            try:
                value = int(value)
            except (ValueError, TypeError):
                return
        self._group_id.value = value
