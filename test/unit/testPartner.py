import unittest
from unittest.mock import MagicMock, patch

from trolley.configuration import Configuration


class TestPartnerGateway(unittest.TestCase):

    @patch('trolley.partner_gateway.trolley.configuration.Configuration.client')
    def test_dedicated_partner_methods_call_expected_endpoints(self, client_factory):
        client = MagicMock()
        client_factory.return_value = client
        partner = Configuration.gateway('access', 'secret').partner
        body = {'enabled': True}

        partner.get_fees()
        partner.update_fees(body)
        partner.list_payout_methods()
        partner.get_payout_method('bank-transfer')
        partner.update_payout_method('bank-transfer', body)
        partner.get_processing_settings()
        partner.update_processing_settings(body)
        partner.get_white_label_dns_records()
        partner.verify_white_label_dns_records()
        partner.delete_white_label_email()
        partner.update_white_label_icon(body)
        partner.get_white_label_settings()
        partner.update_white_label_settings(body)
        partner.get_widget_configuration()
        partner.update_widget_configuration(body)

        self.assertEqual([
            unittest.mock.call('/v1/fees'),
            unittest.mock.call('/v1/payout-methods'),
            unittest.mock.call('/v1/payout-methods/bank-transfer'),
            unittest.mock.call('/v1/processing-settings'),
            unittest.mock.call('/v1/white-label/dns-records'),
            unittest.mock.call('/v1/white-label'),
            unittest.mock.call('/v1/iframe/config'),
        ], client.get.call_args_list)
        self.assertEqual([
            unittest.mock.call('/v1/fees', body),
            unittest.mock.call('/v1/payout-methods/bank-transfer', body),
            unittest.mock.call('/v1/processing-settings', body),
            unittest.mock.call('/v1/white-label/icon', body),
            unittest.mock.call('/v1/white-label', body),
        ], client.patch.call_args_list)
        self.assertEqual([
            unittest.mock.call('/v1/white-label/dns-records/verify', {}),
            unittest.mock.call('/v1/iframe/config', body),
        ], client.post.call_args_list)
        client.delete.assert_called_once_with('/v1/white-label/email')


if __name__ == '__main__':
    unittest.main()
