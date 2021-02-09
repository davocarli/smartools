class SmartoolsObject(object):
	def __init__(self, *initial_data, **kwargs):
		for dictionary in initial_data:
			for key in dictionary:
				setattr(self, key, dictionary[key])
		for key in kwargs:
			setattr(self, key, kwargs[key])

class RequirementError(Exception):
	pass

access_levels = {
	'VIEWER': 1,
	'EDITOR': 2,
	'EDITOR_SHARE': 3,
	'ADMIN': 4,
	'OWNER': 5
}