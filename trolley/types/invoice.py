class Invoice:
    """
    A class representing Invoice object.
    """

    _attributes = {
        'id': "",
        'invoiceNumber': "",
        'description': "",
        'status': "",
        'externalId': "",
        'invoiceDate': "",
        'dueDate': "",
        'createdAt': "",
        'updatedAt': "",
        'totalAmount': "",
        'paidAmount': "",
        'dueAmount': "",
        'tags': "",
        'lines': "",
        'recipientId': ""
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            'id',
            'invoiceNumber',
            'description',
            'status',
            'externalId',
            'invoiceDate',
            'dueDate',
            'createdAt',
            'updatedAt',
            'totalAmount',
            'paidAmount',
            'dueAmount',
            'tags',
            'lines',
            'recipientId'
        ]

        for field in fields:
            if attributes.get('invoice') is None:
                Invoice._attributes[field] = attributes.get(field)
            elif attributes['invoice'].get(field) is not None:
                Invoice._attributes[field] = attributes['invoice'][field]

        return Invoice._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Invoice and returns it. """
        instance = Invoice._initialize(attributes)
        return instance
