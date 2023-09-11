from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration
from trolley.types.recipient_account import RecipientAccount


class RecipientAccountGateway(object):
    """
    Trolley RecipientAccount processor
    Creates and manages bank accounts
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    """
        [DEPRECATED] This method has been deprecated and will be removed in future releases.
        Retrieve all the recipient accounts
            A recipient_id is required::
            recipient_account.findAll('R-fjeracjmuflh')
        """
    def findAll(self, recipient_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)

        recipientaccounts = []
        count = 0
        for recipientaccount in response['accounts']:
            recipaccount = RecipientAccount.factory(
                recipientaccount)
            newrecipientaccount = namedtuple(
                "RecipientAccount", recipaccount.keys())(*recipaccount.values())
            recipientaccounts.insert(count, newrecipientaccount)
            count = count + 1
        return recipientaccounts

    """
        Retrieve a recipient account
            A recipient_id and recipient_account_id are required::
            recipient_account.find('R-fjeracjmuflh','A-2DQMpN4jurTFn9gRxobx4C')
        """
    def find(self, recipient_id, recipient_account_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/' + recipient_account_id
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        recipaccount = RecipientAccount.factory(
            response)
        recipientaccount = namedtuple(
            "RecipientAccount", recipaccount.keys())(*recipaccount.values())
        return recipientaccount

    """
        Create a recipient account
            A recipient_id and body are required::
            recipient_account.create('R-4625iLug2GKqKZG2WzAf3e',{"accountHolderName": "Acer" ...})
        """
    def create(self, recipient_id, body):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, body)
        recipaccount = RecipientAccount.factory(
            response)
        recipientaccount = namedtuple(
            "RecipientAccount", recipaccount.keys())(*recipaccount.values())
        return recipientaccount

    """
        Update a recipient account
            A recipient_id, recipient_account_id, and body are required::
            recipient_account.update('R-fjeracjmuflh','A-2DQMpN4jurTFn9gRxobx4C',
            {"accountHolderName": "Acer Philips"})
        """
    def update(self, recipient_id, recipient_account_id, body):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/' + recipient_account_id
        response = trolley.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        recipaccount = RecipientAccount.factory(
            response)
        recipientaccount = namedtuple(
            "RecipientAccount", recipaccount.keys())(*recipaccount.values())
        return recipientaccount

    """
        Delete a recipient account
            A recipient_id and recipient_account_id are required::
            recipient_account.delete('R-fjeracjmuflh','A-2DQMpN4jurTFn9gRxobx4C')
        """
    def delete(self, recipient_id, recipient_account_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = '/v1/recipients/' + recipient_id + '/accounts/' + recipient_account_id
        trolley.configuration.Configuration.client(
            self.config).delete(endpoint)
        return True
