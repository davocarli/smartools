import smartsheet
from smartsheet import fresh_operation

smart = smartsheet.Smartsheet("INIT")
smart.Sights

class SmartoolsSights(smartsheet.sights.Sights):
    def smartools(self):
        return 'smartools methods are available!'

    def create_sight(self):
        """Creates a dashboard in the "Sheets" folder.
        
        Returns: Result
        """
        _op = fresh_operation('create_sight')
        _op['method'] = 'POST'
        _op['path'] = '/internal/sights'
        _op['json'] = {}

        expected = ['Result', 'Sight']

        prepped_request = self._base.prepare_request(_op)
        response = self._base.request(prepped_request, expected, _op)

        return response

# Perform Monkey Patch
smartsheet.sights.Sights = SmartoolsSights