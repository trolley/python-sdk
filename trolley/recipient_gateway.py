from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration
from trolley.types.meta import Meta
from trolley.utils.url_utils import UrlUtils


class RecipientGateway(object):
    """
    Trolley Recipient processor
    Creates and manages transactions
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def find(self, recipient_id, term=""):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = f'/v1/recipients/{recipient_id}/{term}'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        recip = trolley.Recipient.factory(response)
        recipient = namedtuple("Recipient", recip.keys())(*recip.values())
        count = 0
        for account in recipient.accounts:
            recipient.accounts[count] = namedtuple(
                "RecipientAccount", account.keys())(*account.values())
            count = count + 1
        return recipient

    def create(self, body):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/recipients/'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, body)
        recip = trolley.Recipient.factory(response)
        recipient = namedtuple("Recipient", recip.keys())(*recip.values())
        return recipient

    def update(self, recipient_id, body):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None")
        endpoint = f'/v1/recipients/{recipient_id}'
        trolley.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        return True

    def delete(self, recipient_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = f'/v1/recipients/{recipient_id}'
        trolley.configuration.Configuration.client(
            self.config).delete(endpoint)
        return True
    
    def delete_multiple(self, recipient_ids):
        if recipient_ids is None:
            raise InvalidFieldException("Recipient ids cannot be None.")
        
        endpoint = '/v1/recipients/'
        trolley.configuration.Configuration.client(
            self.config).delete(endpoint, recipient_ids)
        return True

    def retrieve_logs(self, recipient_id, page=1, pageSize=10):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        
        endpoint = f'/v1/recipients/{recipient_id}/logs?page={page}&pageSize={pageSize}'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)

        logs = []
        count = 0
        for log in response['recipientLogs']:
            temp = trolley.Log.factory(log)

            logs.insert(count, namedtuple("Log", temp.keys())(*temp.values()))

            count = count + 1
        
            tempmeta = Meta.factory(response['meta'])
            logs.insert(count,namedtuple("Meta", tempmeta.keys())(*tempmeta.values()))

        return logs
    
    def get_all_payments(self, recipient_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = f'/v1/recipients/{recipient_id}/payments'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        
        payments = []
        count = 0
        for payment in response['payments']:
            temppayment = trolley.Payment.factory(payment)
            newpayment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
            payments.insert(count, newpayment)
            count = count + 1
        
            tempmeta = Meta.factory(response['meta'])
            payments.insert(count,namedtuple("Meta", tempmeta.keys())(*tempmeta.values()))

        return payments

    def get_all_offline_payments(self, recipient_id):
        if recipient_id is None:
            raise InvalidFieldException("Recipient id cannot be None.")
        endpoint = f'/v1/recipients/{recipient_id}/offlinePayments'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        
        offlinePayments = []
        count = 0
        for offlinePayment in response['offlinePayments']:
            temppayment = trolley.Payment.factory(offlinePayment)
            newpayment = namedtuple("Payment", temppayment.keys())(*temppayment.values())
            offlinePayments.insert(count, newpayment)
            count = count + 1
        
            tempmeta = Meta.factory(response['meta'])
            offlinePayments.insert(count,namedtuple("Meta", tempmeta.keys())(*tempmeta.values()))

        return offlinePayments

    """ Search Recipients with a search term.
        This method returns a generator which auto paginates.
        You can use this generator in a foreach loop to sequentially go through all the 
        search results without needing to call this method again.
        
            For accessing specific pages, check the search_by_page() method. """
    def search(self, search=None, name=None, email=None, reference_id=None, start_date=None,
               end_date=None, status=None, compliance_status=None, country=None, payout_method=None, currency=None,
               order_by=None, sort_by=None):
        
        local_vars = UrlUtils.parse(locals())
        
        page = 0
        should_paginate = True
        while should_paginate:
            page+=1
            endpoint = f'/v1/recipients?page={page}&pageSize=10' + (f'&{local_vars}' if(len(local_vars)) else '')
            response = trolley.configuration.Configuration.client(self.config).get(endpoint)
            yield from self.__build_recipients_from_response(response, False)

            if page < response["meta"]["pages"]:
                should_paginate = True
            else:
                should_paginate = False
        
        return self.__build_recipients_from_response(response)
    
    """ Search Recipients by providing a page number.
        This method returns a list.
        You should use this function when you want to paginate manually. """
    def search_by_page(self, page=1, page_size=10, search=None, name=None, email=None, reference_id=None, start_date=None,
               end_date=None, status=None, compliance_status=None, country=None, payout_method=None, currency=None,
               order_by=None, sort_by=None):
        
        endpoint = '/v1/recipients?' + UrlUtils.parse(locals())
        response = trolley.configuration.Configuration.client(self.config).get(endpoint)
        return self.__build_recipients_from_response(response, True)
        
    def __build_recipients_from_response(self, response, include_meta=False):
        recipients = []
        count = 0
        for recipient in response['recipients']:
            temp = trolley.recipient.Recipient.factory(recipient)

            recipient = namedtuple("Recipient", temp.keys())(*temp.values())
            recipients.insert(count, recipient)

            count = count + 1
        
        if include_meta:
            tempmeta = Meta.factory(response['meta'])
            recipients.insert(count,namedtuple("Meta", tempmeta.keys())(*tempmeta.values()))

        return recipients
