from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration


class BalancesGateway(object):
    """
    Trolley Balance module
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def get_trolley_balance(self):
        return self.get_all_balances("paymentrails")
    
    def get_paypal_balance(self):
        return self.get_all_balances("paypal")

    def get_all_balances(self, term=""):
        if term is None:
            raise InvalidFieldException("Term cannot be None")
        endpoint = '/v1/balances/' + term
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        
        balances = []
        for balance in response['balances']:
            tempbalance = trolley.Balances.factory(balance)
            balances.append(namedtuple("Balances", tempbalance.keys())(*tempbalance.values()))

        return balances
