from collections import namedtuple
from trolley.types.invoice_payment_part import InvoicePaymentPart


class InvoicePayment:

    _attributes = {
        'batchId' : "",
        'paymentId' : "",
        'invoicePayments' : [InvoicePaymentPart]
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            'batchId',
            'paymentId',
            'invoicePayments',
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
