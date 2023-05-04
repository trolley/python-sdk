from collections import namedtuple
from trolley.exceptions.invalidFieldException import InvalidFieldException
import trolley.configuration



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
    def search(self, page=1, pagenumber=10, term=""):
        endpoint = '/v1/batches?search=' + term + \
            '&page=' + str(page) + '&pageSize=' + str(pagenumber)
        response = trolley.configuration.Configuration.client(
            self.config).get(endpoint)
        batches = []
        count = 0
        for batch in response['batches']:
            tempbatch = trolley.batch.Batch.factory(batch)
            newbatch = namedtuple("Batch", tempbatch.keys())(*tempbatch.values())
            batches.insert(count, newbatch)
            count = count + 1
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