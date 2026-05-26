
class Payment:
    """
    A class representing Payment object.
    """

    _attributes = {
        'id': "",
        'recipient': "",
        'status': "",
        'returnedAmount': "",
        'sourceAmount': "",
        'sourceCurrency': "",
        'sourceCurrencyName': "",
        'targetAmount': "",
        'targetCurrency': "",
        'targetCurrencyName': "",
        'batch': "",
        'category': "",
        'coverFees': "",
        'currency': "",
        'equivalentWithholdingAmount': "",
        'equivalentWithholdingCurrency': "",
        'estimatedDeliveryAt': "",
        'exchangeRate': "",
        'fees': "",
        'recipientFees': "",
        'fxRate': "",
        'memo': "",
        'externalId': "",
        'failureMessage': "",
        'initiatedAt': "",
        'isSupplyPayment': "",
        'merchantId': "",
        'methodDisplay': "",
        'processedAt': "",
        'createdAt': "",
        'updatedAt': "",
        'merchantFees': "",
        'compliance': "",
        'payoutMethod': "",
        'returnedAt': "",
        'returnedNote': "",
        'returnedReason': "",
        'settledAt': "",
        'tags': "",
        'checkNumber': "",
        'taxBasisAmount': "",
        'taxBasisCurrency': "",
        'taxReportable': "",
        'withholdingAmount': "",
        'withholdingCurrency': "",
        'visibleToRecipient': ""
    }

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            'id',
            'recipient',
            'status',
            'returnedAmount',
            'sourceAmount',
            'sourceCurrency',
            'sourceCurrencyName',
            'targetAmount',
            'targetCurrency',
            'targetCurrencyName',
            'batch',
            'category',
            'coverFees',
            'currency',
            'equivalentWithholdingAmount',
            'equivalentWithholdingCurrency',
            'estimatedDeliveryAt',
            'exchangeRate',
            'fees',
            'recipientFees',
            'fxRate',
            'memo',
            'externalId',
            'failureMessage',
            'initiatedAt',
            'isSupplyPayment',
            'merchantId',
            'methodDisplay',
            'processedAt',
            'createdAt',
            'updatedAt',
            'merchantFees',
            'compliance',
            'payoutMethod',
            'returnedAt',
            'returnedNote',
            'returnedReason',
            'settledAt',
            'tags',
            'checkNumber',
            'taxBasisAmount',
            'taxBasisCurrency',
            'taxReportable',
            'withholdingAmount',
            'withholdingCurrency',
            'visibleToRecipient'
        ]

        for field in fields:
            if attributes.get('payment') is None:
                Payment._attributes[field] = attributes.get(field)
            elif attributes['payment'].get(field) is not None:
                Payment._attributes[field] = attributes['payment'][field]

        return Payment._attributes

    @staticmethod
    def factory(attributes):
        """Creates an instance of Payment and returns it. """
        instance = Payment._initialize(attributes)
        return instance

    @staticmethod
    def find(payment_id, batch_id, term=""):
        from trolley.configuration import Configuration
        if term:
            return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).recipient.get_all_payments(payment_id)
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).payment.find(payment_id, batch_id)

    @staticmethod
    def create(body, batch_id):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).payment.create(body, batch_id)

    @staticmethod
    def update(payment_id, batch_id, body):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).payment.update(payment_id, body, batch_id)

    @staticmethod
    def delete(payment_id, batch_id):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).payment.delete(payment_id, batch_id)

    @staticmethod
    def search(page=1, page_size=10, term=""):
        from trolley.configuration import Configuration
        return Configuration.gateway(Configuration.get_public_key(), Configuration.get_private_key()).payment.search_by_page("", term, page, page_size)
