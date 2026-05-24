class Verification:
    """
    A class representing a Verification object.
    """

    _attributes = {
        "id": "",
        "type": "",
        "recipientId": "",
        "status": "",
        "createdAt": "",
        "updatedAt": "",
        "submittedAt": "",
        "decisionAt": "",
        "reasonType": "",
        "verifiedData": "",
    }

    @staticmethod
    def _initialize(attributes):
        fields = [
            "id",
            "type",
            "recipientId",
            "status",
            "createdAt",
            "updatedAt",
            "submittedAt",
            "decisionAt",
            "reasonType",
            "verifiedData",
        ]

        for field in fields:
            if attributes.get('verification') is None:
                Verification._attributes[field] = attributes.get(field)
            elif attributes['verification'].get(field) is not None:
                Verification._attributes[field] = attributes['verification'][field]

        return Verification._attributes

    @staticmethod
    def factory(attributes):
        instance = Verification._initialize(attributes)
        return instance
