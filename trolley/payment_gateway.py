from collections import namedtuple
import pprint
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration

from trolley.types.meta import Meta

class PaymentGateway(object):
    """
    Trolley Payment processor
    Creates and manages transactions
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def find(self, payment_id, batch_id):
        if payment_id is None:
            raise InvalidFieldException("Payment id cannot be None.")
        if batch_id is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batch_id + '/payments/' + payment_id
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        temppayment = trolley.Payment.factory(response)
        payment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
        return payment

    def create(self, body, batch_id):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        elif batch_id is None:
            raise InvalidFieldException("Batch ID cannot be None.")
        endpoint = '/v1/batches/' + batch_id + '/payments/'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, body)
        temppayment = trolley.Payment.factory(response)
        payment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
        return payment

    def update(self, payment_id, body, batch_id):
        if payment_id is None:
            raise InvalidFieldException("Payment id cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/batches/' + batch_id + '/payments/' + payment_id
        response = trolley.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        temppayment = trolley.Payment.factory(response)
        payment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
        return payment

    def delete(self, payment_id, batch_id):
        if payment_id is None:
            raise InvalidFieldException("Payment id cannot be None.")
        endpoint = '/v1/batches/' + batch_id + '/payments/' + payment_id
        trolley.configuration.Configuration.client(
            self.config).delete(endpoint)
        return True

    """ Lists all payments under a batch.
     This is basically an alias to the search() method. """
    def list_all_payments(self, batch_id):
        return self.search(batch_id)


    """ Search payments within a batch, whose id is provided, with a search term.
     This method returns a generator which auto paginates.
     You can use this generator in a foreach loop to sequentially go through all the 
      search results without needing to call this method again.
       
        For accessing specific pages, check the search_by_page() method. """
    def search(self, batch_id, term=""):
        page = 0
        should_paginate = True
        while should_paginate:
            page+=1
            endpoint = f'/v1/batches/{batch_id}/payments?search={term}'
            params = f'&page={page}&pageSize=10'
            response = trolley.configuration.Configuration.client(self.config).get(endpoint+params)
            yield from self.__build_payments_from_response(response, False)

            if page < response["meta"]["pages"]:
                should_paginate = True
            else:
                should_paginate = False
    
    """ Search payments by providing a page number.
     You should use this function when you want to paginate manually. """
    def search_by_page(self, batch_id, term="", page=1, page_size=10):
        endpoint = f'/v1/batches/{batch_id}/payments?search={term}'
        params = f'&page={page}&pageSize={page_size}'
        
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint+params)
        
        return self.__build_payments_from_response(response, True)
        
    def __build_payments_from_response(self, response, include_meta=False):
        payments = []
        count = 0
        for payment in response['payments']:
            temppayment = trolley.payment.Payment.factory(payment)
            newpayment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
            payments.insert(count, newpayment)
            count = count + 1
        
        if include_meta:
            tempmeta = Meta.factory(response['meta'])
            payments.insert(count,namedtuple("Meta", tempmeta.keys())(*tempmeta.values()))

        return payments
