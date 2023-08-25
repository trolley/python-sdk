import sys
import os
import unittest
from TestHelper import TestHelper

sys.path.append(os.path.abspath('.'))

from trolley.exceptions.malformedException import MalformedException
from TestSetup import TestSetup


class InvoiceTest(unittest.TestCase):

    client = None

    def setUp(self):
        self.client = TestSetup.getClient()

    def test_invoice(self):
        # Setup - Create Recipient
        recipient = TestHelper.createRecipient()

        # Test - Create Invoice
        invoice = self.client.invoice.create({
            "recipientId": recipient.id,
            "description": "Python SDK integration test"
            })
        self.assertEqual(invoice.recipientId, recipient.id)

        # Test - Update Invoice
        invoice = self.client.invoice.update(invoice.id, {
                "externalId": "123"
            })
        self.assertEqual(invoice.externalId, "123")
        
        # Test - Get an invoice by id
        fetched_invoice = self.client.invoice.get(invoice.id)
        self.assertEqual(fetched_invoice.externalId, "123")

        # Test - Delete an Invoice
        response = self.client.invoice.delete([
            f'{invoice.id}'
        ])

        # Test - Search invoices
        invoices = self.client.invoice.search({
            "externalIds": [
                f"{fetched_invoice.externalId}"
            ]
        })

        value = next(invoices)
        self.assertIsNotNone(value)
        
        # Cleanup - Delete Recipient
        response = self.client.recipient.delete(recipient.id)
        self.assertTrue(response)

if __name__ == '__main__':
    unittest.main()
