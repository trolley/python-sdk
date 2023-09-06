from trolley.configuration import Configuration
from trolley.gateway import Gateway

class Balances:
    """
    A class that facilitates Client requests to
    the Trolley API in regards to Balances.
    """
    _attributes = {
        'accountNumber': "",
        'amount': "",
        'amountCleared': "",
        'amountPending': "",
        'currency': "",
        'display': "",
        'pendingCredit': "",
        'pendingDebit': "",
        'primary': "",
        'provider': "",
        'providerAcct': "",
        'providerId': "",
        'type': ""
    }
    
    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            'accountNumber',
            'amount',
            'amountCleared',
            'amountPending',
            'currency',
            'display',
            'pendingCredit',
            'pendingDebit',
            'primary',
            'provider',
            'providerAcct',
            'providerId',
            'type'
        ]

        for field in fields:
            if attributes.get('balances') is None:
                Balances._attributes[field] = attributes.get(field)
            elif attributes['balances'].get(field) is not None:
                Balances._attributes[field] = attributes['balances'][field]

        return Balances._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Balances and returns it. """
        instance = Balances._initialize(attributes)
        return instance
