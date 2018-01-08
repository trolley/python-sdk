import sys
import os
import unittest

sys.path.append(os.path.abspath('.'))

from paymentrails.configuration import Configuration
from paymentrails.recipient import Recipient
from paymentrails.recipient_account import RecipientAccount


class RecipientTest(unittest.TestCase):

    public_key = ("public_key")
    private_key = ("private_key")

    def test_lifecycle(self):
        Configuration.set_public_key(RecipientTest.public_key)
        Configuration.set_private_key(RecipientTest.private_key)
        payload = {"type": "individual", "firstName": "John",
                   "lastName": "Smith", "email": "pr@example.com"}
        response = Recipient.create(payload)

        self.assertTrue(response.name == "John Smith")
        self.assertTrue(response.type == "individual")
        self.assertTrue(response.email == "pr@example.com")
        self.assertTrue(response.lastName == "Smith")
        
        recipient_id = response.id

        response = Recipient.update(recipient_id,  {"firstName": "Jon"})

        self.assertTrue(response)

        response = Recipient.delete(recipient_id)
        self.assertTrue(response)

        response = Recipient.find(recipient_id)
        self.assertTrue(response.status == "archived")

    def test_account(self):
        Configuration.set_public_key(RecipientTest.public_key)
        Configuration.set_private_key(RecipientTest.private_key)

        payload = {"type": "individual", "firstName": "John",
               "lastName": "Smith", "email": "pr2@example.com"}
        response = Recipient.create(payload)
        recipient_id = response.id

        payload = {"type": "bank-transfer", "primary": "true", "country": "CA", "currency": "CAD",
           "accountNum": "604542847", "bankId": "123", "branchId": "47261",  "accountHolderName": "John Smith"}
        response = RecipientAccount.create(recipient_id, payload)
        account_id1 = response.id

        payload = {"type": "bank-transfer", "primary": "true", "country": "CA", "currency": "CAD",
           "accountNum": "604542847", "bankId": "123", "branchId": "47261",  "accountHolderName": "John Smith"}
        response = RecipientAccount.create(recipient_id, payload)
        account_id2 = response.id

        RecipientAccount.delete(recipient_id, account_id2)

        response = RecipientAccount.find(recipient_id, account_id1)
        self.assertTrue(response.id)

if __name__ == '__main__':
    unittest.main()
