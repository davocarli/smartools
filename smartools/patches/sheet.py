import smartsheet
from smartsheet.types import *
from smartsheet.util import serialize
from smartsheet.util import deserialize
from .form import SheetForm

class SmartoolsSheet(smartsheet.models.sheet.Sheet):
	pass

	# def __init__(self, props=None, base_obj=None):

	# 	self._forms = SmartoolsTypedList(SheetForm)

	# 	super(SmartoolsSheet, self).__init__(props, base_obj)

	# @property
	# def forms(self):
	# 	return self._forms
	
	# @forms.setter
	# def forms(self, value):
	# 	self._forms.load(value)

# smartsheet.models.sheet.Sheet = SmartoolsSheet
