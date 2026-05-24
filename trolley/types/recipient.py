class Recipient:
    """
    A class representing Recipient object.
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
        "primaryCurrency": "",
        "merchantId": "",
        "payoutMethod": "",
        "tags": "",
        "compliance": "",
        "accounts": "",
        "address": "",
    }

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
            "primaryCurrency",
            "merchantId",
            "payoutMethod",
            "tags",
            "compliance",
            "accounts",
            "address",
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

    @staticmethod
    def find(recipient_id, term=""):
        from trolley.configuration import Configuration
        gateway = Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key())
        if term == "logs":
            return gateway.recipient.retrieve_logs(recipient_id)
        if term == "payments":
            return gateway.recipient.get_all_payments(recipient_id)
        return gateway.recipient.find(recipient_id)

    @staticmethod
    def create(body):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).recipient.create(body)

    @staticmethod
    def update(recipient_id, body):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).recipient.update(recipient_id, body)

    @staticmethod
    def delete(recipient_id):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).recipient.delete(recipient_id)

    @staticmethod
    def search(page=1, page_size=10, term=""):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).recipient.search_by_page(page, page_size, term)
