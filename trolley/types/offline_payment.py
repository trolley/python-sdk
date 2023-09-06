class OfflinePayment:

    _attributes = {
        'id': "",
        'recipientId': "",
        'amount': "",
        'currency': "",
        'withholdingAmount': "",
        'withholdingCurrency': "",
        'equivalentWithholdingAmount': "",
        'equivalentWithholdingCurrency': "",
        'externalId': "",
        'memo': "",
        'tags': "",
        'category': "",
        'processedAt': "",
        'enteredAmount': "",
        'updatedAt': "",
        'createdAt': "",
        'deletedAt': ""
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            'id',
            'recipientId',
            'amount',
            'currency',
            'withholdingAmount',
            'withholdingCurrency',
            'equivalentWithholdingAmount',
            'equivalentWithholdingCurrency',
            'externalId',
            'memo',
            'tags',
            'category',
            'processedAt',
            'enteredAmount',
            'updatedAt',
            'createdAt',
            'deletedAt'
        ]

        for field in fields:
            if attributes.get('offlinePayment') is None:
                OfflinePayment._attributes[field] = attributes.get(field)
            elif attributes['offlinePayment'].get(field) is not None:
                OfflinePayment._attributes[field] = attributes['offlinePayment'][field]

        return OfflinePayment._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Payment and returns it. """
        instance = OfflinePayment._initialize(attributes)
        return instance
