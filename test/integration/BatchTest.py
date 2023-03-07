import sys
import os
import unittest
import uuid

sys.path.append(os.path.abspath('.'))

from paymentrails.configuration import Configuration
from paymentrails.recipient import Recipient
from paymentrails.recipient_account import RecipientAccount
from paymentrails.batch import Batch
from paymentrails.payment import Payment


class BatchTest(unittest.TestCase):

    client = None

    def setUp(self):
        self.client = Configuration.gateway("YOUR-API-KEY", "YOUR-API-SECRET", "YOUR-ENVIRONMENT")

    def test_processing(self):
        uuidString = str(uuid.uuid4())
        payload = {"type": "individual", "firstName": "Tom",
                   "lastName": "Jones", "email": "test.create" + uuidString + "@example.com"}
        response = self.client.recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "primary": True, "country": "DE", "currency": "EUR", "iban": "DE89 3704 0044 0532 0130 00"}
        response = self.client.recipient_account.create(recipient_id, payload)

        payload = {"payments": [{"recipient": {
            "id": recipient_id}, "sourceAmount": "65", "memo": "", "sourceCurrency": "EUR"}]}
        response = self.client.batch.create(payload)
        batch_id = response.id

        response = self.client.batch.generate_quote(batch_id)
        self.assertTrue(response.id == batch_id)
        response = self.client.batch.process_batch(batch_id)
        self.assertTrue(response.id == batch_id)

    def test_create_batch(self):
        uuidString = str(uuid.uuid4())
        payload = {"type": "individual", "firstName": "Tom",
                   "lastName": "Jones", "email": "test.create" + uuidString + "@example.com"}
        response = self.client.recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "primary": True, "country": "DE", "currency": "EUR", "iban": "DE89 3704 0044 0532 0130 00"}

        response = self.client.recipient_account.create(recipient_id, payload)

        payload = {"payments": [{"recipient": {
            "id": recipient_id}, "sourceAmount": "65", "memo": "", "sourceCurrency": "EUR"}]}
        response = self.client.batch.create(payload)
        self.assertTrue(response.currency == "CAD")

    def test_delete(self):
        uuidString = str(uuid.uuid4())

        payload = {"type": "individual", "firstName": "Tom",
                   "lastName": "Jones", "email": "test.create" + uuidString + "@example.com"}
        response = self.client.recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "primary": True, "country": "DE", "currency": "EUR", "iban": "DE89 3704 0044 0532 0130 00"}
        response = self.client.recipient_account.create(recipient_id, payload)

        payload = {"payments": [{"recipient": {
            "id": recipient_id}, "sourceAmount": "65", "memo": "", "sourceCurrency": "EUR"}]}
        response = self.client.batch.create(payload)
        batch_id = response.id

        response = self.client.batch.delete(batch_id)
        self.assertTrue(response)

    def test_payment(self):
        uuidString = str(uuid.uuid4())
        payload = {"type": "individual", "firstName": "Tom",
                   "lastName": "Jones", "email": "test.create" + uuidString + "@example.com"}
        response = self.client.recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "primary": True, "country": "DE", "currency": "EUR", "iban": "DE89 3704 0044 0532 0130 00"}
        response = self.client.recipient_account.create(recipient_id, payload)

        payload = {"payments": [{"recipient": {
            "id": recipient_id}, "sourceAmount": "65", "memo": "", "sourceCurrency": "EUR"}]}
        response = self.client.batch.create(payload)
        batch_id = response.id

        payload = {"recipient":{"id": recipient_id},"sourceAmount":"100.10","memo":"Freelance payment"}
        response = self.client.payment.create(payload, batch_id)
        self.assertTrue(response.sourceAmount == '76.08')

if __name__ == '__main__':
    unittest.main()
