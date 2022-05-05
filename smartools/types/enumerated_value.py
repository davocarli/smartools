from enum import Enum

import six
from smartsheet.types import EnumeratedValue

class SmartoolsEnumeratedValue(EnumeratedValue):

    def __init__(self, *args, **kwargs):
        from smartsheet.models.enums.access_level import AccessLevel
        from smartools.models.enums.access_level import SmartoolsAccessLevel
        self._access_level_classes = (SmartoolsAccessLevel, AccessLevel)
        super().__init__(*args, **kwargs)

    def set(self, value):
        if isinstance(value, int):
            self._value = self._EnumeratedValue__enum(value)
        else:
            super().set(value)

    def __lt__(self, other):
        if isinstance(self._value, self._access_level_classes):
            return self._access_level_lt(other)
        return super().__lt__(other)
    
    def __le__(self, other):
        if isinstance(self._value, self._access_level_classes):
            return self._access_level_le(other)
        return super().__le__(other)

    def __gt__(self, other):
        if isinstance(self._value, self._access_level_classes):
            return self._access_level_gt(other)
        return super().__gt__(other)
    
    def __ge__(self, other):
        if isinstance(self._value, self._access_level_classes):
            return self._access_level_ge(other)
        return super().__ge__(other)

    def _access_level_lt(self, other):
        if isinstance(other, Enum):
            return self._value.value < other.value
        elif isinstance(other, self._access_level_classes):
            return self._value.value < other._value.value
        elif isinstance(other, six.string_types):
            other_value = self._access_level_classes[0][other]
            return self._value.value < other_value.value
        elif isinstance(other, EnumeratedValue) and isinstance(other._value, self._access_level_classes):
            return self._value.value < other._value.value
        elif isinstance(other, int):
            return self._value.value < other
        return super().__lt__(other)
    
    def _access_level_le(self, other):
        if isinstance(other, Enum):
            return self._value.value <= other.value
        elif isinstance(other, self._access_level_classes):
            return self._value.value <= other.value
        elif isinstance(other, six.string_types):
            other_value = self._access_level_classes[0][other]
            return self._value.value <= other_value.value
        elif isinstance(other, EnumeratedValue) and isinstance(other._value, self._access_level_classes):
            return self._value.value <= other._value.value
        elif isinstance(other, int):
            return self._value.value <= other
        return super().__le__(other)
    
    def _access_level_gt(self, other):
        if isinstance(other, Enum):
            return self._value.value > other.value
        elif isinstance(other, self._access_level_classes):
            return self._value.value > other.value
        elif isinstance(other, six.string_types):
            other_value = self._access_level_classes[0][other]
            return self._value.value > other_value.value
        elif isinstance(other, EnumeratedValue) and isinstance(other._value, self._access_level_classes):
            return self._value.value > other._value.value
        elif isinstance(other, int):
            return self._value.value > other
        return super().__gt__(other)

    def _access_level_ge(self, other):
        if isinstance(other, Enum):
            return self._value.value >= other.value
        elif isinstance(other, self._access_level_classes):
            return self._value.value >= other.value
        elif isinstance(other, six.string_types):
            other_value = self._access_level_classes[0][other]
            return self._value.value >= other_value.value
        elif isinstance(other, EnumeratedValue) and isinstance(other._value, self._access_level_classes):
            return self._value.value >= other._value.value
        elif isinstance(other, int):
            return self._value.value >= other
        return super().__ge__(other)    

    def __eq__(self, other):
        if isinstance(other, Enum) or other is None:
            return self._value == other
        elif isinstance(other, six.string_types):
            return self._value == self._EnumeratedValue__enum[other]
