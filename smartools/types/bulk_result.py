class BulkOperationResult(object):

    def __init__(self, main_attr):

        self._main_attr = main_attr
        self.responses = []
        self._data = []
        self.status = None
        self.result = None
        self.error = None
    
    def __getattr__(self, name):
        if name == self._main_attr:
            return self._data
        return super().__getattribute__(name)
