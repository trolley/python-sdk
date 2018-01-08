import sys
import os
import unittest

sys.path.append(os.path.abspath('.'))

from paymentrails.configuration import Configuration
from paymentrails.recipient import Recipient
from paymentrails.recipient_account import RecipientAccount
from paymentrails.batch import Batch
from paymentrails.payment import Payment


class BatchTest(unittest.TestCase):

    public_key = ("public_key")
    private_key = ("private_key")

    def test_processing(self):
        Configuration.set_public_key(BatchTest.public_key)
        Configuration.set_private_key(BatchTest.private_key)

        payload = {"type": "individual", "firstName": "John",
                   "lastName": "Smith", "email": "pr13@example.com"}
        response = Recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "primary": "true", "country": "CA", "currency": "USD",
                   "accountNum": "604542847", "bankId": "123", "branchId": "47261",  "accountHolderName": "John Smith"}
        response = RecipientAccount.create(recipient_id, payload)

        payload = {"payments": [{"recipient": {
            "id": recipient_id}, "sourceAmount": "65", "memo": "", "sourceCurrency": "USD"}]}
        response = Batch.create(payload)
        batch_id = response.id

        response = Batch.generate_quote(batch_id)
        self.assertTrue(response.id == batch_id)
        response = Batch.process_batch(batch_id)
        self.assertTrue(response.id == batch_id)

    def test_create_batch(self):
        Configuration.set_public_key(BatchTest.public_key)
        Configuration.set_private_key(BatchTest.private_key)

        payload = {"type": "individual", "firstName": "John",
                   "lastName": "Smith", "email": "prtest17@example.com"}
        response = Recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "primary": "true", "country": "CA", "currency": "USD",
                   "accountNum": "604542847", "bankId": "123", "branchId": "47261",  "accountHolderName": "John Smith"}
        response = RecipientAccount.create(recipient_id, payload)

        payload = {"payments": [{"recipient": {
            "id": recipient_id}, "sourceAmount": "65", "memo": "", "sourceCurrency": "USD"}]}
        response = Batch.create(payload)
        self.assertTrue(response.currency == "USD")

    def test_delete(self):
        Configuration.set_public_key(BatchTest.public_key)
        Configuration.set_private_key(BatchTest.private_key)

        payload = {"type": "individual", "firstName": "John",
                   "lastName": "Smith", "email": "pr19@example.coms"}
        response = Recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "primary": "true", "country": "CA", "currency": "USD",
                   "accountNum": "604542847", "bankId": "123", "branchId": "47261",  "accountHolderName": "John Smith"}
        response = RecipientAccount.create(recipient_id, payload)

        payload = {"payments": [{"recipient": {
            "id": recipient_id}, "sourceAmount": "65", "memo": "", "sourceCurrency": "USD"}]}
        response = Batch.create(payload)
        batch_id = response.id

        response = Batch.delete(batch_id)
        self.assertTrue(response)

    def test_payment(self):
        Configuration.set_public_key(BatchTest.public_key)
        Configuration.set_private_key(BatchTest.private_key)

        payload = {"type": "individual", "firstName": "John",
                   "lastName": "Smith", "email": "pr21@example.com"}
        response = Recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "primary": "true", "country": "CA", "currency": "USD",
                   "accountNum": "604542847", "bankId": "123", "branchId": "47261",  "accountHolderName": "John Smith"}
        response = RecipientAccount.create(recipient_id, payload)

        payload = {"payments": [{"recipient": {
            "id": recipient_id}, "sourceAmount": "65", "memo": "", "sourceCurrency": "USD"}]}
        response = Batch.create(payload)
        batch_id = response.id

        payload = {"recipient":{"id": recipient_id},"sourceAmount":"100.10","memo":"Freelance payment"}
        response = Payment.create(payload, batch_id)
        self.assertTrue(response.sourceAmount == '100.10')

if __name__ == '__main__':
    unittest.main()
