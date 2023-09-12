from collections import namedtuple
import trolley.configuration
from trolley.exceptions.invalidFieldException import InvalidFieldException
from trolley.types.batch import Batch
from trolley.types.batch_summary import BatchSummary
from trolley.types.meta import Meta

class BatchGateway(object):
    """
    Trolley Batch processor
    Creates and manages batches
    """

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = config

    """
        Retrieve a batch
            A batch_id is required::
            Batch.find('B-fjeracjmuflh')
        """
    def find(self, batchid):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batchid
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        tempbatch = Batch.factory(response)
        batch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
        return batch

    """
    Create a batch
        A body is required::
        Batch.create(
            {"payments":[{"recipient":{"id":"R-SBAHDK3DK6M7SUEM"},
            "sourceAmount":"65","memo":"","sourceCurrency":"CAD"}]})
    """
    def create(self, body):
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/batches/'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, body)
        tempbatch = Batch.factory(response)
        batch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
        return batch

    """
        Update a batch
            A batch_id and body are required::
            Batch.update('B-fjeracjmuflh',{"payments":[{"recipient":{"id":"R-3DF7FAF680739541",
            "email":"jsmith@example.com"},"sourceAmount":65,"memo":"Salary",
            "sourceCurrency":"CAD"}]})
        """
    def update(self, batchid, body):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        if body is None:
            raise InvalidFieldException("Body cannot be None.")
        endpoint = '/v1/batches/' + batchid
        trolley.configuration.Configuration.client(
            self.config).patch(endpoint, body)
        return True

    """
        Delete a batch
            A batch_id is required::
            batch.delete('B-fjeracjmuflh')
        """
    def delete(self, batchid):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batchid
        trolley.configuration.Configuration.client(
            self.config).delete(endpoint)
        return True
    
    """
        Delete multiple batches
            A list of batch ids is required::
            batch.delete([
                'B-fjeracjmuflh',
                'B-fjeracabclh'
            ])
        """
    def delete_multiple(self, batchids):
        if batchids is None:
            raise InvalidFieldException("Batch IDs cannot be None.")
        endpoint = '/v1/batches/'
        trolley.configuration.Configuration.client(
            self.config).delete(endpoint, batchids)
        return True
    
    """ Lists all payments under a batch.
     This is basically an alias to the search() method. """
    def list_all_batches(self):
        return self.search()

    """ Search for a batch with a search term.
     This method returns a generator which auto paginates.
     You can use this generator in a foreach loop to sequentially go through all the 
      search results without needing to call this method again.
       
        For accessing specific pages, check the search_by_page() method. 
        
        batch.search('term')"""
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
     You should use this function when you want to paginate manually.
      batch.search_by_page('term', 1, 10) """
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
            tempbatch = Batch.factory(batch)
            newbatch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
            batches.insert(count, newbatch)
            count = count + 1
        
        if include_meta:
            tempmeta = Meta.factory(response['meta'])
            batches.insert(count,namedtuple("Meta", tempmeta.keys())(*tempmeta.values()))
            
        return batches

    """
        Retrieve a summary about a specific batch
            A batch_id is required::
            batch.summary('B-fjeracjmuflh')
        """
    def summary(self, batchid):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batchid + '/summary'
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        tempbatchsummary = BatchSummary.factory(
            response)
        batchsummary = namedtuple("BatchSummary", tempbatchsummary.keys())(
            *tempbatchsummary.values())
        return batchsummary

    """
        Generate a quote for a batch
            A batch_id is required::
            batch.generate_quote('B-fjeracjmuflh')
        """
    def generate_quote(self, batchid):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batchid + '/generate-quote'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, {})
        tempbatch = Batch.factory(response)
        batch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
        return batch

    """
        Process a batch
            A batch_id is required::
            batch.process_batch('B-fjeracjmuflh')
        """
    def process_batch(self, batchid):
        if batchid is None:
            raise InvalidFieldException("Batch id cannot be None.")
        endpoint = '/v1/batches/' + batchid + '/start-processing'
        response = trolley.configuration.Configuration.client(
            self.config).post(endpoint, {})
        tempbatch = Batch.factory(response)
        batch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
        return batch
