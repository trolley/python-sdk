import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath('.'))

import trolley
from trolley.client import Client
from trolley.configuration import Configuration
from trolley.gateway import Gateway
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
        return {"ok": True, "balances": []}

    def post(self, endpoint, body):
        self.calls.append(("POST", endpoint, body))
        return {"ok": True, "verifications": [{"id": "WV-123", "type": "watchlist"}], "meta": {"page": 1, "pages": 1, "records": 1}}

    def patch(self, endpoint, body):
        self.calls.append(("PATCH", endpoint, body))
        return {"ok": True, "verifications": [{"id": "WV-123", "type": "watchlist"}], "meta": {"page": 1, "pages": 1, "records": 1}}


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


if __name__ == "__main__":
    unittest.main()
