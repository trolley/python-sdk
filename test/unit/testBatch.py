import sys
import os
import unittest

sys.path.append(os.path.abspath('.'))

import paymentrails.configuration
import paymentrails.batch
from mock import MagicMock, Mock, patch

import paymentrails.exceptions.notFoundException
import paymentrails.exceptions.invalidFieldException


def fake_find(batchId):
    if batchId == None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Batch id cannot be None")
    if batchId[0:1] != "B":
        raise paymentrails.exceptions.notFoundException.NotFoundException("Batch id is invalid")
    return {"ok":"true","batch":{"id":"B-912Q61G0BRVGC","status":"open","amount":"999.00","totalPayments":1,"currency":"USD","description":"Weekly Payouts on 2017-4-4","sentAt":"null","completedAt":"null","createdAt":"2017-05-04T19:19:38.049Z","updatedAt":"2017-05-15T16:38:21.552Z","payments":{"payments":[{"id":"P-91XQ0U0B1RW5M","recipient":{"id":"R-91XPYX3V2MM1G","referenceId":"jsmith@exafmple.com","email":"jsmith@exafmple.com","name":"John Smith","status":"archived","countryCode":"null"},"method":"paypal","methodDisplay":"PayPal","status":"pending","sourceAmount":"999.00","targetAmount":"100.10","isSupplyPayment":"false","memo":"Do something amazing!","fees":"0.00","recipientFees":"0.00","exchangeRate":"1.000000","processedAt":"null","merchantFees":"0.00","sourceCurrency":"USD","sourceCurrencyName":"US Dollar","targetCurrency":"USD","targetCurrencyName":"US Dollar","compliance":{"status":"pending","checkedAt":"null"}}],"meta":{"page":1,"pages":1,"records":1}}}}
def fake_update(batchId, body):
    if batchId == None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Batch id cannot be None")
    if batchId[0:1] != "B":
        raise paymentrails.exceptions.notFoundException.NotFoundException("Batch id is invalid")
    if body == None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Body cannot be None")
    return {"ok": "true", "object": "updated"}

def fake_create(body):
    if body == None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Body is invalid")
    return {"ok": "true"}

def fake_delete(batchId):
    if batchId == None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Batch id cannot be None")
    if batchId[0:1] != "B":
        raise paymentrails.exceptions.notFoundException.NotFoundException("Batch id is invalid")
    return {"ok": "true", "object": "deleted"}

def fake_search(page,pageSize,term):
    if term == None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Term cannot be None")
    return {"ok":"true","batches":[{"id":"B-91XQ40VT5HF18","status":"open","amount":"900.90","totalPayments":1,"currency":"USD","description":"Weekly Payouts on 2017-4-8","sentAt":"null","completedAt":"null","createdAt":"2017-05-08T18:30:44.905Z","updatedAt":"2017-05-12T18:39:06.125Z"}],"meta":{"page":1,"pages":1,"records":1}}
def fake_summary(batchId):

    if batchId == None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Batch id cannot be None")
    if batchId[0:1] != "B":
        raise paymentrails.exceptions.notFoundException.NotFoundException("Batch id is invalid")
    return {"ok":"true","batchSummary":{"id":"B-91XQ40VT5HF18","serverTime":"2017-05-16T13:34:52.026Z","status":"open","currency":"USD","description":"Weekly Payouts on 2017-4-8","sentAt":"null","completedAt":"null","createdAt":"2017-05-08T18:30:44.905Z","processed_by":"API","updatedAt":"2017-05-12T18:39:06.125Z","quoteExpiredAt":"null","errors":[],"methods":{"paypal":{"count":1,"value":900.9,"fees":0,"recipientFees":0,"merchantFees":0,"net":900.9,"accountType":"Gateway","displayName":"PayPal"},"bank-transfer":{"count":0,"value":0,"fees":0,"recipientFees":0,"merchantFees":0,"net":0,"accountType":"PaymentRails","displayName":"Bank Transfer"}},"PaymentRailsTotal":{"count":0,"value":0,"fees":0,"recipientFees":0,"merchantFees":0,"net":0},"GatewayTotal":{"count":1,"value":900.9,"fees":0,"recipientFees":0,"merchantFees":0,"net":900.9},"total":{"count":1,"value":900.9,"fees":0,"recipientFees":0,"merchantFees":0,"net":900.9},"merchantBalances":{"GatewayTotal":0,"PaymentRailsTotal":10000},"enoughFunds":"true"}}
def fake_process_batch(batchId):
    if batchId == None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Batch id cannot be None")
    if batchId[0:1] != "B":
        raise paymentrails.exceptions.notFoundException.NotFoundException("Batch id is invalid")
    return {"ok":"true","batch":{"id":"B-91XQ40VT5HF18","status":"processing","amount":"900.90","totalPayments":1,"currency":"USD","description":"Weekly Payouts on 2017-4-8","sentAt":"2017-05-16T13:41:56.149Z","completedAt":"null","createdAt":"2017-05-08T18:30:44.905Z","updatedAt":"2017-05-16T13:41:56.150Z"}}
def fake_generate_quote(batchId):
    if batchId == None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Batch id cannot be None")
    if batchId[0:1] != "B":
        raise paymentrails.exceptions.notFoundException.NotFoundException("Batch id is invalid")
    return {"ok":"true","batch":{"id":"B-91XQ40VT5HF18","status":"open","amount":"900.90","totalPayments":"1","currency":"USD","description":"Weekly Payouts on 2017-4-8","sentAt":"null","completedAt":"null","createdAt":"2017-05-08T18:30:44.905Z","updatedAt":"2017-05-16T13:40:08.098Z"}}
class TestBatch(unittest.TestCase):

    public_key = ("public_key")
    private_key = ("private_key")

    @patch('paymentrails.batch.Batch.find',fake_find)
    def test_retrieve_batch(self):
        paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
        response = paymentrails.batch.Batch.find("B-912Q61G0BRVGC")
        status = {"ok":"true","batch":{"id":"B-912Q61G0BRVGC","status":"open","amount":"999.00","totalPayments":1,"currency":"USD","description":"Weekly Payouts on 2017-4-4","sentAt":"null","completedAt":"null","createdAt":"2017-05-04T19:19:38.049Z","updatedAt":"2017-05-15T16:38:21.552Z","payments":{"payments":[{"id":"P-91XQ0U0B1RW5M","recipient":{"id":"R-91XPYX3V2MM1G","referenceId":"jsmith@exafmple.com","email":"jsmith@exafmple.com","name":"John Smith","status":"archived","countryCode":"null"},"method":"paypal","methodDisplay":"PayPal","status":"pending","sourceAmount":"999.00","targetAmount":"100.10","isSupplyPayment":"false","memo":"Do something amazing!","fees":"0.00","recipientFees":"0.00","exchangeRate":"1.000000","processedAt":"null","merchantFees":"0.00","sourceCurrency":"USD","sourceCurrencyName":"US Dollar","targetCurrency":"USD","targetCurrencyName":"US Dollar","compliance":{"status":"pending","checkedAt":"null"}}],"meta":{"page":1,"pages":1,"records":1}}}}
        self.assertEqual(response, status)

    @patch('paymentrails.batch.Batch.find',fake_find)
    def test_retrieve_batch_InvalidBatchId(self):
        with self.assertRaises(paymentrails.exceptions.notFoundException.NotFoundException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            response = paymentrails.batch.Batch.find("dddd")
    @patch('paymentrails.batch.Batch.find',fake_find)
    def test_retrieve_batch_None(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            response = paymentrails.batch.Batch.find(None)
    
    @patch('paymentrails.batch.Batch.update',fake_update)
    def test_update_batch(self):
        paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
        body = {"update_payments": [
            {"id": "P-91XQ0U0B1RW5M", "sourceAmount": 999}]}
        response = paymentrails.batch.Batch.update("B-912Q61G0BRVGC", body)
        status = {"ok": "true", "object": "updated"}
        self.assertEqual(response, status)

    @patch('paymentrails.batch.Batch.update',fake_update)
    def test_update_batch_InvalidBatchId(self):
        with self.assertRaises(paymentrails.exceptions.notFoundException.NotFoundException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            body = {"update_payments": [
                {"id": "P-91XQ0U0B1RW5M", "sourceAmount": 999}]}
            response = paymentrails.batch.Batch.update("ddddd",body)

    @patch('paymentrails.batch.Batch.update',fake_update)
    def test_update_batch_None_Batch(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            body = {"update_payments": [
                {"id": "P-91XQ0U0B1RW5M", "sourceAmount": 999}]}
            response = paymentrails.batch.Batch.update(None,body)
    @patch('paymentrails.batch.Batch.update',fake_update)
    def test_update_batch_None_Body(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            response = paymentrails.batch.Batch.update("B-ddddd",None)
    @patch('paymentrails.batch.Batch.delete',fake_delete)
    def test_delete_batch(self):
        paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
        response = paymentrails.batch.Batch.delete("B-912Q61G0BRVGC")
        status = {"ok": "true", "object": "deleted"}
        self.assertEqual(response, status)

    @patch('paymentrails.batch.Batch.delete',fake_delete)
    def test_delete_batch_InvalidBatchId(self):
        with self.assertRaises(paymentrails.exceptions.notFoundException.NotFoundException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            response = paymentrails.batch.Batch.delete("ddddd")
    @patch('paymentrails.batch.Batch.delete',fake_delete)
    def test_delete_batch_None_Batch(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            response = paymentrails.batch.Batch.delete(None)
    @patch('paymentrails.batch.Batch.search',fake_search)
    def test_list_allBatchesWithQueries(self):
        paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
        response = paymentrails.batch.Batch.search(1, 10, "f18")
        status = {"ok":"true","batches":[{"id":"B-91XQ40VT5HF18","status":"open","amount":"900.90","totalPayments":1,"currency":"USD","description":"Weekly Payouts on 2017-4-8","sentAt":"null","completedAt":"null","createdAt":"2017-05-08T18:30:44.905Z","updatedAt":"2017-05-12T18:39:06.125Z"}],"meta":{"page":1,"pages":1,"records":1}}
        self.assertEqual(response, status)

    @patch('paymentrails.batch.Batch.search',fake_search)
    def test_list_allBatchesWithNone(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            response = paymentrails.batch.Batch.search(1, 10, None)
            
    @patch('paymentrails.batch.Batch.summary',fake_summary)
    def test_batch_summary(self):
        paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
        response = paymentrails.batch.Batch.summary("B-912Q61G0BRVGC")
        status = {"ok":"true","batchSummary":{"id":"B-91XQ40VT5HF18","serverTime":"2017-05-16T13:34:52.026Z","status":"open","currency":"USD","description":"Weekly Payouts on 2017-4-8","sentAt":"null","completedAt":"null","createdAt":"2017-05-08T18:30:44.905Z","processed_by":"API","updatedAt":"2017-05-12T18:39:06.125Z","quoteExpiredAt":"null","errors":[],"methods":{"paypal":{"count":1,"value":900.9,"fees":0,"recipientFees":0,"merchantFees":0,"net":900.9,"accountType":"Gateway","displayName":"PayPal"},"bank-transfer":{"count":0,"value":0,"fees":0,"recipientFees":0,"merchantFees":0,"net":0,"accountType":"PaymentRails","displayName":"Bank Transfer"}},"PaymentRailsTotal":{"count":0,"value":0,"fees":0,"recipientFees":0,"merchantFees":0,"net":0},"GatewayTotal":{"count":1,"value":900.9,"fees":0,"recipientFees":0,"merchantFees":0,"net":900.9},"total":{"count":1,"value":900.9,"fees":0,"recipientFees":0,"merchantFees":0,"net":900.9},"merchantBalances":{"GatewayTotal":0,"PaymentRailsTotal":10000},"enoughFunds":"true"}}
        self.assertEqual(response, status)

    @patch('paymentrails.batch.Batch.summary',fake_summary)
    def test_batch_summary_InvalidBatchId(self):
        with self.assertRaises(paymentrails.exceptions.notFoundException.NotFoundException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            response = paymentrails.batch.Batch.summary("dddd")
    @patch('paymentrails.batch.Batch.summary',fake_summary)
    def test_batch_summary_None(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            response = paymentrails.batch.Batch.summary(None)

    @patch('paymentrails.batch.Batch.create',fake_create)
    @patch('paymentrails.batch.Batch.generate_quote',fake_generate_quote)
    @patch('paymentrails.batch.Batch.process_batch',fake_process_batch)
    def test_create_batch(self):
        paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
        body = {"payments": [{"recipient": {"id": "R-91XQ0PJH39U54"},
                              "sourceAmount": "65", "memo": "", "sourceCurrency": "CAD"}]}
        response = paymentrails.batch.Batch.create(body)
        status = {"ok": "true"}
        self.assertEqual(response,status)

        batchId = 'B-91XQ40VT5HF18' 

        response = paymentrails.batch.Batch.generate_quote(batchId)
        status = {"ok":"true","batch":{"id":"B-91XQ40VT5HF18","status":"open","amount":"900.90","totalPayments":"1","currency":"USD","description":"Weekly Payouts on 2017-4-8","sentAt":"null","completedAt":"null","createdAt":"2017-05-08T18:30:44.905Z","updatedAt":"2017-05-16T13:40:08.098Z"}}
        self.assertEqual(response, status)


        response = paymentrails.batch.Batch.process_batch(batchId)
        status = {"ok":"true","batch":{"id":"B-91XQ40VT5HF18","status":"processing","amount":"900.90","totalPayments":1,"currency":"USD","description":"Weekly Payouts on 2017-4-8","sentAt":"2017-05-16T13:41:56.149Z","completedAt":"null","createdAt":"2017-05-08T18:30:44.905Z","updatedAt":"2017-05-16T13:41:56.150Z"}}
        self.assertEqual(response, status)
    
    @patch('paymentrails.batch.Batch.create',fake_create)
    def test_create_batch_None(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestBatch.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestBatch.private_key)
            response = paymentrails.batch.Batch.create(None)


if __name__ == '__main__':
    unittest.main()
