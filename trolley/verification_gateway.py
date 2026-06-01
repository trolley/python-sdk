from collections import namedtuple
from urllib.parse import urlencode

import trolley.configuration
from trolley.exceptions.invalidFieldException import InvalidFieldException
from trolley.types.meta import Meta
from trolley.types.verification import Verification


class VerificationGateway(object):
    """
    Trolley verification processor.
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def search(self, **filters):
        endpoint = '/v1/verifications'
        query = urlencode(filters, doseq=True)
        if query:
            endpoint = f'{endpoint}?{query}'
        response = trolley.configuration.Configuration.client(self.config).get(endpoint)
        return self.__build_verifications_from_response(response, True)

    all = search

    def expire(self, body):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/verifications/expire'
        response = trolley.configuration.Configuration.client(self.config).patch(endpoint, body)
        return self.__build_verifications_from_response(response, True)

    def trigger(self, verification_type, body):
        if verification_type is None:
            raise InvalidFieldException("Verification type cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = f'/v1/verifications/{verification_type}/trigger'
        response = trolley.configuration.Configuration.client(self.config).post(endpoint, body)
        return self.__build_verifications_from_response(response, True)

    def trigger_watchlist(self, body):
        return self.trigger('watchlist', body)

    def __build_verifications_from_response(self, response, include_meta=False):
        verifications = []
        count = 0
        for verification in response.get('verifications', []):
            temp = Verification.factory(verification)
            verifications.insert(count, namedtuple("Verification", temp.keys())(*temp.values()))
            count = count + 1

        if include_meta and response.get('meta') is not None:
            tempmeta = Meta.factory(response['meta'])
            verifications.insert(count, namedtuple("Meta", tempmeta.keys())(*tempmeta.values()))

        return verifications
