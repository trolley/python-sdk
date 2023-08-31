from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration

from trolley.types.meta import Meta

class InvoicePaymentGateway(object):
    """
    Trolley Invoice Payment processor
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    """ Creates a new Invoice Payment.  """
    def create(self, body):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        if not isinstance(body, list):
            raise InvalidFieldException("Body must be of type list")
        
        payload = {
            'ids' : body
        }

        endpoint = f'/v1/invoices/payment/create'
        response = trolley.Configuration.client(
            self.config).post(endpoint, payload)

        temp_invoice_payment = trolley.InvoicePayment.factory(response)
        invoice = namedtuple("InvoicePayment", temp_invoice_payment.keys())(*temp_invoice_payment.values())
        return invoice

    """ Update an Invoice Payment. """
    def update(self, body):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")

        endpoint = f'/v1/invoices/payment/update'
        response = trolley.Configuration.client(
            self.config).post(endpoint, body)

        return response['ok']

    """ Remove the association between a payment and an invoice.
    Provide a list of str in invoice_line_ids """
    def delete(self, payment_id, invoice_line_ids):
        if payment_id is None:
            raise InvalidFieldException("Payment ID cannot be None.")
        if invoice_line_ids is None:
            raise InvalidFieldException("Invoice Line IDs cannot be None.")
        if not isinstance(invoice_line_ids, list):
            raise InvalidFieldException("Invoice Line IDs must be of type list.")
        
        payload = {
            'paymentId' : payment_id,
            'invoiceLineIds' : invoice_line_ids
        }

        endpoint = f'/v1/invoices/payment/delete'
        response = trolley.Configuration.client(
            self.config).post(endpoint, payload)

        return response['ok']
    
    """ Search for Invoice Payments. Provide a list of str of payment or invoice IDs in the argument ids """
    def search(self, invoice_payment_ids):
        if invoice_payment_ids is None:
            raise InvalidFieldException("Invoice Payment IDs cannot be None.")
        if not isinstance(invoice_payment_ids, list):
            raise InvalidFieldException("Invoice Payment IDs has to be of type list.")
        
        payload = {
            'paymentIds' : invoice_payment_ids
        }

        endpoint = f'/v1/invoices/payment/search'
        response = trolley.Configuration.client(
            self.config).post(endpoint, payload)
        
        invoice_payments = []
                    
        for part in response['invoicePayments']:
            temp_part = trolley.InvoicePaymentPart.factory(part)
            invoice_payments.append(namedtuple("InvoicePaymentPart", temp_part.keys())(*temp_part.values()))
        
        return invoice_payments
