class Batch:
    """
    A class that facilitates Client requests to
    the Trolley API in regards to Batches.
    """

    _attributes = {
        "id": "",
        "amount": "",
        "completedAt": "",
        "createdAt": "",
        "currency": "",
        "description": "",
        "sentAt": "",
        "status": "",
        "tags": "",
        "totalPayments": "",
        "updatedAt": "",
        "quoteExpiredAt": "",
        "payments": "",
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""
        fields = [
            "id",
            "amount",
            "completedAt",
            "createdAt",
            "currency",
            "description",
            "sentAt",
            "status",
            "tags",
            "totalPayments",
            "updatedAt",
            "quoteExpiredAt",
            "payments",
        ]

        for field in fields:
            if attributes.get('batch') is None:
                Batch._attributes[field] = attributes.get(field)
            elif attributes['batch'].get(field) is not None:
                Batch._attributes[field] = attributes['batch'][field]

        return Batch._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Batch and returns it. """
        instance = Batch._initialize(attributes)
        return instance
