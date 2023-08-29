import sys
import os
import time
import unittest
from pprint import pprint
from TestHelper import TestHelper
from trolley.types.invoice_line import InvoiceLine

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

        # Test - Add lines to Invoice
        invoice_with_lines = self.client.invoice_line.create(invoice.id,[
                {
                    "unitAmount" :{
                        "value" : "50.00",
                        "currency" : "EUR"
                    },
                    "description" 	: "first line",
                    "category"		: InvoiceLine.categories.education
                },
                {
                    "unitAmount" :{
                        "value" : "150.00",
                        "currency" : "EUR"
                    },
                    "description" 	: "second line",
                    "category"		: InvoiceLine.categories.prizes
                }
            ])
        
        self.assertEqual("150.00", invoice_with_lines.lines[1]['unitAmount']['value'])

        # Test - Update lines to Invoice
        invoice_with_lines = self.client.invoice_line.update(invoice.id,[
                {
                    "invoiceLineId"	: invoice_with_lines.lines[1]['id'],
                    "unitAmount" :{
                        "value" : "151.00",
                        "currency" : "EUR"
                    },
                    "category"		: InvoiceLine.categories.refunds
                }
            ])
        
        self.assertEqual("151.00", invoice_with_lines.lines[1]['unitAmount']['value'])
        self.assertEqual(
            InvoiceLine.categories.refunds, 
            invoice_with_lines.lines[1]['category'])

        # Test - Delete an invoice line
        del_result = self.client.invoice_line.delete(
            invoice.id, 
            [
                invoice_with_lines.lines[1]['id']
            ])
        self.assertTrue(del_result)

        # Test - Update Invoice
        ext_id = f"inv-id-{time.time()}"
        invoice = self.client.invoice.update(invoice.id, {
                "externalId": ext_id
            })
        self.assertEqual(invoice.externalId, ext_id)

        # Assert that the deleted line can't be found
        self.assertEqual(len(invoice.lines), 1)
        
        # Test - Get an invoice by id
        fetched_invoice = self.client.invoice.get(invoice.id)
        self.assertEqual(fetched_invoice.externalId, ext_id)

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
