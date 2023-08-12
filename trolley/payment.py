from trolley.configuration import Configuration
from trolley.gateway import Gateway

class Payment:
    """
    A class that facilitates Client requests to
    the Trolley API in regards to Payments.
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
    def find(payment_id, batch_id):
        """
        Retrieve a payment
            A payment_id and batch_id are required::
            Payment.find('P-dejrtewdsj',B-fjeracjmuflh')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key)
        return Gateway(config).payment.find(payment_id, batch_id)

    @staticmethod
    def create(body, batch_id):
        """
        Create a payment
            A body and batch_id are required::
            Payment.create(
               {"recipient":{"id":"R-91XNJBKM30F06"},"sourceAmount":"100.10",
               "memo":"Freelance payment"}
        """
        config = Configuration(Configuration.public_key, Configuration.private_key)
        return Gateway(config).payment.create(body, batch_id)

    @staticmethod
    def update(payment_id, body, batch_id):
        """
        Update a payment
            A payment_id, batch_id, and body are required::
            Payment.update('B-fjeracjmuflh',{"sourceAmount":"900.90"},'P-jddfjwojd')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key)
        return Gateway(config).payment.update(payment_id, body, batch_id)

    @staticmethod
    def delete(payment_id, batch_id):
        """
        Delete a payment
            A payment_id and batch_id are required::
            Payment.delete('P-dejrtewdsj',B-fjeracjmuflh')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key)
        return Gateway(config).payment.delete(payment_id, batch_id)

    @staticmethod
    def search(page=1, page_number=10, term=""):
        """
        Query for a payment
            Payment.search(1,10,'test')
        """
        config = Configuration(Configuration.public_key, Configuration.private_key)
        return Gateway(config).payment.search(page, page_number, term)

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
