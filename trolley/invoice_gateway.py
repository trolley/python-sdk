from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration

from trolley.types.meta import Meta

class InvoiceGateway(object):
    """
    Trolley Invoice processor
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    """ Create a new Invoice """
    def create(self, body,):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = f'/v1/invoices/create'
        response = trolley.Configuration.client(
            self.config).post(endpoint, body)

        temp_invoice = trolley.Invoice.factory(response)
        invoice = namedtuple("Invoice", temp_invoice.keys())(*temp_invoice.values())
        return invoice

    """ Update an Invoice. """
    def update(self, invoice_id, body):
        if invoice_id is None:
            raise InvalidFieldException("Invoice ID cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        body["invoiceId"] = invoice_id
        endpoint = f'/v1/invoices/update'
        response = trolley.Configuration.client(
            self.config).post(endpoint, body)
        temp_invoice = trolley.Invoice.factory(response)
        invoice = namedtuple("Invoice", temp_invoice.keys())(*temp_invoice.values())
        return invoice

    """ Get details of an invoice whose ID is provided."""
    def get(self, invoice_id):
        if invoice_id is None:
            raise InvalidFieldException("Invoice ID cannot be None.")
        endpoint = f'/v1/invoices/get'
        response = trolley.Configuration.client(
            self.config).post(endpoint, {
                "invoiceId": invoice_id
            })

        temp_invoice = trolley.Invoice.factory(response)
        invoice = namedtuple("Invoice", temp_invoice.keys())(*temp_invoice.values())
        return invoice

    """ Search through invoices. This method auto paginates.
    If you want to paginate manually, use search_by_page() method instead.
      If you added pagination parameters in the body, they'll be ignored. """
    def search(self, body):
        page = 0
        should_paginate = True
        if "page" in body:
            del body['page']
        
        if "pageSize" in body:
            del body['pageSize']
        
        while should_paginate:
            page+=1
            endpoint = f'/v1/invoices/search'
            body['page'] = page

            response = trolley.Configuration.client(self.config).post(endpoint, body)
            yield from self.__build_invoice_from_response(response, False)

            if page < response["meta"]["pages"]:
                should_paginate = True
            else:
                should_paginate = False

    """ Search through invoices. This method paginates manually.
    If you want to auto paginate, use search() method instead.
      If you added pagination parameters in the body, they'll be ignored. Provide them as method parameter instead."""
    def search_by_page(self, body, page=1, pageSize=10):
        if "page" in body:
            del body['page']
        
        if "pageSize" in body:
            del body['pageSize']

        endpoint = f'/v1/invoices/search'
        body['page'] = page
        body['pageSize'] = pageSize

        response = trolley.Configuration.client(self.config).post(endpoint, body)
        return self.__build_invoice_from_response(response, True)

    """ Delete an Invoice """
    def delete(self, invoice_ids):
        if invoice_ids is None:
            raise InvalidFieldException("Body cannot be None.")
        
        body = {
            "invoiceIds": invoice_ids
        }

        endpoint = f'/v1/invoices/delete'
        response = trolley.Configuration.client(
            self.config).post(endpoint, body)

        return response['ok']
        
    def __build_invoice_from_response(self, response, include_meta=False):
        invoices = []
        count = 0
        for invoice in response['invoices']:
            tempinvoice = trolley.Invoice.factory(invoice)
            newinvoice = namedtuple("Invoice", tempinvoice.keys())(*tempinvoice.values())
            invoices.insert(count, newinvoice)
            count = count + 1
        
        if include_meta:
            temp_meta = Meta.factory(response['meta'])
            invoices.insert(count,namedtuple("Meta", temp_meta.keys())(*temp_meta.values()))

        return invoices
