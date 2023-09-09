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
        "ssn": "",
        "primaryCurrency": "",
        "merchantId": "",
        "payoutMethod": "",
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
            "ssn",
            "primaryCurrency",
            "merchantId",
            "payoutMethod",
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
