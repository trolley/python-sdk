from collections import namedtuple
from paymentrails.exceptions.invalidFieldException import InvalidFieldException
import paymentrails.configuration

class RecipientGateway(object):
    """
    PaymentRails Recipient processor
    Creates and manages transactions
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def find(self, recipient_id, term):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/' + term
        response = paymentrails.configuration.Configuration.client(
            self.config).get(endpoint)
        recip = paymentrails.recipient.Recipient.factory(response)
        recipient = namedtuple("Recipient", recip.keys())(*recip.values())
        count = 0
        for account in recipient.accounts:
            recipient.accounts[count] = namedtuple(
                "RecipientAccount", account.keys())(*account.values())
            count = count + 1
        return recipient

    def create(self, body):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/recipients/'
        response = paymentrails.configuration.Configuration.client(
            self.config).post(endpoint, body)
        recip = paymentrails.recipient.Recipient.factory(response)
        recipient = namedtuple("Recipient", recip.keys())(*recip.values())
        return recipient

    def update(self, recipient_id, body):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None")
        endpoint = '/v1/recipients/' + recipient_id
        response = paymentrails.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        if response['ok'] is True:
            return True
        return False

    def delete(self, recipient_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id
        response = paymentrails.configuration.Configuration.client(
            self.config).delete(endpoint)
        if response['ok'] is True:
            return True
        return False

    def search(self, page, page_number, term):
        endpoint = '/v1/recipients?search=' + term + '&page=' + \
            str(page) + '&pageSize=' + str(page_number)
        response = paymentrails.configuration.Configuration.client(
            self.config).get(endpoint)
        recipients = []
        count = 0
        for recipient in response['recipients']:
            temp = paymentrails.recipient.Recipient.factory(recipient)

            recipient = namedtuple("Recipient", temp.keys())(*temp.values())
            recipients.insert(count, recipient)

            count = count + 1
        return recipients
