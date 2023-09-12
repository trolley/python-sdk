import sys
import os
import unittest
import uuid
from pprint import pprint

sys.path.append(os.path.abspath('.'))

from trolley.exceptions.malformedException import MalformedException
from TestSetup import TestSetup


class PaymentTest(unittest.TestCase):

    client = None

    def setUp(self):
        self.client = TestSetup.getClient()

    def test_pagination(self):
        payments = self.client.payment.list_all_payments("B-3B2DeZ4hwLcRY3fqpqrSAv")
        value = next(payments)
        self.assertIsNotNone(value)

        payments = self.client.payment.search("B-3B2DeZ4hwLcRY3fqpqrSAv")
        value = next(payments)
        self.assertIsNotNone(value)

        payments = self.client.payment.search_by_page("B-3B2DeZ4hwLcRY3fqpqrSAv","",2)
        self.assertTrue(payments[len(payments) - 1].page == 2)

if __name__ == '__main__':
    unittest.main()
