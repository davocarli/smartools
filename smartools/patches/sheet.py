import smartsheet
from smartsheet.types import *
from smartsheet.util import serialize
from smartsheet.util import deserialize
from .form import SheetForm

class Sheet(smartsheet.models.sheet.Sheet):
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

	def __setattr__(self, key, value):
		if key == 'id':
			self.id_ = value
		else:
			super(Sheet, self).__setattr__(key, value)

smartsheet.models.sheet.Sheet = Sheet
