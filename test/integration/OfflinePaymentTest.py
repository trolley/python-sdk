import sys
import os
import unittest
from pprint import pprint
from TestHelper import TestHelper

sys.path.append(os.path.abspath('.'))

from trolley.exceptions.malformedException import MalformedException
from TestSetup import TestSetup


class OfflinePaymentTest(unittest.TestCase):

    client = None

    def setUp(self):
        self.client = TestSetup.getClient()

    def test_offline_payments(self):
        response = TestHelper.createRecipient()
        recipient_id = response.id

        # Test - Create an offline payment
        offline_payment = self.client.offline_payment.create(recipient_id, 
            {
            "currency":"CAD",
			"amount":"10.00",
			"payoutMethod":"paypal",
			"category":"services",
			"memo":"Python SDK Integration Test Payment",
			"processedAt":"2022-06-22T01:10:17.571Z"
            })

        self.assertEqual(offline_payment.recipientId, recipient_id)

        # Test - Edit an Offline Payment
        offline_payment = self.client.offline_payment.update(offline_payment.id,
            recipient_id, 
            {
            "currency":"CAD",
			"amount":"20.00"
            })

        self.assertEqual(offline_payment.amount, '20.00')

        # Test - Get All Offline Payments
        offline_payments = self.client.offline_payment.get_all()
        val = next(offline_payments)
        self.assertIsNotNone(val)
        
        # Test - Get All Offline Payments by page
        offline_payments = self.client.offline_payment.get_all_by_page(2)
        self.assertTrue(offline_payments[len(offline_payments) - 1].page == 2)

        # Test - Delete an Offline Payment
        response = self.client.offline_payment.delete(recipient_id, offline_payment.id)
        self.assertTrue(response)

        # Cleanup
        response = self.client.recipient.delete(recipient_id)
        self.assertTrue(response)

if __name__ == '__main__':
    unittest.main()
