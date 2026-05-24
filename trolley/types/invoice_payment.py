from collections import namedtuple
from trolley.types.invoice_payment_part import InvoicePaymentPart


class InvoicePayment:
    """
    A class representing Invoice Payment object.
    """

    _attributes = {
        'id': "",
        'batchId' : "",
        'paymentId' : "",
        'invoiceId': "",
        'invoiceLineId': "",
        'amount': "",
        'invoicePayments' : [InvoicePaymentPart],
        'status': "",
        'memo': "",
        'externalId': "",
        'tags': "",
        'coverFees': ""
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            'id',
            'batchId',
            'paymentId',
            'invoiceId',
            'invoiceLineId',
            'amount',
            'invoicePayments',
            'status',
            'memo',
            'externalId',
            'tags',
            'coverFees',
        ]
        
        for field in fields:
            if attributes.get('invoicePayment') is None:
                InvoicePayment._attributes[field] = attributes.get(field)
            elif attributes['invoicePayment'].get(field) is not None:

                if field == "invoicePayments":
                    parts = []
                    
                    for part in attributes['invoicePayment'].get(field):
                        temp_part = InvoicePaymentPart.factory(part)
                        parts.append(namedtuple("InvoicePaymentPart", temp_part.keys())(*temp_part.values()))
                    
                    InvoicePayment._attributes[field] = parts
                else:
                    InvoicePayment._attributes[field] = attributes['invoicePayment'][field]

        return InvoicePayment._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Invoice Payment and returns it. """
        instance = InvoicePayment._initialize(attributes)
        return instance
