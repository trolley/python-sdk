import os
import sys
import unittest
from unittest.mock import Mock, patch

sys.path.append(os.path.abspath('.'))

import trolley
from trolley.client import Client
from trolley.configuration import Configuration
from trolley.exceptions.invalidFieldException import InvalidFieldException
from trolley.gateway import Gateway
from trolley.types.balances import Balances
from trolley.types.batch import Batch
from trolley.types.invoice_payment import InvoicePayment
from trolley.types.offline_payment import OfflinePayment
from trolley.types.payment import Payment
from trolley.types.recipient import Recipient
from trolley.types.recipient_account import RecipientAccount


class FakeResponse:
    status_code = 200
    content = b'{"ok": true}'


class FakeClient:
    def __init__(self):
        self.calls = []

    def get(self, endpoint):
        self.calls.append(("GET", endpoint, None))
        if endpoint.startswith("/v1/verifications"):
            return {"ok": True, "verifications": [{"id": "WV-123", "type": "watchlist"}], "meta": {"page": 1, "pages": 1, "records": 1}}
        if endpoint.startswith("/v1/balances"):
            return {"ok": True, "balances": [{"type": "paymentrails", "amount": "10.00"}]}
        if endpoint.endswith("/summary"):
            return {"ok": True, "batchSummary": {"id": "B-123", "status": "open"}}
        if "/payments/" in endpoint or endpoint.startswith("/v1/payments/"):
            return {"ok": True, "payment": {"id": "P-123", "visibleToRecipient": False}}
        if endpoint.startswith("/v1/batches?"):
            return {"ok": True, "batches": [{"id": "B-123"}], "meta": {"page": 1, "pages": 1, "records": 1}}
        if endpoint.startswith("/v1/batches/"):
            return {"ok": True, "batch": {"id": "B-123", "status": "open"}}
        if endpoint.endswith("/accounts/"):
            return {"ok": True, "accounts": [{"id": "A-123"}]}
        if "/accounts/" in endpoint:
            return {"ok": True, "account": {"id": "A-123"}}
        if endpoint.startswith("/v1/recipients/"):
            return {"ok": True, "recipient": {"id": "R-123", "accounts": []}}
        return {"ok": True, "balances": []}

    def post(self, endpoint, body):
        self.calls.append(("POST", endpoint, body))
        if endpoint.startswith("/v1/batches/"):
            return {"ok": True, "batch": {"id": "B-123", "status": "open"}}
        if endpoint.startswith("/v1/invoices/payment/create"):
            return {"ok": True, "batchId": body.get("batchId"), "paymentId": "P-123", "invoicePayments": []}
        if endpoint.startswith("/v1/batches"):
            return {"ok": True, "batch": {"id": "B-123", "status": "open"}}
        if endpoint.startswith("/v1/recipients/") and endpoint.endswith("/accounts"):
            return {"ok": True, "account": {"id": "A-123"}}
        if endpoint.endswith("/payments"):
            return {"ok": True, "payment": {"id": "P-123", "visibleToRecipient": False}}
        return {"ok": True, "verifications": [{"id": "WV-123", "type": "watchlist"}], "meta": {"page": 1, "pages": 1, "records": 1}}

    def patch(self, endpoint, body):
        self.calls.append(("PATCH", endpoint, body))
        if "/payments/" in endpoint:
            return {"ok": True, "payment": {"id": "P-123", "visibleToRecipient": False}}
        if "/accounts/" in endpoint:
            return {"ok": True, "account": {"id": "A-123"}}
        return {"ok": True, "verifications": [{"id": "WV-123", "type": "watchlist"}], "meta": {"page": 1, "pages": 1, "records": 1}}

    def delete(self, endpoint, body={}):
        self.calls.append(("DELETE", endpoint, body))
        return {"ok": True}


class ReleasePrepTest(unittest.TestCase):
    def test_client_request_uses_authenticated_shared_request_path(self):
        config = Configuration("public", "private")
        client = Client(config)

        with patch("requests.get", return_value=FakeResponse()) as request:
            response = client.request("get", "/v1/balances")

        self.assertEqual({"ok": True}, response)
        headers = request.call_args.kwargs["headers"]
        self.assertEqual("python-sdk_1.1.0", headers["Trolley-Source"])
        self.assertTrue(headers["Authorization"].startswith("prsign public:"))

    def test_gateway_exposes_generic_request_and_trust_alias(self):
        gateway = Gateway(Configuration("public", "private"))

        self.assertTrue(callable(gateway.request))
        self.assertIs(gateway.trust, gateway.verification)

    def test_verification_gateway_calls_documented_endpoints(self):
        gateway = Gateway(Configuration("public", "private"))
        fake_client = FakeClient()

        with patch("trolley.configuration.Configuration.client", return_value=fake_client):
            search = gateway.verification.search(verificationType="watchlist", page=1, pageSize=10)
            expire = gateway.verification.expire({"type": "individual", "verificationIds": ["IV-123"]})
            trigger = gateway.verification.trigger("individual", {"recipientIds": ["R-123"]})
            watchlist = gateway.verification.trigger_watchlist({"recipientIds": ["R-123"]})

        self.assertEqual("WV-123", search[0].id)
        self.assertEqual("WV-123", expire[0].id)
        self.assertEqual("WV-123", trigger[0].id)
        self.assertEqual("WV-123", watchlist[0].id)
        self.assertEqual(("GET", "/v1/verifications?verificationType=watchlist&page=1&pageSize=10", None), fake_client.calls[0])
        self.assertEqual(("PATCH", "/v1/verifications/expire", {"type": "individual", "verificationIds": ["IV-123"]}), fake_client.calls[1])
        self.assertEqual(("POST", "/v1/verifications/individual/trigger", {"recipientIds": ["R-123"]}), fake_client.calls[2])
        self.assertEqual(("POST", "/v1/verifications/watchlist/trigger", {"recipientIds": ["R-123"]}), fake_client.calls[3])

    def test_invoice_payment_create_preserves_existing_body_and_adds_batch_id(self):
        gateway = Gateway(Configuration("public", "private"))
        fake_client = FakeClient()

        with patch("trolley.configuration.Configuration.client", return_value=fake_client):
            gateway.invoice_payment.create(["I-123"], batch_id="B-123", memo="memo")

        self.assertEqual(("POST", "/v1/invoices/payment/create", {"ids": ["I-123"], "batchId": "B-123", "memo": "memo"}), fake_client.calls[0])

    def test_gateway_paths_are_documented_without_breaking_existing_signatures(self):
        gateway = Gateway(Configuration("public", "private"))
        fake_client = FakeClient()

        with patch("trolley.configuration.Configuration.client", return_value=fake_client):
            gateway.balances.get_all_balances()
            gateway.balances.get_trolley_balance()
            gateway.balances.get_paypal_balance()
            gateway.batch.find("B-123")
            gateway.batch.generate_quote("B-123")
            gateway.batch.process_batch("B-123")
            gateway.batch.summary("B-123")
            gateway.batch.delete("B-123")
            gateway.payment.create({"recipient": {"id": "R-123"}, "sourceAmount": "10.00"}, "B-123")
            gateway.payment.find("P-123", "B-123")
            gateway.payment.find_by_id("P-123")
            gateway.payment.update("P-123", {"memo": "updated"}, "B-123")
            gateway.payment.delete("P-123", "B-123")
            gateway.recipient.find("R-123")
            gateway.recipient.delete_multiple(["R-123", "R-456"])
            gateway.recipient_account.create("R-123", {"type": "paypal", "emailAddress": "test@example.com"})
            gateway.recipient_account.find("R-123", "A-123")
            gateway.recipient_account.update("R-123", "A-123", {"primary": True})
            gateway.recipient_account.delete("R-123", "A-123")
            gateway.recipient_account.all("R-123")

        self.assertIn(("GET", "/v1/balances", None), fake_client.calls)
        self.assertIn(("GET", "/v1/balances/paymentrails", None), fake_client.calls)
        self.assertIn(("GET", "/v1/balances/paypal", None), fake_client.calls)
        self.assertIn(("GET", "/v1/batches/B-123", None), fake_client.calls)
        self.assertIn(("POST", "/v1/batches/B-123/generate-quote", {}), fake_client.calls)
        self.assertIn(("POST", "/v1/batches/B-123/start-processing", {}), fake_client.calls)
        self.assertIn(("GET", "/v1/batches/B-123/summary", None), fake_client.calls)
        self.assertIn(("DELETE", "/v1/batches/B-123", {}), fake_client.calls)
        self.assertIn(("POST", "/v1/batches/B-123/payments", {"recipient": {"id": "R-123"}, "sourceAmount": "10.00"}), fake_client.calls)
        self.assertIn(("GET", "/v1/batches/B-123/payments/P-123", None), fake_client.calls)
        self.assertIn(("GET", "/v1/payments/P-123", None), fake_client.calls)
        self.assertIn(("PATCH", "/v1/batches/B-123/payments/P-123", {"memo": "updated"}), fake_client.calls)
        self.assertIn(("DELETE", "/v1/batches/B-123/payments/P-123", {}), fake_client.calls)
        self.assertIn(("GET", "/v1/recipients/R-123", None), fake_client.calls)
        self.assertIn(("DELETE", "/v1/recipients/", {"ids": ["R-123", "R-456"]}), fake_client.calls)
        self.assertIn(("POST", "/v1/recipients/R-123/accounts", {"type": "paypal", "emailAddress": "test@example.com"}), fake_client.calls)
        self.assertIn(("GET", "/v1/recipients/R-123/accounts/A-123", None), fake_client.calls)
        self.assertIn(("PATCH", "/v1/recipients/R-123/accounts/A-123", {"primary": True}), fake_client.calls)
        self.assertIn(("DELETE", "/v1/recipients/R-123/accounts/A-123", {}), fake_client.calls)
        self.assertIn(("GET", "/v1/recipients/R-123/accounts/", None), fake_client.calls)

    def test_documented_response_attributes_are_mapped(self):
        payment = Payment.factory({"payment": {"id": "P-123", "visibleToRecipient": False}})
        offline_payment = OfflinePayment.factory({"offlinePayment": {"id": "OP-123", "activityCount": 1, "taxReportable": True}})
        recipient = Recipient.factory({"recipient": {"id": "R-123", "placeOfBirth": "CA", "tags": ["tag"]}})
        account = RecipientAccount.factory({"account": {"id": "A-123", "cardDetails": {"brand": "visa"}, "mailing": {"city": "Toronto"}, "phoneNumber": "+15555550123"}})
        invoice_payment = InvoicePayment.factory({"invoicePayment": {"id": "IP-123", "status": "pending", "memo": "memo", "externalId": "external", "tags": ["tag"], "coverFees": True}})

        self.assertFalse(payment["visibleToRecipient"])
        self.assertEqual(1, offline_payment["activityCount"])
        self.assertTrue(offline_payment["taxReportable"])
        self.assertEqual("CA", recipient["placeOfBirth"])
        self.assertEqual(["tag"], recipient["tags"])
        self.assertEqual({"brand": "visa"}, account["cardDetails"])
        self.assertEqual({"city": "Toronto"}, account["mailing"])
        self.assertEqual("+15555550123", account["phoneNumber"])
        self.assertEqual("pending", invoice_payment["status"])
        self.assertEqual("memo", invoice_payment["memo"])
        self.assertEqual("external", invoice_payment["externalId"])
        self.assertEqual(["tag"], invoice_payment["tags"])
        self.assertTrue(invoice_payment["coverFees"])

    def test_legacy_static_methods_delegate_to_current_gateway(self):
        gateway = Mock()
        gateway.balances.get_all_balances.return_value = "balances"
        gateway.batch.find.return_value = "batch_find"
        gateway.batch.create.return_value = "batch_create"
        gateway.batch.update.return_value = "batch_update"
        gateway.batch.delete.return_value = "batch_delete"
        gateway.batch.search_by_page.return_value = "batch_search"
        gateway.batch.summary.return_value = "batch_summary"
        gateway.batch.generate_quote.return_value = "batch_quote"
        gateway.batch.process_batch.return_value = "batch_process"
        gateway.payment.find.return_value = "payment_find"
        gateway.payment.create.return_value = "payment_create"
        gateway.payment.update.return_value = "payment_update"
        gateway.payment.delete.return_value = "payment_delete"
        gateway.payment.search_by_page.return_value = "payment_search"
        gateway.recipient.find.return_value = "recipient_find"
        gateway.recipient.retrieve_logs.return_value = "recipient_logs"
        gateway.recipient.get_all_payments.return_value = "recipient_payments"
        gateway.recipient.create.return_value = "recipient_create"
        gateway.recipient.update.return_value = "recipient_update"
        gateway.recipient.delete.return_value = "recipient_delete"
        gateway.recipient.search_by_page.return_value = "recipient_search"

        with patch("trolley.configuration.Configuration.gateway", return_value=gateway):
            self.assertEqual("balances", Balances.find("paypal"))
            self.assertEqual("batch_find", Batch.find("B-123"))
            self.assertEqual("batch_create", Batch.create({"description": "batch"}))
            self.assertEqual("batch_update", Batch.update("B-123", {"description": "updated"}))
            self.assertEqual("batch_delete", Batch.delete("B-123"))
            self.assertEqual("batch_search", Batch.search(2, 20, "term"))
            self.assertEqual("batch_summary", Batch.summary("B-123"))
            self.assertEqual("batch_quote", Batch.generate_quote("B-123"))
            self.assertEqual("batch_process", Batch.process_batch("B-123"))
            self.assertEqual("payment_find", Payment.find("P-123", "B-123"))
            self.assertEqual("payment_create", Payment.create({"amount": "10.00"}, "B-123"))
            self.assertEqual("payment_update", Payment.update("P-123", "B-123", {"memo": "updated"}))
            self.assertEqual("payment_delete", Payment.delete("P-123", "B-123"))
            self.assertEqual("payment_search", Payment.search(3, 30, "payment-term"))
            self.assertEqual("recipient_find", Recipient.find("R-123"))
            self.assertEqual("recipient_logs", Recipient.find("R-123", "logs"))
            self.assertEqual("recipient_payments", Recipient.find("R-123", "payments"))
            self.assertEqual("recipient_create", Recipient.create({"type": "individual"}))
            self.assertEqual("recipient_update", Recipient.update("R-123", {"firstName": "Ada"}))
            self.assertEqual("recipient_delete", Recipient.delete("R-123"))
            self.assertEqual("recipient_search", Recipient.search(4, 40, "recipient-term"))

        gateway.balances.get_all_balances.assert_called_once_with("paypal")
        gateway.batch.search_by_page.assert_called_once_with("term", 2, 20)
        gateway.payment.update.assert_called_once_with("P-123", {"memo": "updated"}, "B-123")
        gateway.payment.search_by_page.assert_called_once_with("", "payment-term", 3, 30)
        gateway.recipient.search_by_page.assert_called_once_with(4, 40, "recipient-term")

    def test_exceptions_accept_plain_string_messages(self):
        error = InvalidFieldException("Body cannot be None")

        self.assertEqual("Body cannot be None", error.value)
        self.assertEqual([{"message": "Body cannot be None"}], error.get_error_array())


if __name__ == "__main__":
    unittest.main()
