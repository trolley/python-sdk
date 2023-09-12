from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration

from trolley.types.meta import Meta
from trolley.types.offline_payment import OfflinePayment

class OfflinePaymentGateway(object):
    """
    Trolley OfflinePayment processor
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    """ This method returns a generator which iterates through all the pages of Offline Payments.
     If you want to paginate manually, please use get_all_by_page() instead. """
    def get_all(self):
        page = 0
        should_paginate = True
        while should_paginate:
            page+=1
            endpoint = f'/v1/offline-payments?page={page}&pageSize=10'
            response = trolley.configuration.Configuration.client(self.config).get(endpoint)
            yield from self.__build_offline_payments_from_response(response)

            if page < response["meta"]["pages"]:
                should_paginate = True
            else:
                should_paginate = False

    """ This method returns all offline payments but requires you to specify page number and page size manually.
     If you want to auto paginate, use get_all() method instead. """
    def get_all_by_page(self, page=1, pageSize=10):
            endpoint = f'/v1/offline-payments?page={page}&pageSize={pageSize}'
            response = trolley.configuration.Configuration.client(self.config).get(endpoint)
            return self.__build_offline_payments_from_response(response, True)

    """ Creates a new Offline Payment for a Recipient whose ID is provided """
    def create(self, recipient_id, body,):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        elif recipient_id is None:
            raise InvalidFieldException("Recipient ID cannot be None.")
        endpoint = f'/v1/recipients/{recipient_id}/offlinePayments/'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, body)

        temppayment = OfflinePayment.factory(response)
        offlinepayment = namedtuple("OfflinePayment", temppayment.keys())(*temppayment.values())
        return offlinepayment

    """ Update an Offline Payment """
    def update(self, offline_payment_id, recipient_id, body):
        if offline_payment_id is None:
            raise InvalidFieldException("Offline Payment id cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        if recipient_id is None:
            raise InvalidFieldException("Recipient ID cannot be None.")
        endpoint = f'/v1/recipients/{recipient_id}/offlinePayments/{offline_payment_id}'
        response = trolley.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        temppayment = OfflinePayment.factory(response)
        offlinepayment = namedtuple("OfflinePayment", temppayment.keys())(*temppayment.values())
        return offlinepayment

    """ Delete an Offline Payment """
    def delete(self, recipient_id, offline_payment_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient ID cannot be None.")
        if offline_payment_id is None:
            raise InvalidFieldException("Offline Payment ID cannot be None.")
        
        endpoint = f'/v1/recipients/{recipient_id}/offlinePayments/{offline_payment_id}'
        response = trolley.configuration.Configuration.client(
            self.config).delete(endpoint)
        return response['ok']
        
    def __build_offline_payments_from_response(self, response, include_meta=False):
        offlinepayments = []
        count = 0
        for offlinepayment in response['offlinePayments']:
            temppayment = OfflinePayment.factory(offlinepayment)
            newpayment = namedtuple("OfflinePayment", temppayment.keys())(*temppayment.values())
            offlinepayments.insert(count, newpayment)
            count = count + 1
        
        if include_meta:
            tempmeta = Meta.factory(response['meta'])
            offlinepayments.insert(count,namedtuple("Meta", tempmeta.keys())(*tempmeta.values()))

        return offlinepayments
