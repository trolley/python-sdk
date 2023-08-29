from enum import Enum

class InvoicePayment:

    _attributes = {
        # 'id' : "",
        # 'status' : "",
        # 'unitAmount' : "",
        # 'taxAmount' : "",
        # 'totalAmount' : "",
        # 'dueAmount' : "",
        # 'paidAmount' : "",
        # 'category' : "",
        # 'royalties' : "",
        # 'description' : "",
        # 'externalId' : "",
        # 'taxReportable' : "",
        # 'forceUsTaxActivity' : "",
        # 'tags' : ""
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            # 'id',
            # 'status',
            # 'unitAmount',
            # 'taxAmount',
            # 'totalAmount',
            # 'dueAmount',
            # 'paidAmount',
            # 'category',
            # 'royalties',
            # 'description',
            # 'externalId',
            # 'taxReportable',
            # 'forceUsTaxActivity',
            # 'tags'
        ]

        for field in fields:
            if attributes.get('invoicePayment') is None:
                InvoicePayment._attributes[field] = attributes.get(field)
            elif attributes['invoicePayment'].get(field) is not None:
                InvoicePayment._attributes[field] = attributes['invoicePayment'][field]

        return InvoicePayment._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Payment and returns it. """
        instance = InvoicePayment._initialize(attributes)
        return instance
