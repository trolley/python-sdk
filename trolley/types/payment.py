
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
        'withholdingCurrency': ""
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
            'withholdingCurrency'
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
