from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration

from trolley.types.meta import Meta

class InvoiceLineGateway(object):
    """
    Trolley InvoiceLine processor
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    """ Creates a new InvoiceLine. Only provide the line item in the body, and provide invoiceId separately.  """
    def create(self, invoice_id, body,):
        if invoice_id is None:
            raise InvalidFieldException("Invoice ID cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        if not isinstance(body, list):
            raise InvalidFieldException("Body must be of type list")

        if "invoiceId" in body:
            del body['invoiceId']
        
        payload = {
            'invoiceId' : invoice_id,
            'lines' : body
        }

        endpoint = f'/v1/invoices/create-lines/'
        response = trolley.Configuration.client(
            self.config).post(endpoint, payload)

        temp_invoice = trolley.Invoice.factory(response)
        invoice = namedtuple("Invoice", temp_invoice.keys())(*temp_invoice.values())
        return invoice

    """ Update an Invoice Line. """
    def update(self, invoice_id, body):
        if invoice_id is None:
            raise InvalidFieldException("Invoice ID cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        if not isinstance(body, list):
            raise InvalidFieldException("Body must be of type list")
        
        if "invoiceId" in body:
            del body['invoiceId']
        
        payload = {
            'invoiceId' : invoice_id,
            'lines' : body
        }

        endpoint = f'/v1/invoices/update-lines'
        response = trolley.Configuration.client(
            self.config).post(endpoint, payload)
        temp_invoice = trolley.Invoice.factory(response)
        invoice = namedtuple("Invoice", temp_invoice.keys())(*temp_invoice.values())
        return invoice

    """ Delete Invoice Lines. Provide a list of str in invoice_line_ids """
    def delete(self, invoice_id, invoice_line_ids):
        if invoice_id is None:
            raise InvalidFieldException("Invoice ID cannot be None.")
        if invoice_line_ids is None:
            raise InvalidFieldException("Invoice Line IDs cannot be None.")
        if not isinstance(invoice_line_ids, list):
            raise InvalidFieldException("Invoice Line IDs cannot be None.")
        
        payload = {
            'invoiceId' : invoice_id,
            'invoiceLineIds' : invoice_line_ids
        }

        endpoint = f'/v1/invoices/delete-lines'
        response = trolley.Configuration.client(
            self.config).post(endpoint, payload)

        return response['ok']
