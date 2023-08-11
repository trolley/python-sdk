import sys
import os

sys.path.append(os.path.abspath('.'))

from TestSetup import TestSetup
import uuid

class TestHelper:

    @staticmethod
    def createRecipient():
        client = TestSetup.getClient()
        uuidString = str(uuid.uuid4())
        payload = {"type": "individual", "firstName": "Tom", "lastName": "Jones",
                   "email": "test.create.pythonsdk" + uuidString + "@example.com",
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
        response = client.recipient.create(payload)
        return response
    
    @staticmethod
    def createRecipientAccount(recipient_id, payload=None):
        client = TestSetup.getClient()
        if payload is None:
            payload = {"type": "bank-transfer", "currency": "EUR",
                   "iban": "DE89 3704 0044 0532 0130 00", "country": "DE"}
        response = client.recipient_account.create(recipient_id, payload)
        return response