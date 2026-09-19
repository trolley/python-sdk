from urllib.parse import quote

import trolley.configuration


class PartnerGateway(object):
    """Trolley partner settings processor."""

    def __init__(self, gateway, config):
        self.gateway = gateway
        self.config = gateway.config

    def _client(self):
        return trolley.configuration.Configuration.client(self.config)

    def get_fees(self, currency=None):
        endpoint = '/v1/fees'
        if currency:
            endpoint += '?currency={}'.format(quote(currency, safe=''))
        return self._client().get(endpoint)

    def update_fees(self, body):
        return self._client().patch('/v1/fees', body)

    def list_payout_methods(self):
        return self._client().get('/v1/payout-methods')

    def get_payout_method(self, payout_method):
        return self._client().get(
            '/v1/payout-methods/{}'.format(quote(payout_method, safe=''))
        )

    def update_payout_method(self, payout_method, body):
        return self._client().patch(
            '/v1/payout-methods/{}'.format(quote(payout_method, safe='')),
            body
        )

    def get_processing_settings(self):
        return self._client().get('/v1/processing-settings')

    def update_processing_settings(self, body):
        return self._client().patch('/v1/processing-settings', body)

    def get_white_label_dns_records(self):
        return self._client().get('/v1/white-label/dns-records')

    def verify_white_label_dns_records(self):
        return self._client().post('/v1/white-label/dns-records/verify', {})

    def delete_white_label_email(self):
        return self._client().delete('/v1/white-label/email')

    def update_white_label_icon(self, body):
        return self._client().patch('/v1/white-label/icon', body)

    def get_white_label_settings(self):
        return self._client().get('/v1/white-label')

    def update_white_label_settings(self, body):
        return self._client().patch('/v1/white-label', body)

    def get_widget_configuration(self):
        return self._client().get('/v1/iframe/config')

    def update_widget_configuration(self, body=None):
        return self._client().post('/v1/iframe/config', body or {})
