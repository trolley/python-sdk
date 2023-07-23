from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration
from trolley.utils.meta import Meta



class BatchGateway(object):
    """
    Trolley Batch processor
    Creates and manages batches
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    def find(self, batchid):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batchid
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        tempbatch = trolley.batch.Batch.factory(response)
        batch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
        return batch

    def create(self, body):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/batches/'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, body)
        tempbatch = trolley.batch.Batch.factory(response)
        batch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
        return batch

    def update(self, batchid, body):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/batches/' + batchid
        trolley.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        return True

    def delete(self, batchid):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batchid
        trolley.configuration.Configuration.client(
            self.config).delete(endpoint)
        return True
    
    """ Lists all payments under a batch.
     This is basically an alias to the search() method. """
    def list_all_batches(self):
        return self.search()

    """ Search for a batch with a search term.
     This method returns a generator which auto paginates.
     You can use this generator in a foreach loop to sequentially go through all the 
      search results without needing to call this method again.
       
        For accessing specific pages, check the search_by_page() method. """
    def search(self, term=""):
        page = 0
        should_paginate = True
        while should_paginate:
            page+=1
            endpoint = f'/v1/batches/?search={term}'
            params = f'&page={page}&pageSize=10'
            response = trolley.configuration.Configuration.client(self.config).get(endpoint+params)
            yield from self.__build_batches_from_response(response, False)

            if page < response["meta"]["pages"]:
                should_paginate = True
            else:
                should_paginate = False

    """ Search batches by providing a page number.
     You should use this function when you want to paginate manually. """
    def search_by_page(self, term="", page=1, page_size=10):
        endpoint = f'/v1/batches?search={term}'
        params = f'&page={page}&pageSize={page_size}'

        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint+params)
        
        return self.__build_batches_from_response(response, True)
        
    
    def __build_batches_from_response(self, response, include_meta=False):
        batches = []
        count = 0
        for batch in response['batches']:
            tempbatch = trolley.batch.Batch.factory(batch)
            newbatch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
            batches.insert(count, newbatch)
            count = count + 1
        
        if include_meta:
            tempmeta = Meta.factory(response['meta'])
            batches.insert(count,namedtuple("Meta", tempmeta.keys())(*tempmeta.values()))
            
        return batches

    def summary(self, batchid):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batchid + '/summary'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        tempbatchsummary = trolley.batch_summary.BatchSummary.factory(
            response)
        batchsummary = namedtuple("BatchSummary", tempbatchsummary.keys())(
            *tempbatchsummary.values())
        return batchsummary

    def generate_quote(self, batchid):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batchid + '/generate-quote'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, {})
        tempbatch = trolley.batch.Batch.factory(response)
        batch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
        return batch

    def process_batch(self, batchid):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batchid + '/start-processing'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, {})
        tempbatch = trolley.batch.Batch.factory(response)
        batch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
        return batch
