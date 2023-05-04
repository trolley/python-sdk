import sys
import os
import unittest
import uuid

sys.path.append(os.path.abspath('.'))

from trolley.configuration import Configuration
from trolley.recipient import Recipient
from trolley.recipient_account import RecipientAccount
from TestSetup import TestSetup


class RecipientTest(unittest.TestCase):

    client = None

    def setUp(self):
        self.client = TestSetup.getClient()
    
    def test_lifecycle(self):
        uuidString = str(uuid.uuid4())
        payload = {"type": "individual", "firstName": "Tom", "lastName": "Jones",
                   "email": "test.create" + uuidString + "@example.com"}
        response = self.client.recipient.create(payload)

        self.assertTrue(response.name == "Tom Jones")
        self.assertTrue(response.type == "individual")
        self.assertTrue(response.email == "test.create" +
                        uuidString + "@example.com")
        self.assertTrue(response.lastName == "Jones")

        recipient_id = response.id

        response = self.client.recipient.update(
            recipient_id,  {"firstName": "Jon"})

        self.assertTrue(response)

        response = self.client.recipient.delete(recipient_id)
        self.assertTrue(response)

        response = self.client.recipient.find(recipient_id)
        self.assertTrue(response.status == "archived")

    def test_account(self):
        uuidString = str(uuid.uuid4())
        payload = {"type": "individual", "firstName": "Tom", "lastName": "Jones",
                   "email": "test.create" + uuidString + "@example.com"}
        response = self.client.recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "currency": "EUR",
                   "iban": "DE89 3704 0044 0532 0130 00", "country": "DE"}
        response = self.client.recipient_account.create(recipient_id, payload)
        account_id1 = response.id

        payload = {"type": "bank-transfer", "currency": "EUR",
                   "iban": "FR14 2004 1010 0505 0001 3M02 606", "country": "FR"}
        response = self.client.recipient_account.create(recipient_id, payload)
        account_id2 = response.id

        response = self.client.recipient_account.delete(
            recipient_id, account_id2)
        self.assertTrue(response, True)

        response = self.client.recipient_account.find(
            recipient_id, account_id1)
        self.assertTrue(response.id, account_id1)

    def test_routeMinimum(self):
        uuidString = str(uuid.uuid4())
        payload = {"type": "individual", "firstName": "Tom", "lastName": "Jones",
                   "email": "test.create" + uuidString + "@example.com",
                   "address": {
                        "street1": '123 Wolfstrasse',
                        "city": 'Berlin',
                        "country": 'DE',
                        "postalCode": '123123'
                    },
                   "account": {
                        "type": "bank-transfer", "currency": "EUR",
                        "iban": "DE89 3704 0044 0532 0130 00", "country": "DE"}
                        }
        response = self.client.recipient.create(payload)
        recipient_id = response.id
        
        self.assertTrue(response.routeType == "sepa")
        self.assertTrue(response.routeMinimum == "3")

        response = self.client.recipient.delete(recipient_id)
        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()
