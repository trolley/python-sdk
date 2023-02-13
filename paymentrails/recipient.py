from paymentrails.configuration import Configuration
from paymentrails.gateway import Gateway
class Recipient:
    """
    A class that facilitates Client requests to
    the Trolley API in regards to Recipients.
    """

    _attributes = {
        "id": "",
        "routeType": "",
        "routeMinimum": "",
        "estimatedFees": "",
        "referenceId": "",
        "email": "",
        "name": "",
        "lastName": "",
        "firstName": "",
        "type": "",
        "taxType": "",
        "status": "",
        "language": "",
        "complianceStatus": "",
        "dob": "",
        "passport": "",
        "updatedAt": "",
        "createdAt": "",
        "gravatarUrl": "",
        "governmentId": "",
        "ssn": "",
        "primaryCurrency": "",
        "merchantId": "",
        "payoutMethod": "",
        "compliance": "",
        "accounts": "",
        "address": "",
    }


    @staticmethod
    def find(recipient_id, term=""):
        """
        Retrieve a recipient
            A recipient_id is required::
            Recipient.find('R-fjeracjmuflh')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key, Configuration.enviroment)
        return Gateway(config).recipient.find(recipient_id, term)
    @staticmethod
    def create(body):
        """
        Create a recipient
            A body is required::
            Recipient.create({"type": "individual", "firstName": "John",
                                    "lastName": "Smith", "email": "jh@edxample.com"})
        """
        config = Configuration(Configuration.public_key, Configuration.private_key, Configuration.enviroment)
        return Gateway(config).recipient.create(body)

    @staticmethod
    def update(recipient_id, body):
        """
        Update a recipient
            A recipient_id and body are required::
            Recipient.update({'firstName': 'tom'})
        """
        config = Configuration(Configuration.public_key, Configuration.private_key, Configuration.enviroment)
        return Gateway(config).recipient.update(recipient_id, body)

    @staticmethod
    def delete(recipient_id):
        """
        Delete a recipient
            A recipient_id is required::
            Recipient.delete('R-fjeracjmuflh')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key, Configuration.enviroment)
        return Gateway(config).recipient.delete(recipient_id)

    @staticmethod
    def search(page=1, page_number=10, term=""):
        """
        Query for a recipient
            Recipient.search(1,10,'test')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key, Configuration.enviroment)
        return Gateway(config).recipient.search(page, page_number, term)

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            "id",
            "routeType",
            "routeMinimum",
            "estimatedFees",
            "id",
            "referenceId",
            "email",
            "name",
            "lastName",
            "firstName",
            "type",
            "taxType",
            "status",
            "language",
            "complianceStatus",
            "dob",
            "passport",
            "updatedAt",
            "createdAt",
            "gravatarUrl",
            "governmentId",
            "ssn",
            "primaryCurrency",
            "merchantId",
            "payoutMethod",
            "compliance",       # TODO: Factory
            "accounts",
            "address",          #TODO: Factory
        ]

        for field in fields:
            if attributes.get('recipient') is None:
                Recipient._attributes[field] = attributes.get(field)
            elif attributes['recipient'].get(field) is not None:
                Recipient._attributes[field] = attributes['recipient'][field]

        return Recipient._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Recipient and returns it. """
        instance = Recipient._initialize(attributes)
        return instance
