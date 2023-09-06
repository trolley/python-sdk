import sys
import os
import time
import unittest
from TestHelper import TestHelper
from trolley.exceptions.notFoundException import NotFoundException
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
                        "value" : "250.00",
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

        # Test - Create Invoice Payment with multiple Invoices
        invoice2 = self.client.invoice.create({
            "recipientId": recipient.id,
            "description": "Python SDK integration test 2",
            "lines": [
                    {
                        "unitAmount" :{
                            "value" : "50.00",
                            "currency" : "EUR"
                        },
                        "description" 	: "first line",
                        "category"		: InvoiceLine.categories.education
                    }
                ]
            })
        
        invoice_payment = self.client.invoice_payment.create([
            {
                "invoiceId": invoice.id,
                "amount":{
                    "value":"11.00",
                    "currency":"EUR"
                }
            },
            {
                "invoiceId": invoice2.id,
                "amount":{
                    "value":"10.00",
                    "currency":"EUR"
                }
            }
        ])
        self.assertEqual(invoice_payment.invoicePayments[0].invoiceId, invoice2.id)

        # Test - Update Invoice Payment
        update_payment = self.client.invoice_payment.update(
            {
                "invoiceId": invoice2.id,
                "invoiceLineId": invoice2.lines[0]['id'],
                "paymentId": invoice_payment.paymentId,
                "amount":{
                    "value":"21.00",
                    "currency":"EUR"
                }
            }
        )
        self.assertTrue(update_payment)

        # Test - Search for Invoice Payments
        invoice_payments = self.client.invoice_payment.search([invoice_payment.paymentId])
        self.assertTrue(
            (invoice_payments[0].invoiceId == invoice_with_lines.id) 
            or 
            (invoice_payments[0].invoiceId == invoice2.id))

        # Test - Delete Invoice Payment
        del_inv_payment = self.client.invoice_payment.delete(invoice_payment.paymentId, [
            invoice_with_lines.lines[0]['id']
        ])
        self.assertTrue(del_inv_payment)

        # Assert that the payment was deleted and can't be found anymore
        find_payment = self.client.invoice_payment.search([invoice_payment.paymentId])
        self.assertNotEqual(find_payment[0].invoiceLineId, invoice_with_lines.lines[0]['id'])

        # Test - Update Invoice
        ext_id = f"inv-id-{time.time()}"
        invoice = self.client.invoice.update(invoice.id, {
                "externalId": ext_id
            })
        self.assertEqual(invoice.externalId, ext_id)

        # Additionally, assert that line item deleted earlier isn't present
        for line in invoice.lines:
            self.assertNotEqual(invoice_with_lines.lines[1]['id'], line['id'])
        
        # Test - Get an invoice by id
        fetched_invoice = self.client.invoice.get(invoice.id)
        self.assertEqual(fetched_invoice.externalId, ext_id)

        # Test - Delete an Invoice
        response = self.client.invoice.delete([
            f'{invoice.id}',
            f'{invoice2.id}'
        ])
        
        # Assert that the deleted invoice is not found anymore
        try:
            find_invoice = self.client.invoice.get(invoice.id)
        except NotFoundException as e:
            self.assertEqual(e.get_error_array()[0]['code'],'not_found')

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
