import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath('.'))

from trolley.configuration import Configuration
from trolley.fees_gateway import FeesGateway
from trolley.gateway import Gateway


class FakeClient:
    def __init__(self):
        self.calls = []
        self.revenue_stream = {
            "currencyCode": "USD",
            "integration": "bank-transfer",
            "routeType": "ach",
            "merchantAmountType": "percentage",
            "merchantAmount": "8.00",
            "guardrails": {
                "fixed": {"min": "0.00", "max": "2.00"},
                "percentage": {"min": "0.00", "max": "10.00"},
            },
            "percentCap": {"min": "2.00", "max": "75.00"},
            "revenueShareId": "RSRC-123",
        }

    def post(self, endpoint, body):
        self.calls.append(("POST", endpoint, body))
        if endpoint == "/v1/fees/route-pricing/search":
            return {
                "ok": True,
                "fees": [{
                    "currencyCode": "USD",
                    "revenueStream": {
                        "bankTransfer": {
                            "ach": self.revenue_stream,
                        },
                    },
                }],
            }
        return {"ok": True, "revenueStream": self.revenue_stream}


class TestFeesGateway(unittest.TestCase):
    def setUp(self):
        self.gateway = Gateway(Configuration("public", "private"))
        self.client = FakeClient()
        self.client_patch = patch(
            "trolley.configuration.Configuration.client",
            return_value=self.client,
        )
        self.client_patch.start()

    def tearDown(self):
        self.client_patch.stop()

    def test_search_route_pricing_accepts_an_optional_body_and_maps_fees(self):
        all_fees = self.gateway.fees.search_route_pricing()
        usd_fees = self.gateway.fees.search_route_pricing({"currency": "USD"})

        self.assertEqual("USD", all_fees[0].currencyCode)
        self.assertEqual("RSRC-123", all_fees[0].revenueStream["bankTransfer"]["ach"]["revenueShareId"])
        self.assertEqual(all_fees, usd_fees)
        self.assertEqual(
            ("POST", "/v1/fees/route-pricing/search", {}),
            self.client.calls[0],
        )
        self.assertEqual(
            ("POST", "/v1/fees/route-pricing/search", {"currency": "USD"}),
            self.client.calls[1],
        )

    def test_create_revenue_stream_posts_body_and_maps_response(self):
        body = {
            "currencyCode": "USD",
            "integration": "bank-transfer",
            "routeType": "ach",
            "merchantAmountType": "percentage",
            "merchantAmount": "8.00",
            "minPercentCapAmount": "2.00",
            "maxPercentCapAmount": "75.00",
        }

        result = self.gateway.fees.create_revenue_stream(body)

        self.assertEqual("RSRC-123", result.revenueShareId)
        self.assertEqual({"min": "2.00", "max": "75.00"}, result.percentCap)
        self.assertEqual(
            ("POST", "/v1/fees/revenue-stream/create", body),
            self.client.calls[0],
        )

    def test_update_revenue_stream_passes_null_caps_through(self):
        body = {
            "revenueShareId": "RSRC-123",
            "currencyCode": "USD",
            "integration": "bank-transfer",
            "routeType": "ach",
            "merchantAmountType": "percentage",
            "merchantAmount": "9.00",
            "minPercentCapAmount": None,
            "maxPercentCapAmount": None,
        }

        result = self.gateway.fees.update_revenue_stream(body)

        self.assertEqual("USD", result.currencyCode)
        self.assertEqual(
            ("POST", "/v1/fees/revenue-stream/update", body),
            self.client.calls[0],
        )
        self.assertIsNone(self.client.calls[0][2]["minPercentCapAmount"])
        self.assertIsNone(self.client.calls[0][2]["maxPercentCapAmount"])

    def test_fees_are_available_on_the_main_gateway(self):
        self.assertIsInstance(self.gateway.fees, FeesGateway)


if __name__ == "__main__":
    unittest.main()
