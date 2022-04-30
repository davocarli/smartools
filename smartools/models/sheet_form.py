from smartsheet.types import *
from smartsheet.util import serialize, deserialize

class SheetForm(object):

    """Smartsheet SheetForm data model."""

    def __init__(self, props=None, base_obj=None):
        """Initialize the SheetForm model."""
        self._base = None
        if base_obj is not None:
            self._base = base_obj
        
        self._id = Number()
        self._publish_type = String()
        self._publish_key = String()
        self._publish_url = String()
        self._title = String()
        self._published = Boolean()

        if props:
            deserialize(self, props)

        self.request_response = None
        self.__initialized = True

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id.value = value

    @property
    def publish_type(self):
        return self._publish_type.value

    @publish_type.setter
    def publish_type(self, value):
        self._publish_type.value = value

    @property
    def publish_key(self):
        return self._publish_key.value

    @publish_key.setter
    def publish_key(self, value):
        self._publish_key.value = value

    @property
    def publish_url(self):
        return self._publish_url

    @publish_url.setter
    def publish_url(self, value):
        self._publish_url.value = value
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title.value = value

    @property
    def published(self):
        return self._published

    @published.setter
    def published(self, value):
        self._published.value = value

    def to_dict(self):
        return serialize(self)

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()
