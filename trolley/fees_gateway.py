from collections import namedtuple

import trolley.configuration
from trolley.exceptions.invalidFieldException import InvalidFieldException
from trolley.types.fees import RevenueStream, RoutePricing


class FeesGateway(object):
    """
    Trolley fees module.
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def search_route_pricing(self, body=None):
        endpoint = '/v1/fees/route-pricing/search'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, {} if body is None else body)
        return [
            self.__namedtuple_from_factory("RoutePricing", RoutePricing, fee)
            for fee in response.get("fees", [])
        ]

    def create_revenue_stream(self, body):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/fees/revenue-stream/create'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, body)
        return self.__namedtuple_from_factory(
            "RevenueStream", RevenueStream, response["revenueStream"])

    def update_revenue_stream(self, body):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/fees/revenue-stream/update'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, body)
        return self.__namedtuple_from_factory(
            "RevenueStream", RevenueStream, response["revenueStream"])

    @staticmethod
    def __namedtuple_from_factory(name, factory, attributes):
        values = factory.factory(attributes)
        return namedtuple(name, values.keys())(*values.values())
