from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration


class RecipientAccountGateway(object):
    """
    Trolley RecipientAccount processor
    Creates and manages bank accounts
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def findAll(self, recipient_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)

        recipientaccounts = []
        count = 0
        for recipientaccount in response['accounts']:
            recipaccount = trolley.recipient_account.RecipientAccount.factory(
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
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        recipaccount = trolley.recipient_account.RecipientAccount.factory(
            response)
        recipientaccount = namedtuple(
            "RecipientAccount", recipaccount.keys())(*recipaccount.values())
        return recipientaccount

    def create(self, recipient_id, body):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, body)
        recipaccount = trolley.recipient_account.RecipientAccount.factory(
            response)
        recipientaccount = namedtuple(
            "RecipientAccount", recipaccount.keys())(*recipaccount.values())
        return recipientaccount

    def update(self, recipient_id, recipient_account_id, body):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/' + recipient_account_id
        response = trolley.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        recipaccount = trolley.recipient_account.RecipientAccount.factory(
            response)
        recipientaccount = namedtuple(
            "RecipientAccount", recipaccount.keys())(*recipaccount.values())
        return recipientaccount

    def delete(self, recipient_id, recipient_account_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/' + recipient_account_id
        trolley.configuration.Configuration.client(
            self.config).delete(endpoint)
        return True