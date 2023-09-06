class InvoicePaymentPart:

    _attributes = {
        'invoiceId' : "",
        'invoiceLineId' : "",
        'paymentId' : "",
        'amount' : ""
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            'invoiceId',
            'invoiceLineId',
            'paymentId',
            'amount'
        ]

        for field in fields:
            if attributes.get(field) is not None:
                InvoicePaymentPart._attributes[field] = attributes.get(field)

        return InvoicePaymentPart._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Payment Part and returns it. """
        instance = InvoicePaymentPart._initialize(attributes)
        return instance
