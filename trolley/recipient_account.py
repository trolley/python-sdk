from trolley.configuration import Configuration
from trolley.gateway import Gateway

class RecipientAccount:
    """
    A class that facilitates Client requests to
    the Trolley API in regards to Recipient Accounts.
    """

    _attributes = {
        "id": "",
        "primary": "",
        "currency": "",
        "recipientAccountId": "",
        "routeType": "",
        "recipientFees": "",
        "emailAddress": "",
        "country": "",
        "type": "",
        "iban": "",
        "accountNum": "",
        "accountHolderName": "",
        "swiftBic": "",
        "branchId": "",
        "bankId": "",
        "bankName": "",
        "bankAddress": "",
        "bankCity": "",
        "bankRegionCode": "",
        "bankPostalCode": ""
    }

    @staticmethod
    def findAll(recipient_id):
        """
        Retrieve all the recipient accounts
            A recipient_id is required::
            RecipientAccount.findAll('R-fjeracjmuflh')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key)
        return Gateway(config).recipient_account.findAll(recipient_id)

    @staticmethod
    def find(recipient_id, recipient_account_id):
        """
        Retrieve a recipient account
            A recipient_id and recipient_account_id are required::
            RecipientAccount.find('R-fjeracjmuflh','A-2DQMpN4jurTFn9gRxobx4C')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key)
        return Gateway(config).recipient_account.find(recipient_id, recipient_account_id)
       
    @staticmethod
    def create(recipient_id, body):
        """
        Create a recipient account
            A recipient_id and body are required::
            RecipientAccount.create('R-4625iLug2GKqKZG2WzAf3e','payload')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key)
        return Gateway(config).recipient_account.create(recipient_id, body)

    @staticmethod
    def update(recipient_id, recipient_account_id, body):
        """
        Update a recipient account
            A recipient_id, recipient_account_id, and body are required::
            RecipientAccount.update('R-fjeracjmuflh','A-2DQMpN4jurTFn9gRxobx4C',
            {"accountHolderName": "Acer Philips"})
        """
        config = Configuration(Configuration.public_key, Configuration.private_key)
        return Gateway(config).recipient_account.update(recipient_id,
                                                                recipient_account_id, body)

    @staticmethod
    def delete(recipient_id, recipient_account_id):
        """
        Delete a recipient account
            A recipient_id and recipient_account_id are required::
            RecipientAccount.delete('R-fjeracjmuflh','A-2DQMpN4jurTFn9gRxobx4C')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key)
        return Gateway(config).recipient_account.delete(recipient_id, recipient_account_id)

    @staticmethod
    def _initialize(attributes):
        fields = [
            "id",
            "primary",
            "currency",
            "recipientAccountId",
            "routeType",
            "recipientFees",
            "emailAddress",
            "country",
            "type",
            "iban",
            "accountNum",
            "accountHolderName",
            "swiftBic",
            "branchId",
            "bankId",
            "bankName",
            "bankAddress",
            "bankCity",
            "bankRegionCode",
            "bankPostalCode",
        ]

        for field in fields:
            if attributes.get('account') is None:
                RecipientAccount._attributes[field] = attributes.get(field)
            elif attributes.get('account') is not None:
                RecipientAccount._attributes[field] = attributes['account'].get(field)

        return RecipientAccount._attributes

    @staticmethod
    def factory(attributes):
        instance = RecipientAccount._initialize(attributes)
        return instance
