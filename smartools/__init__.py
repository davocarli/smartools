import importlib
import logging
import inspect

import smartsheet

# Monkey patch types
from .types.enumerated_value import SmartoolsEnumeratedValue

from smartsheet import models as smartsheet_models
from . import models

patches = []

for model in dir(models):
	# if model.startswith('Smartools'):
	class_ = getattr(models, model)
	if hasattr(class_, '__name__') and class_.__name__.startswith('Smartools'):
		name = class_.__name__
		base = class_.__base__
		patches.append((class_, base))
patches.append((models.enums.SmartoolsAccessLevel, smartsheet.models.enums.AccessLevel))
patches.append((SmartoolsEnumeratedValue, smartsheet.types.EnumeratedValue))

for class_, base in patches:
	for model in dir(smartsheet_models):
		try:
			module = importlib.import_module(
				'smartsheet.models.' + model
			)
			imports = dir(module)
			for i in imports:
				smar_module = getattr(module, i)
				if module.__name__ != inspect.getmodule(smar_module).__name__:
					smar_module = getattr(module, i)
					if smar_module == base:
						smar_module = class_
						module_to_patch = 'smartsheet.models.' + model + '.' + base.__name__
						logging.info('Patching ' + module_to_patch)
						exec(module_to_patch + ' = class_')
						exec('smartsheet.models.' + base.__name__ + ' = class_')
		except (ImportError, AttributeError):
			pass

# Import Smartsheet and copy all init variables such as __gov_base__ and __api_base__.
from smartsheet import *

for var in dir(smartsheet):
	if var not in dir():
		exec(var + ' = smartsheet.' + var)

# Replace Smartsheet 
from .smartools import Smartools as Smartsheet

# Additional variables
__eu_base__ = 'https://api.smartsheet.eu/2.0'
__us_base__ = smartsheet.__api_base__
