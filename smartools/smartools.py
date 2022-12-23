import importlib
from modulefinder import Module
import re

import smartsheet
from smartsheet.smartsheet import OperationErrorResult

class Smartools(smartsheet.Smartsheet):

    def smartools(self):
        return True

    def __getattr__(self, name):
        """
        Handle sub-class instantiation.

        Args:
            name (str): Name of smartsheet to instantiate.

        Returns:
            Instance of named class.
        """
        if name == 'smartools':
            return self.smartools
        try:
            # smartools api class first
            class_ = getattr(importlib.import_module(
                __package__ + '.operations.' + name.lower()), 'Smartools' + name)
            return class_(self)
        except ImportError:
            # smartools model class next
            try:
                class_ = getattr(importlib.import_module(
                    __package__ + '.models.' + name.lower(), 'Smartools' + name
                ))
                class_ = getattr(importlib.import_module(
                    name.lower()), name)
                return class_()
            except ImportError:
            # smartsheet classes next
                return super().__getattr__(name)

class SmartoolsOperationResult(smartsheet.smartsheet.OperationResult):

    def native(self, expected):
        try:
            if expected != 'DownloadedFile':
                data = self.resp.json()
            else:
                filename = re.findall(
                        'filename="(.+)";',
                        self.resp.headers['Content-Disposition'])

                data = {
                    'resultCode': 0,
                    'message': 'SUCCESS',
                    'resp': self.resp,
                    'filename': filename[0],
                    'downloadDirectory': self.operation['dl_path']
                }
        except ValueError:
            return OperationErrorResult(self.op_result, self.resp)

        if isinstance(expected, list):
            klass = expected[0]
            dynamic_type = expected[1]
            try:
                class_ = getattr(importlib.import_module(
                    'smartools.models'), 'Smartools' + klass)
            except AttributeError:
                class_ = getattr(importlib.import_module(
                    'smartsheet.models'), klass)
            obj = class_(data, dynamic_type, self._base)
            if hasattr(obj, 'request_response'):
                obj.request_response = self.resp

            return obj

        try:
            class_ = getattr(importlib.import_module(
                'smartools.models'), 'Smartools' + expected)
        except AttributeError:
            class_ = getattr(importlib.import_module(
                'smartsheet.models'), expected)

        obj = class_(data, self._base)
        if hasattr(obj, 'request_response'):
            obj.request_response = self.resp

        return obj

# Perform Monkey Patches
smartsheet.smartsheet.OperationResult = SmartoolsOperationResult
