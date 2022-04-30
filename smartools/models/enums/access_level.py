from enum import Enum

class SmartoolsAccessLevel(Enum):
    UNSHARED = 0 # Used for the get_access_level methods, returns if you not shared
    VIEWER = 1
    SHARED = 1 # Used for folders only, since they don't have an access level
    COMMENTER = 2
    EDITOR = 3
    EDITOR_SHARE = 4
    ADMIN = 5
    OWNER = 6
