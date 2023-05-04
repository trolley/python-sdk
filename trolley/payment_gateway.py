from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration


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
        temppayment = trolley.payment.Payment.factory(response)
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
        temppayment = trolley.payment.Payment.factory(response)
        payment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
        return payment

    def update(self, payment_id, body, batch_id):
        if payment_id is None:
            raise InvalidFieldException("Payment id cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/batches/' + batch_id + '/payments/' + payment_id
        trolley.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        return True

    def delete(self, payment_id, batch_id):
        if payment_id is None:
            raise InvalidFieldException("Payment id cannot be None.")
        endpoint = '/v1/batches/' + batch_id + '/payments/' + payment_id
        trolley.configuration.Configuration.client(
            self.config).delete(endpoint)
        return True
    def search(self, page=1, page_number=10, term=""):
        endpoint = '/v1/batches?search=' + term + \
            '&page=' + str(page) + '&pageSize=' + str(page_number)
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        payments = []
        count = 0
        for payment in response['batches']:
            temppayment = trolley.payment.Payment.factory(payment)
            newpayment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
            payments.insert(count, newpayment)
            count = count + 1
        return payments
