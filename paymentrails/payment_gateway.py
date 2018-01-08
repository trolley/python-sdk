from collections import namedtuple
from paymentrails.exceptions.invalidFieldException import InvalidFieldException
import paymentrails.configuration


class PaymentGateway(object):
    """
    PaymentRails Payment processor
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
        response = paymentrails.configuration.Configuration.client(
            self.config).get(endpoint)
        temppayment = paymentrails.payment.Payment.factory(response)
        payment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
        return payment

    def create(self, body, batch_id):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/batches/' + batch_id + '/payments/'
        response = paymentrails.configuration.Configuration.client(
            self.config).post(endpoint, body)
        temppayment = paymentrails.payment.Payment.factory(response)
        payment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
        return payment

    def update(self, payment_id, body, batch_id):
        if payment_id is None:
            raise InvalidFieldException("Payment id cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/batches/' + batch_id + '/payments/' + payment_id
        response = paymentrails.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        if response['ok'] is True:
            return True
        return False

    def delete(self, payment_id, batch_id):
        if payment_id is None:
            raise InvalidFieldException("Payment id cannot be None.")
        endpoint = '/v1/batches/' + batch_id + '/payments/' + payment_id
        response = paymentrails.configuration.Configuration.client(
            self.config).delete(endpoint)
        if response['ok'] is True:
            return True
        return False

    def search(self, page=1, page_number=10, term=""):
        endpoint = '/v1/batches?search=' + term + \
            '&page=' + str(page) + '&pageSize=' + str(page_number)
        response = paymentrails.configuration.Configuration.client(
            self.config).get(endpoint)
        payments = []
        count = 0
        for payment in response['batches']:
            temppayment = paymentrails.payment.Payment.factory(payment)
            newpayment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
            payments.insert(count, newpayment)
            count = count + 1
        return payments
