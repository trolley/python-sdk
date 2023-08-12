import sys
import os
import unittest
from TestHelper import TestHelper

sys.path.append(os.path.abspath('.'))

from trolley.exceptions.malformedException import MalformedException
from TestSetup import TestSetup


class BatchTest(unittest.TestCase):

    client = None

    def setUp(self):
        self.client = TestSetup.getClient()

    def test_pagination(self):
        batches = self.client.batch.list_all_batches()
        value = next(batches)
        self.assertIsNotNone(value)

        batches = self.client.batch.search()
        value = next(batches)
        self.assertIsNotNone(value)

        batches = self.client.batch.search_by_page("",2)
        self.assertTrue(batches[len(batches) - 1].page == 2)

    def test_processing(self):
        # Test - Setup
        response = TestHelper.createRecipient()
        recipient_id = response.id

        payload = {
            "payments": [
                {
                    "recipient": {
                        "id": recipient_id
                    }, 
                    "sourceAmount": "65", 
                    "memo": "", 
                    "sourceCurrency": "EUR"
                    }
                ]
            }
        
        # Test - Create Batch
        response = self.client.batch.create(payload)
        batch_id = response.id
        self.assertTrue("B-" in batch_id)

        try:
            response = self.client.batch.generate_quote(batch_id)
            self.assertTrue(response.id == batch_id)
            
            response = self.client.batch.process_batch(batch_id)
        except MalformedException as e:
            print(e.get_error_array()[0]['message'])
            self.assertTrue(len(e.get_error_array()) > 0)

        self.assertTrue(response.id == batch_id)

        # Cleanup
        r = self.client.recipient.delete(recipient_id)
        self.assertTrue(r)
        r = self.client.batch.delete(batch_id)
        self.assertTrue(r)

    def test_create_batch(self):
        response = TestHelper.createRecipient()
        recipient_id = response.id

        payload = {
            "payments": [
                {
                    "recipient": {
                    "id": recipient_id
                    }, 
                "sourceAmount": "65", 
                "memo": "", 
                "sourceCurrency": "EUR"
                }
            ]
        }

        # Test - Create a Batch
        response = self.client.batch.create(payload)
        self.assertTrue(response.currency == "CAD")

        # Cleanup
        r = self.client.recipient.delete(recipient_id)
        self.assertTrue(r)
        r = self.client.batch.delete(response.id)
        self.assertTrue(r)

    def test_delete(self):
        # Setup
        response = TestHelper.createRecipient()
        recipient_id = response.id

        # Create Batch
        payload = {"payments": [{"recipient": {
            "id": recipient_id}, "sourceAmount": "65", "memo": "", "sourceCurrency": "EUR"}]}
        response = self.client.batch.create(payload)
        batch_id = response.id

        response = self.client.batch.delete(batch_id)
        self.assertTrue(response)

        # Cleanup
        r = self.client.recipient.delete(recipient_id)
        self.assertTrue(r)

    def test_payment(self):
        # Setup - Create a recipient
        response = TestHelper.createRecipient()
        recipient_id = response.id

        # Setup - Create batch
        payload = {
            "payments": [
                {
                "recipient": {
                    "id": recipient_id
                }, 
                "sourceAmount": "65", 
                "memo": "", 
                "sourceCurrency": "EUR"
                }
            ]
        }

        response = self.client.batch.create(payload)
        batch_id = response.id

        # Test - Create payment
        payload = {
            "recipient":{
                "id": recipient_id
            },
            "sourceAmount":"100.10",
            "memo":"Freelance payment"
        }

        response = self.client.payment.create(payload, batch_id)
        self.assertTrue(response.sourceAmount == '70.07')

        # Test - Update the payment
        payload = {
            "sourceAmount":"200.10",
        }
        response = self.client.payment.update(response.id, payload, batch_id)
        self.assertTrue(response.sourceAmount == '140.07')

        # Cleanup
        r = self.client.recipient.delete(recipient_id)
        self.assertTrue(r)
        r = self.client.batch.delete(batch_id)
        self.assertTrue(r)

if __name__ == '__main__':
    unittest.main()
