
class BatchSummary:
    """
    A class that facilitates Client requests to
    the PaymentRails API in regards to Batches.
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
        "totalPayments": "",
        "updatedAt": "",
        "methods": "",
    }

    @staticmethod
    def _initialize(attributes):
        fields = [
            "id",
            "amount",
            "completedAt",
            "createdAt",
            "currency",
            "description",
            "sentAt",
            "status",
            "totalPayments",
            "updatedAt",
            "methods",
        ]

        for field in fields:
            if attributes.get('batchSummary') is not None:
                BatchSummary._attributes[field] = attributes['batchSummary'].get(field)

        return BatchSummary._attributes

    @staticmethod
    def factory(attributes):
        instance = BatchSummary._initialize(attributes)
        return instance
