class RecipientAccount:
    """
    A class representing Recipient Account object.
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
