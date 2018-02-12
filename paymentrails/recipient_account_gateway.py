from collections import namedtuple
from paymentrails.exceptions.invalidFieldException import InvalidFieldException
import paymentrails.configuration


class RecipientAccountGateway(object):
    """
    PaymentRails RecipientAccount processor
    Creates and manages bank accounts
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def findAll(self, recipient_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/'
        response = paymentrails.configuration.Configuration.client(
            self.config).get(endpoint)

        recipientaccounts = []
        count = 0
        for recipientaccount in response['accounts']:
            recipaccount = paymentrails.recipient_account.RecipientAccount.factory(
                recipientaccount)
            newrecipientaccount = namedtuple(
                "RecipientAccount", recipaccount.keys())(*recipaccount.values())
            recipientaccounts.insert(count, newrecipientaccount)
            count = count + 1
        return recipientaccounts

    def find(self, recipient_id, recipient_account_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/' + recipient_account_id
        response = paymentrails.configuration.Configuration.client(
            self.config).get(endpoint)
        recipaccount = paymentrails.recipient_account.RecipientAccount.factory(
            response)
        recipientaccount = namedtuple(
            "RecipientAccount", recipaccount.keys())(*recipaccount.values())
        return recipientaccount

    def create(self, recipient_id, body):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts'
        response = paymentrails.configuration.Configuration.client(
            self.config).post(endpoint, body)
        recipaccount = paymentrails.recipient_account.RecipientAccount.factory(
            response)
        recipientaccount = namedtuple(
            "RecipientAccount", recipaccount.keys())(*recipaccount.values())
        return recipientaccount

    def update(self, recipient_id, recipient_account_id, body):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/' + recipient_account_id
        response = paymentrails.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        recipaccount = paymentrails.recipient_account.RecipientAccount.factory(
            response)
        recipientaccount = namedtuple(
            "RecipientAccount", recipaccount.keys())(*recipaccount.values())
        return recipientaccount

    def delete(self, recipient_id, recipient_account_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/' + recipient_account_id
        paymentrails.configuration.Configuration.client(
            self.config).delete(endpoint)
        return True
