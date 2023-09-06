import sys
import os
import unittest
import uuid

sys.path.append(os.path.abspath('.'))

from trolley.configuration import Configuration
from trolley.recipient import Recipient
from trolley.recipient_account import RecipientAccount
from TestSetup import TestSetup
from TestHelper import TestHelper
from trolley.exceptions.malformedException import MalformedException

class RecipientTest(unittest.TestCase):

    client = None

    def setUp(self):
        self.client = TestSetup.getClient()
    
    def test_search_and_pagination(self):
        
        recipients = self.client.recipient.search_by_page()
        self.assertIsNotNone(recipients)

        recipients = self.client.recipient.search()
        value = next(recipients)
        self.assertIsNotNone(value)

    def test_lifecycle(self):
        # Test - Create Recipient
        response = TestHelper.createRecipient()

        self.assertTrue(response.name == "Tom Jones")
        self.assertTrue(response.type == "individual")
        self.assertTrue(response.lastName == "Jones")

        recipient_id = response.id

        # Test - Update Recipient
        response = self.client.recipient.update(
            recipient_id,  {"firstName": "Jon"})

        self.assertTrue(response)

        # Test - Delete Recipient
        response = self.client.recipient.delete(recipient_id)
        self.assertTrue(response)

        # Test - Delete Multiple Recipients
        recipient1 = TestHelper.createRecipient()
        self.assertTrue(recipient1)

        recipient2 = TestHelper.createRecipient()
        self.assertTrue(recipient2)

        payload = {
            "ids": [
                recipient1.id,
                recipient2.id
                ]
            }
        response = self.client.recipient.delete_multiple(payload)
        self.assertTrue(response)

        # Test - Find Recipient
        response = self.client.recipient.find(recipient_id)
        self.assertTrue(response.status == "archived")

    def test_account(self):
        # Setup
        response = TestHelper.createRecipient()
        recipient_id = response.id

        # Test - Create Recipient Accounts
        response = TestHelper.createRecipientAccount(recipient_id)
        account_id1 = response.id
        self.assertTrue(account_id1, "Account1 ID not found")
        
        payload = {"type": "bank-transfer", "currency": "EUR",
                   "iban": "FR14 2004 1010 0505 0001 3M02 606", "country": "FR", "primary": False}
        response = TestHelper.createRecipientAccount(recipient_id, payload)
        account_id2 = response.id
        self.assertTrue(account_id2, "Account2 ID not found")

        # Test - Delete Recipient Account
        response = self.client.recipient_account.delete(recipient_id, account_id1)
        self.assertTrue(response,"Recipient Not Deleted")
        
        # Test - Find Recipient Account
        response = self.client.recipient_account.find(
            recipient_id, account_id2)
        self.assertEqual(response.id, account_id2, "Search result doesn't match with the Test Account created")

        # Test - Update Recipient Account
        response = self.client.recipient_account.update(recipient_id, account_id2, {"primary": True})
        self.assertTrue(response.primary, "Account country not updated")

        # Cleanup
        response = self.client.recipient.delete(recipient_id)
        self.assertTrue(response)

    def test_routeMinimum(self):
        # Setup - Create recipient
        response = TestHelper.createRecipient()
        recipient_id = response.id
        
        self.assertTrue(response.routeType == "sepa")
        self.assertTrue(response.routeMinimum == "3")

        # Cleanup
        response = self.client.recipient.delete(recipient_id)
        self.assertTrue(response)

    def test_recipient_payments(self):
        payments = self.client.recipient.get_all_payments("R-91XPCK1J9W1HU")
        self.assertTrue(len(payments)>0)

        offlinePayments = self.client.recipient.get_all_offline_payments("R-4QoXiSPjbnLuUmQR2bgb8C")
        self.assertTrue(len(offlinePayments)>0)

if __name__ == '__main__':
    unittest.main()
