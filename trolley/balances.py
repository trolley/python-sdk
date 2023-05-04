from trolley.configuration import Configuration
from trolley.gateway import Gateway

class Balances:
    """
    A class that facilitates Client requests to
    the PaymentRails API in regards to Balances.
    """
    _attributes = {}


    @staticmethod
    def find(term=""):
        """
        Retrieve a balance
            Balances.find()
        """
        config = Configuration(Configuration.public_key, Configuration.private_key, Configuration.enviroment)
        return Gateway(config).balances.find(term)
    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""
        for field in attributes.get('balances'):
            Balances._attributes.update({field:""})
            Balances._attributes[field] = attributes['balances'].get(field)

        return Balances._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Balances and returns it. """
        instance = Balances._initialize(attributes)
        return instance
