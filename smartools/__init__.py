# Multiple imports are performed to ensure that classes are overwritten in the correct order.u

from .patches import *

import smartsheet
from smartsheet import *  # Import all the modules from smartsheet.

for var in dir(smartsheet):  # Define all variables locally that are defined during
	if var not in dir():	 # smartsheet's __init__ such as __gov_base__ or __api_base__.
		exec(var + ' = smartsheet.' + var)

from smartools.smartools import Smartsheet  # Import our new custom subclass
