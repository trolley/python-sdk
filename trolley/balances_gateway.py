from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration
from trolley.types.balances import Balances


class BalancesGateway(object):
    """
    Trolley Balance module
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def get_trolley_balance(self):
        endpoint = '/v1/balances/paymentrails'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        return self.__build_balances_from_response(response)

    paymentrails = get_trolley_balance
    
    def get_paypal_balance(self):
        endpoint = '/v1/balances/paypal'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        return self.__build_balances_from_response(response)

    paypal = get_paypal_balance

    def get_all_balances(self, term=""):
        if term is None:
            raise InvalidFieldException("Term cannot be None")
        if term:
            endpoint = f'/v1/balances/{term}'
        else:
            endpoint = '/v1/balances'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        return self.__build_balances_from_response(response)

    def __build_balances_from_response(self, response):
        balances = []
        for balance in response['balances']:
            tempbalance = Balances.factory(balance)
            balances.append(namedtuple("Balances", tempbalance.keys())(*tempbalance.values()))

        return balances

    all = get_all_balances
    find = get_all_balances
