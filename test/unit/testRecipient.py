import sys
import os
import unittest

sys.path.append(os.path.abspath('.'))

import paymentrails.configuration
import paymentrails.recipient
from mock import MagicMock, Mock, patch


import paymentrails.exceptions.notFoundException
import paymentrails.exceptions.invalidFieldException


def fake_find(recipientId, term=""):
    if recipientId is None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Recipient id cannot be None")
    if recipientId[0:1] != "R":
        raise paymentrails.exceptions.notFoundException.NotFoundException("Recipient id is invalid")
    if term == "logs":
        return {"ok":"true","activities":[{"ip":"::ffff:127.0.0.1","url":"/v1/recipients/R-91XQ8T3G088QM/","method":"POST","headers":{"host":"api.local.dev:3000","connection":"keep-alive","content-length":"97","postman-token":"93d525ab-dfa7-1a90-2fe6-9b337716d8af","cache-control":"no-cache","origin":"chrome-extension://fhbjgbiflinjbdggehcddcbncdddomop","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36","x-api-key":"pk_test_dfffddfdf","content-type":"application/json","accept":"*/*","accept-encoding":"gzip, deflate","accept-language":"en-US,en;q=0.8"},"request":"{\"type\": \"individual\", \"firstName\": \"John\", \"lastName\": \"Smith\", \"email\": \"jsmith@examwdple.com\"}","response":"{\"ok\":false,\"errors\":[{\"code\":\"not_found\",\"message\":\"Object not found\"}]}","code":404,"source":"api-server","testMode":"true","createdAt":"2017-05-15T20:45:32.766Z"},{"ip":"::ffff:127.0.0.1","url":"/v1/recipients/R-91XQ8T3G088QM/logs","method":"POST","headers":{"host":"api.local.dev:3000","connection":"keep-alive","content-length":"97","postman-token":"985161e4-e9e3-6622-ade0-7bce775b6acc","cache-control":"no-cache","origin":"chrome-extension://fhbjgbiflinjbdggehcddcbncdddomop","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36","x-api-key":"pk_test_dfffddfdf","content-type":"application/json","accept":"*/*","accept-encoding":"gzip, deflate","accept-language":"en-US,en;q=0.8"},"request":"{\"type\": \"individual\", \"firstName\": \"John\", \"lastName\": \"Smith\", \"email\": \"jsmith@examwdple.com\"}","response":"{\"ok\":false,\"errors\":[{\"code\":\"not_found\",\"message\":\"Object not found\"}]}","code":404,"source":"api-server","testMode":"true","createdAt":"2017-05-15T20:45:25.960Z"}],"meta":{"page":1,"pages":1,"records":2}}
    if term == "payments":
        return {"ok":"true","payments":[],"meta":{"page":1,"pages":0,"records":0}}
    return {"ok": "true", "recipient": {"id": "R-91XQ4QBJ65W1U", "referenceId": "jsmwwdith@example.com", "email": "jsmwwdith@example.com", "name": "John Smith", "lastName": "Smith", "firstName": "John", "type": "individual", "status": "active", "language": "en", "complianceStatus": "pending", "dob": "null", "payoutMethod": "paypal", "updatedAt": "2017-05-12T15:22:09.444Z", "createdAt": "2017-05-09T15:16:32.591Z", "gravatarUrl": "https://s3.amazonaws.com/static.api.trolley.com/icon_user.svg", "compliance": {"status": "pending", "checkedAt": "null"}, "payout": {"autoswitch": {"limit": 1000, "active": "false"}, "holdup": {"limit": 1000, "active": "false"}, "primary": {"method": "paypal", "currency": {"currency": {"code": "CAD", "name": "Canadian Dollar"}}}, "method": "paypal", "accounts": {"paypal": {"address": "testpaypal@example.com"}}, "methodDisplay": "PayPal"}, "address": {"street1": "null", "street2": "null", "city": "null", "postalCode": "null", "country": "null", "region": "null", "phone": "null"}, "primaryCurrency": "CAD"}}

def fake_update(recipientId, body):
    if recipientId is None:
            raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Recipient id cannot be None")
    if recipientId[0:1] != "R":
        raise paymentrails.exceptions.notFoundException.NotFoundException("Recipient id is invalid")
    if body is None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Body cannot be None")
    return {"ok": "true", "object": "updated"}

def fake_create(body):
    if body is None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Body cannot be None")

    return {"ok": "true"}

def fake_delete(recipientId):
    if recipientId is None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Recipient id cannot be None")
    if recipientId[0:1] != "R":
        raise paymentrails.exceptions.notFoundException.NotFoundException("Recipient id is invalid")
    return {"ok": "true", "object": "deleted"}

def fake_search(page, pageSize, term):
    if term is None:
        raise paymentrails.exceptions.invalidFieldException.InvalidFieldException("Term cannot be None")
    return {"ok":"true","recipients":[{"id":"R-91XQ8T3G088QM","referenceId":"jsmith@examwdple.com","email":"jsmith@examwdple.com","name":"John Smith","lastName":"Smith","firstName":"John","type":"individual","status":"incomplete","language":"en","complianceStatus":"pending","dob":"null","payoutMethod":"null","updatedAt":"2017-05-15T20:34:50.558Z","createdAt":"2017-05-15T20:34:50.558Z","gravatarUrl":"https://s3.amazonaws.com/static.api.trolley.com/icon_user.svg","compliance":{"status":"pending","checkedAt":"null"},"payout":{"method":"null"},"address":{"street1":"null","street2":"null","city":"null","postalCode":"null","country":"null","region":"null","phone":"null"}},{"id":"R-91XQ4Q8R2WY28","referenceId":"jsmith@fff.com","email":"jsmith@fff.com","name":"John Smith","lastName":"Smith","firstName":"John","type":"individual","status":"incomplete","language":"en","complianceStatus":"pending","dob":"null","payoutMethod":"bank","updatedAt":"2017-05-09T15:12:19.683Z","createdAt":"2017-05-09T15:11:40.483Z","gravatarUrl":"https://s3.amazonaws.com/static.api.trolley.com/icon_user.svg","compliance":{"status":"pending","checkedAt":"null"},"payout":{"autoswitch":{"limit":1000,"active":"false"},"holdup":{"limit":1000,"active":"false"},"primary":{"method":"bank","currency":{"currency":{"code":"CAD","name":"Canadian Dollar"}}},"method":"bank","accounts":{},"methodDisplay":"Bank Transfer"},"address":{"street1":"null","street2":"null","city":"null","postalCode":"null","country":"null","region":"null","phone":"null"},"primaryCurrency":"CAD"}],"meta":{"page":1,"pages":1,"records":2}}


class TestRecipient(unittest.TestCase):

    public_key = ("public_key")
    private_key = ("private_key")

    @patch('paymentrails.recipient.Recipient.find', fake_find)
    def test_retrieve_recipient(self):
        paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
        response = paymentrails.recipient.Recipient.find("R-91XQ4QBJ65W1U")
        status = {"ok": "true", "recipient": {"id": "R-91XQ4QBJ65W1U", "referenceId": "jsmwwdith@example.com", "email": "jsmwwdith@example.com", "name": "John Smith", "lastName": "Smith", "firstName": "John", "type": "individual", "status": "active", "language": "en", "complianceStatus": "pending", "dob": "null", "payoutMethod": "paypal", "updatedAt": "2017-05-12T15:22:09.444Z", "createdAt": "2017-05-09T15:16:32.591Z", "gravatarUrl": "https://s3.amazonaws.com/static.api.trolley.com/icon_user.svg", "compliance": {"status": "pending", "checkedAt": "null"}, "payout": {"autoswitch": {"limit": 1000, "active": "false"}, "holdup": {"limit": 1000, "active": "false"}, "primary": {"method": "paypal", "currency": {"currency": {"code": "CAD", "name": "Canadian Dollar"}}}, "method": "paypal", "accounts": {"paypal": {"address": "testpaypal@example.com"}}, "methodDisplay": "PayPal"}, "address": {"street1": "null", "street2": "null", "city": "null", "postalCode": "null", "country": "null", "region": "null", "phone": "null"}, "primaryCurrency": "CAD"}}
        self.assertEqual(response, status)

    @patch('paymentrails.recipient.Recipient.find', fake_find)
    def test_retrieve_recipient_Invalid_RecipientId(self):
        with self.assertRaises(paymentrails.exceptions.notFoundException.NotFoundException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            response = paymentrails.recipient.Recipient.find("jfjfj")
    @patch('paymentrails.recipient.Recipient.find', fake_find)
    def test_retrieve_recipient_None_Recipient(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            response = paymentrails.recipient.Recipient.find(None)

    @patch('paymentrails.recipient.Recipient.create', fake_create)
    def test_create_recipient(self):
        paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
        body = {'type': 'individual', 'firstName': 'Bob',
                'lastName': 'TheBuilder', 'email': 'bob@thebuilder.com'}
        response = paymentrails.recipient.Recipient.create(body)
        status = {"ok": "true"}
        self.assertEqual(status, response)

    @patch('paymentrails.recipient.Recipient.create', fake_create)
    def test_create_recipient_None_body(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            response = paymentrails.recipient.Recipient.create(None)
    
    @patch('paymentrails.recipient.Recipient.update', fake_update)
    def test_update_recipient(self):
        paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
        body = {'firstName': 'Mark'}
        recipientId = 'R-91XQ0FRA3T40Y'
        response = paymentrails.recipient.Recipient.update(recipientId, body)
        status = {"ok": "true", "object": "updated"}
        self.assertEqual(response, status)

    @patch('paymentrails.recipient.Recipient.update', fake_update)
    def test_update_recipient_InvalidRecipientId(self):
        with self.assertRaises(paymentrails.exceptions.notFoundException.NotFoundException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            body = {'firstName': 'Mark'}
            recipientId = 'dddd'
            response = paymentrails.recipient.Recipient.update(recipientId, body)
    @patch('paymentrails.recipient.Recipient.update', fake_update)
    def test_update_recipient_None_recipient(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            body = {'firstName': 'Mark'}
            response = paymentrails.recipient.Recipient.update(None, body)
    @patch('paymentrails.recipient.Recipient.update', fake_update)
    def test_update_recipient_None_body(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            response = paymentrails.recipient.Recipient.update("R-hghgh", None)
    @patch('paymentrails.recipient.Recipient.delete', fake_delete)
    def test_delete_recipient(self):
        paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
        recipientId = 'R-91XPYX3V2MM1G'
        response = paymentrails.recipient.Recipient.delete(recipientId)
        status = {"ok": "true", "object": "deleted"}
        self.assertEqual(response, status)

    @patch('paymentrails.recipient.Recipient.delete', fake_delete)
    def test_delete_recipient_InvalidRecipientId(self):
        with self.assertRaises(paymentrails.exceptions.notFoundException.NotFoundException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            recipientId = 'fefef'
            response = paymentrails.recipient.Recipient.delete(recipientId)

    @patch('paymentrails.recipient.Recipient.delete', fake_delete)
    def test_delete_recipient_None_recipient(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            response = paymentrails.recipient.Recipient.delete(None)

    @patch('paymentrails.recipient.Recipient.search', fake_search)
    def test_list_allRecipientsWithQueries(self):
        paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
        response = paymentrails.recipient.Recipient.search(1, 10, "")
        status = {"ok":"true","recipients":[{"id":"R-91XQ8T3G088QM","referenceId":"jsmith@examwdple.com","email":"jsmith@examwdple.com","name":"John Smith","lastName":"Smith","firstName":"John","type":"individual","status":"incomplete","language":"en","complianceStatus":"pending","dob":"null","payoutMethod":"null","updatedAt":"2017-05-15T20:34:50.558Z","createdAt":"2017-05-15T20:34:50.558Z","gravatarUrl":"https://s3.amazonaws.com/static.api.trolley.com/icon_user.svg","compliance":{"status":"pending","checkedAt":"null"},"payout":{"method":"null"},"address":{"street1":"null","street2":"null","city":"null","postalCode":"null","country":"null","region":"null","phone":"null"}},{"id":"R-91XQ4Q8R2WY28","referenceId":"jsmith@fff.com","email":"jsmith@fff.com","name":"John Smith","lastName":"Smith","firstName":"John","type":"individual","status":"incomplete","language":"en","complianceStatus":"pending","dob":"null","payoutMethod":"bank","updatedAt":"2017-05-09T15:12:19.683Z","createdAt":"2017-05-09T15:11:40.483Z","gravatarUrl":"https://s3.amazonaws.com/static.api.trolley.com/icon_user.svg","compliance":{"status":"pending","checkedAt":"null"},"payout":{"autoswitch":{"limit":1000,"active":"false"},"holdup":{"limit":1000,"active":"false"},"primary":{"method":"bank","currency":{"currency":{"code":"CAD","name":"Canadian Dollar"}}},"method":"bank","accounts":{},"methodDisplay":"Bank Transfer"},"address":{"street1":"null","street2":"null","city":"null","postalCode":"null","country":"null","region":"null","phone":"null"},"primaryCurrency":"CAD"}],"meta":{"page":1,"pages":1,"records":2}}
        self.assertEqual(response, status)
    @patch('paymentrails.recipient.Recipient.search', fake_search)
    def test_list_allRecipientsWithQueries_None_term(self):
        with self.assertRaises(paymentrails.exceptions.invalidFieldException.InvalidFieldException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            response = paymentrails.recipient.Recipient.search(1, 10, None)

    @patch('paymentrails.recipient.Recipient.find', fake_find)
    def test_retrieveLogs(self):
        paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
        response = paymentrails.recipient.Recipient.find("R-91XPYX3V2MM1G", "logs")
        status = {"ok":"true","activities":[{"ip":"::ffff:127.0.0.1","url":"/v1/recipients/R-91XQ8T3G088QM/","method":"POST","headers":{"host":"api.local.dev:3000","connection":"keep-alive","content-length":"97","postman-token":"93d525ab-dfa7-1a90-2fe6-9b337716d8af","cache-control":"no-cache","origin":"chrome-extension://fhbjgbiflinjbdggehcddcbncdddomop","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36","x-api-key":"pk_test_dfffddfdf","content-type":"application/json","accept":"*/*","accept-encoding":"gzip, deflate","accept-language":"en-US,en;q=0.8"},"request":"{\"type\": \"individual\", \"firstName\": \"John\", \"lastName\": \"Smith\", \"email\": \"jsmith@examwdple.com\"}","response":"{\"ok\":false,\"errors\":[{\"code\":\"not_found\",\"message\":\"Object not found\"}]}","code":404,"source":"api-server","testMode":"true","createdAt":"2017-05-15T20:45:32.766Z"},{"ip":"::ffff:127.0.0.1","url":"/v1/recipients/R-91XQ8T3G088QM/logs","method":"POST","headers":{"host":"api.local.dev:3000","connection":"keep-alive","content-length":"97","postman-token":"985161e4-e9e3-6622-ade0-7bce775b6acc","cache-control":"no-cache","origin":"chrome-extension://fhbjgbiflinjbdggehcddcbncdddomop","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36","x-api-key":"pk_test_dfffddfdf","content-type":"application/json","accept":"*/*","accept-encoding":"gzip, deflate","accept-language":"en-US,en;q=0.8"},"request":"{\"type\": \"individual\", \"firstName\": \"John\", \"lastName\": \"Smith\", \"email\": \"jsmith@examwdple.com\"}","response":"{\"ok\":false,\"errors\":[{\"code\":\"not_found\",\"message\":\"Object not found\"}]}","code":404,"source":"api-server","testMode":"true","createdAt":"2017-05-15T20:45:25.960Z"}],"meta":{"page":1,"pages":1,"records":2}}
        self.assertEqual(response, status)

    @patch('paymentrails.recipient.Recipient.find', fake_find)
    def test_retrieveLogs_InvalidRecipientId(self):
        with self.assertRaises(paymentrails.exceptions.notFoundException.NotFoundException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            response = paymentrails.recipient.Recipient.find("wdwd", "logs")
    @patch('paymentrails.recipient.Recipient.find', fake_find)
    def test_retrievePayments(self):
        paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
        paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
        response = paymentrails.recipient.Recipient.find("R-91XPYX3V2MM1G", "payments")
        status = {"ok":"true","payments":[],"meta":{"page":1,"pages":0,"records":0}}
        self.assertEqual(response, status)
        
    @patch('paymentrails.recipient.Recipient.find', fake_find)
    def test_retrievePayments_InvalidRecipientId(self):
        with self.assertRaises(paymentrails.exceptions.notFoundException.NotFoundException):
            paymentrails.configuration.Configuration.set_public_key(TestRecipient.public_key)
            paymentrails.configuration.Configuration.set_private_key(TestRecipient.private_key)
            response = paymentrails.recipient.Recipient.find("wdwd", "payments")


if __name__ == '__main__':
    unittest.main()
