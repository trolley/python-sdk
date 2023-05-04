from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration


class BalancesGateway(object):
    """
    PaymentRails Balance module
    Manages balances
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def find(self, term=""):
        if term is None:
            raise InvalidFieldException("Term cannot be None")
        endpoint = '/v1/balances/' + term
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        oldbalance = trolley.balances.Balances.factory(response)
        balance = namedtuple("Balances", oldbalance.keys())(*oldbalance.values())
        return balance
