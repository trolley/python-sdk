import sys
import os
import unittest

sys.path.append(os.path.abspath('.'))

import trolley.configuration
import trolley.payment
from mock import MagicMock, Mock, patch


import trolley.exceptions.notFoundException
import trolley.exceptions.invalidFieldException


def fake_find(paymentId,batchId,term=""):
    if paymentId == None:
        raise  trolley.exceptions.invalidFieldException.InvalidFieldException("Payment id cannot be None")
    if paymentId[0:1] != "P":
        raise trolley.exceptions.notFoundException.NotFoundException("Payment id is invalid")
    if batchId == None:
        raise  trolley.exceptions.invalidFieldException.InvalidFieldException("Batch id cannot be None")
    if batchId[0:1] != "B":
        raise trolley.exceptions.notFoundException.NotFoundException("Batch id is invalid")
    return {"ok":"true","payment":{"id":"P-91XQ40VT54GQM","recipient":{"id":"R-91XQ0PJH39U54","referenceId":"U345678912","email":"Johnny@test.com","name":"mark Test","lastName":"Test","firstName":"mark","type":"individual","status":"active","language":"en","complianceStatus":"pending","dob":"null","payoutMethod":"paypal","updatedAt":"2017-05-08T14:49:12.512Z","createdAt":"2017-05-04T16:17:04.378Z","gravatarUrl":"https://s3.amazonaws.com/static.api.trolley.com/icon_user.svg","compliance":{"status":"pending","checkedAt":"null"},"payout":{"autoswitch":{"limit":1000,"active":"false"},"holdup":{"limit":1000,"active":"false"},"primary":{"method":"paypal","currency":{"currency":{}}},"method":"paypal","accounts":{"paypal":{"address":"testpaypal@example.com"}},"methodDisplay":"PayPal"},"address":{"street1":"null","street2":"null","city":"null","postalCode":"null","country":"null","region":"null","phone":"null"}},"status":"pending","sourceAmount":"900.90","exchangeRate":"1.000000","fees":"0.00","recipientFees":"0.00","targetAmount":"65.00","fxRate":"2.000000","memo":"","processedAt":"null","createdAt":"2017-05-08T18:30:45.012Z","updatedAt":"2017-05-12T18:39:06.061Z","merchantFees":"0.00","compliance":{"status":"pending","checkedAt":"null"},"sourceCurrency":"USD","sourceCurrencyName":"US Dollar","targetCurrency":"USD","targetCurrencyName":"US Dollar","batch":{"id":"B-91XQ40VT5HF18","createdAt":"2017-05-08T18:30:44.905Z","updatedAt":"2017-05-12T18:39:06.125Z","sentAt":"null","completedAt":"null"}}}
def fake_update(paymentId,batchId, body):
    if paymentId == None:
        raise  trolley.exceptions.invalidFieldException.InvalidFieldException("Payment id cannot be None")
    if batchId == None:
        raise  trolley.exceptions.invalidFieldException.InvalidFieldException("Batch id cannot be None")
    if batchId[0:1] != "B":
        raise trolley.exceptions.notFoundException.NotFoundException("Batch id is invalid")
    if paymentId[0:1] != "P":
        raise trolley.exceptions.notFoundException.NotFoundException("Payment id is invalid")
    if body == None:
        raise  trolley.exceptions.invalidFieldException.InvalidFieldException("Body cannot be None")
    return {"ok": "true", "object": "updated"}

def fake_create(body,batchId):
    if batchId == None:
        raise  trolley.exceptions.invalidFieldException.InvalidFieldException("Batch id cannot be None")
    if body == None:
        raise  trolley.exceptions.invalidFieldException.InvalidFieldException("Body is invalid")
    if batchId[0:1] != "B":
        raise trolley.exceptions.notFoundException.NotFoundException("Batch Id is invalid")
    return {"ok": "true"}

def fake_delete(paymentId,batchId):
    if paymentId == None:
        raise  trolley.exceptions.invalidFieldException.InvalidFieldException("Payment id cannot be None")
    if batchId == None:
        raise  trolley.exceptions.invalidFieldException.InvalidFieldException("Batch id cannot be None")
    if batchId[0:1] != "B":
        raise trolley.exceptions.notFoundException.NotFoundException("Batch id is invalid")
    if paymentId[0:1] != "P":
        raise trolley.exceptions.notFoundException.NotFoundException("Payment id is invalid")
    return {"ok": "true", "object": "deleted"}

def fake_search(page,pageSize,term):
    if term == None:
        raise  trolley.exceptions.invalidFieldException.InvalidFieldException("Term cannot be None")
    return {"ok":"true","payments":[{"id":"P-912Q8JUA75HNC","recipient":{"id":"R-91XQ0PJH39U54","referenceId":"U345678912","email":"Johnny@test.com","name":"mark Test","lastName":"Test","firstName":"mark","type":"individual","status":"active","language":"en","complianceStatus":"pending","dob":"null","payoutMethod":"paypal","updatedAt":"2017-05-08T14:49:12.512Z","createdAt":"2017-05-04T16:17:04.378Z","gravatarUrl":"https://s3.amazonaws.com/static.api.trolley.com/icon_user.svg","compliance":{"status":"pending","checkedAt":"null"},"payout":{"autoswitch":{"limit":1000,"active":"false"},"holdup":{"limit":1000,"active":"false"},"primary":{"method":"paypal","currency":{"currency":{}}},"method":"paypal","accounts":{"paypal":{"address":"testpaypal@example.com"}},"methodDisplay":"PayPal"},"address":{"street1":"null","street2":"null","city":"null","postalCode":"null","country":"null","region":"null","phone":"null"}},"status":"pending","sourceAmount":"15.00","exchangeRate":"1.000000","fees":"0.00","recipientFees":"0.00","targetAmount":"65.00","fxRate":"2.000000","memo":"","processedAt":"null","createdAt":"2017-05-08T17:18:16.948Z","updatedAt":"2017-05-11T19:05:53.172Z","merchantFees":"0.00","compliance":{"status":"pending","checkedAt":"null"},"sourceCurrency":"USD","sourceCurrencyName":"US Dollar","targetCurrency":"USD","targetCurrencyName":"US Dollar","batch":{"id":"B-91XQ2ZHXARPJE","createdAt":"2017-05-08T17:18:16.893Z","updatedAt":"2017-05-11T19:05:53.265Z","sentAt":"null","completedAt":"null"}}],"meta":{"page":1,"pages":1,"records":1}}

class TestPayment(unittest.TestCase):

    public_key = ("public_key")
    private_key = ("private_key")

    @patch('paymentrails.payment.Payment.find', fake_find)
    def test_retrieve_payment(self):
        trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
        trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
        batchId = "B-912Q61G0BRVGC"
        response = trolley.payment.Payment.find('P-91XQ0U0B1RW5M',batchId)
        status = {"ok":"true","payment":{"id":"P-91XQ40VT54GQM","recipient":{"id":"R-91XQ0PJH39U54","referenceId":"U345678912","email":"Johnny@test.com","name":"mark Test","lastName":"Test","firstName":"mark","type":"individual","status":"active","language":"en","complianceStatus":"pending","dob":"null","payoutMethod":"paypal","updatedAt":"2017-05-08T14:49:12.512Z","createdAt":"2017-05-04T16:17:04.378Z","gravatarUrl":"https://s3.amazonaws.com/static.api.trolley.com/icon_user.svg","compliance":{"status":"pending","checkedAt":"null"},"payout":{"autoswitch":{"limit":1000,"active":"false"},"holdup":{"limit":1000,"active":"false"},"primary":{"method":"paypal","currency":{"currency":{}}},"method":"paypal","accounts":{"paypal":{"address":"testpaypal@example.com"}},"methodDisplay":"PayPal"},"address":{"street1":"null","street2":"null","city":"null","postalCode":"null","country":"null","region":"null","phone":"null"}},"status":"pending","sourceAmount":"900.90","exchangeRate":"1.000000","fees":"0.00","recipientFees":"0.00","targetAmount":"65.00","fxRate":"2.000000","memo":"","processedAt":"null","createdAt":"2017-05-08T18:30:45.012Z","updatedAt":"2017-05-12T18:39:06.061Z","merchantFees":"0.00","compliance":{"status":"pending","checkedAt":"null"},"sourceCurrency":"USD","sourceCurrencyName":"US Dollar","targetCurrency":"USD","targetCurrencyName":"US Dollar","batch":{"id":"B-91XQ40VT5HF18","createdAt":"2017-05-08T18:30:44.905Z","updatedAt":"2017-05-12T18:39:06.125Z","sentAt":"null","completedAt":"null"}}}
        self.assertEqual(response, status)

    @patch('paymentrails.payment.Payment.find', fake_find)
    def test_retrieve_payment_InvalidPaymentId(self):
        with self.assertRaises(trolley.exceptions.notFoundException.NotFoundException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            batchId = "B-912Q61G0BRVGC"
            response = trolley.payment.Payment.find('wdwdwd',batchId)

    @patch('paymentrails.payment.Payment.find', fake_find)
    def test_retrieve_payment_InvalidBatchId(self):
        with self.assertRaises(trolley.exceptions.notFoundException.NotFoundException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            batchId = "wwdwdwd"
            response = trolley.payment.Payment.find('P-91XQ0U0B1RW5M',batchId)
    @patch('paymentrails.payment.Payment.find', fake_find)
    def test_retrieve_payment_None_Batch(self):
        with self.assertRaises( trolley.exceptions.invalidFieldException.InvalidFieldException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            response = trolley.payment.Payment.find('P-91XQ0U0B1RW5M',None)
    @patch('paymentrails.payment.Payment.find', fake_find)
    def test_retrieve_payment_None_Payment(self):
        with self.assertRaises( trolley.exceptions.invalidFieldException.InvalidFieldException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            response = trolley.payment.Payment.find(None,"B-hghgh")

    @patch('paymentrails.payment.Payment.create', fake_create)
    def test_create_payment(self):
        trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
        trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
        body = {"payments": [{"recipient": {"id": "R-91XPYX3V2MM1G"},
                              "sourceAmount": "65", "memo": "", "sourceCurrency": "CAD"}]}
        batchId = "B-912Q61G0BRVGC"
        response = trolley.payment.Payment.create(body,batchId)
        status = {"ok": "true"}
        self.assertEqual(response, status)

    @patch('paymentrails.payment.Payment.create', fake_create)
    def test_create_payment_InvalidBatchId(self):
        with self.assertRaises(trolley.exceptions.notFoundException.NotFoundException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            body = {"payments": [{"recipient": {"id": "R-91XPYX3V2MM1G"},
                                  "sourceAmount": "65", "memo": "", "sourceCurrency": "CAD"}]}
            batchId = "dddd"
            response = trolley.payment.Payment.create(body,batchId)

    @patch('paymentrails.payment.Payment.create', fake_create)
    def test_create_payment_None_body(self):
        with self.assertRaises( trolley.exceptions.invalidFieldException.InvalidFieldException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            batchId = "B-dddd"
            response = trolley.payment.Payment.create(None,batchId)
            
    @patch('paymentrails.payment.Payment.create', fake_create)
    def test_create_payment_None_batch(self):
        with self.assertRaises( trolley.exceptions.invalidFieldException.InvalidFieldException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            body = {"payments": [{"recipient": {"id": "R-91XPYX3V2MM1G"},
                                  "sourceAmount": "65", "memo": "", "sourceCurrency": "CAD"}]}
            response = trolley.payment.Payment.create(body,None)

    @patch('paymentrails.payment.Payment.update', fake_update)
    def test_update_payment(self):
        trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
        trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
        body = {"sourceAmount": "900.90"}
        batchId = "B-912Q61G0BRVGC"
        response = trolley.payment.Payment.update("P-91XQ0U0B1RW5M",batchId, body)
        status = {"ok": "true", "object": "updated"}
        self.assertEqual(response, status)

    @patch('paymentrails.payment.Payment.update', fake_update)
    def test_update_payment_InvalidBatchId(self):
        with self.assertRaises(trolley.exceptions.notFoundException.NotFoundException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            body = {"sourceAmount": "900.90"}
            batchId = "dddd"
            response = trolley.payment.Payment.update("P-91XQ0U0B1RW5M",batchId, body)

    @patch('paymentrails.payment.Payment.update', fake_update)
    def test_update_payment_InvalidPaymentId(self):
        with self.assertRaises(trolley.exceptions.notFoundException.NotFoundException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            body = {"sourceAmount": "900.90"}
            batchId = "B-912Q61G0BRVGC"
            response = trolley.payment.Payment.update("ddd",batchId, body)

    @patch('paymentrails.payment.Payment.update', fake_update)
    def test_update_payment_None_body(self):
        with self.assertRaises( trolley.exceptions.invalidFieldException.InvalidFieldException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            batchId = "B-dddd"
            response = trolley.payment.Payment.update("P-91XQ0U0B1RW5M",batchId, None)

    @patch('paymentrails.payment.Payment.update', fake_update)
    def test_update_payment_None_payment(self):
        with self.assertRaises( trolley.exceptions.invalidFieldException.InvalidFieldException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            body = {"sourceAmount": "900.90"}
            batchId = "dddd"
            response = trolley.payment.Payment.update(None,batchId, body)
    @patch('paymentrails.payment.Payment.update', fake_update)
    def test_update_payment_None_batch(self):
        with self.assertRaises( trolley.exceptions.invalidFieldException.InvalidFieldException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            body = {"sourceAmount": "900.90"}
            response = trolley.payment.Payment.update("P-91XQ0U0B1RW5M",None, body)
    @patch('paymentrails.payment.Payment.delete', fake_delete)
    def test_delete_payment(self):
        trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
        trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
        batchId = "B-912Q61G0BRVGC"
        response = trolley.payment.Payment.delete('P-912Q61G06TT6A',batchId)
        status = {"ok": "true", "object": "deleted"}
        self.assertEqual(response, status)

    @patch('paymentrails.payment.Payment.delete', fake_delete)
    def test_delete_payment_InvalidBatchId(self):
        with self.assertRaises(trolley.exceptions.notFoundException.NotFoundException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            batchId = "ffff"
            response = trolley.payment.Payment.delete('P-912Q61G06TT6A',batchId)
    @patch('paymentrails.payment.Payment.delete', fake_delete)
    def test_delete_payment_None_payment(self):
        with self.assertRaises( trolley.exceptions.invalidFieldException.InvalidFieldException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            batchId = "B-ffff"
            response = trolley.payment.Payment.delete(None,batchId)
    @patch('paymentrails.payment.Payment.delete', fake_delete)
    def test_delete_payment_None_batch(self):
        with self.assertRaises( trolley.exceptions.invalidFieldException.InvalidFieldException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            response = trolley.payment.Payment.delete("P-fhfh",None)

    @patch('paymentrails.payment.Payment.delete', fake_delete)
    def test_delete_payment_InvalidPaymentId(self):
        with self.assertRaises(trolley.exceptions.notFoundException.NotFoundException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            batchId = "B-912Q61G0BRVGC"
            response = trolley.payment.Payment.delete('fffff',batchId)
    

    @patch('paymentrails.payment.Payment.search',fake_search)
    def test_list_allPaymentsWithQueries(self):
        trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
        trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
        response = trolley.payment.Payment.search(1, 10, "hnc")
        status = {"ok":"true","payments":[{"id":"P-912Q8JUA75HNC","recipient":{"id":"R-91XQ0PJH39U54","referenceId":"U345678912","email":"Johnny@test.com","name":"mark Test","lastName":"Test","firstName":"mark","type":"individual","status":"active","language":"en","complianceStatus":"pending","dob":"null","payoutMethod":"paypal","updatedAt":"2017-05-08T14:49:12.512Z","createdAt":"2017-05-04T16:17:04.378Z","gravatarUrl":"https://s3.amazonaws.com/static.api.trolley.com/icon_user.svg","compliance":{"status":"pending","checkedAt":"null"},"payout":{"autoswitch":{"limit":1000,"active":"false"},"holdup":{"limit":1000,"active":"false"},"primary":{"method":"paypal","currency":{"currency":{}}},"method":"paypal","accounts":{"paypal":{"address":"testpaypal@example.com"}},"methodDisplay":"PayPal"},"address":{"street1":"null","street2":"null","city":"null","postalCode":"null","country":"null","region":"null","phone":"null"}},"status":"pending","sourceAmount":"15.00","exchangeRate":"1.000000","fees":"0.00","recipientFees":"0.00","targetAmount":"65.00","fxRate":"2.000000","memo":"","processedAt":"null","createdAt":"2017-05-08T17:18:16.948Z","updatedAt":"2017-05-11T19:05:53.172Z","merchantFees":"0.00","compliance":{"status":"pending","checkedAt":"null"},"sourceCurrency":"USD","sourceCurrencyName":"US Dollar","targetCurrency":"USD","targetCurrencyName":"US Dollar","batch":{"id":"B-91XQ2ZHXARPJE","createdAt":"2017-05-08T17:18:16.893Z","updatedAt":"2017-05-11T19:05:53.265Z","sentAt":"null","completedAt":"null"}}],"meta":{"page":1,"pages":1,"records":1}}
        self.assertEqual(response, status)

    @patch('paymentrails.payment.Payment.search',fake_search)
    def test_list_allPayments_None_body(self):
        with self.assertRaises( trolley.exceptions.invalidFieldException.InvalidFieldException):
            trolley.configuration.Configuration.set_public_key(TestPayment.public_key)
            trolley.configuration.Configuration.set_private_key(TestPayment.private_key)
            response = trolley.payment.Payment.search(1, 10, None)



if __name__ == '__main__':
    unittest.main()
