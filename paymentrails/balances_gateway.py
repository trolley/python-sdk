from collections import namedtuple
from paymentrails.exceptions.invalidFieldException import InvalidFieldException
import paymentrails.configuration


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
        endpoint = '/v1/profile/balances/' + term
        response = paymentrails.configuration.Configuration.client(
            self.config).get(endpoint)
        oldbalance = paymentrails.balances.Balances.factory(response)
        balance = namedtuple("Balances", oldbalance.keys())(*oldbalance.values())
        return balance
