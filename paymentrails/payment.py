from paymentrails.configuration import Configuration


class Payment:
    """
    A class that facilitates Client requests to
    the PaymentRails API in regards to Payments.
    """

    _attributes = {
        'id': "",
        'status': "",
        'isSupplyPayment': "",
        'returnedAmount': "",
        'sourceAmount': "",
        'sourceCurrency': "",
        'targetAmount': "",
        'targetCurrency': "",
        'exchangeRate': "",
        'fees': "",
        'recipientFees': "",
        'fxRate': "",
        'memo': "",
        'externalId': "",
        'processedAt': "",
        'createdAt': "",
        'updatedAt': "",
        'merchantFees': "",
        'compliance': "",
        'payoutMethod': "",
    }

    @staticmethod
    def find(payment_id, batch_id):
        """
        Retrieve a payment
            A payment_id and batch_id are required::
            Payment.find('P-dejrtewdsj',B-fjeracjmuflh')
        """
        return Configuration.gateway().payment.find(payment_id, batch_id)

    @staticmethod
    def create(body, batch_id):
        """
        Create a payment
            A body and batch_id are required::
            Payment.create(
               {"recipient":{"id":"R-91XNJBKM30F06"},"sourceAmount":"100.10",
               "memo":"Freelance payment"}
        """
        return Configuration.gateway().payment.create(body, batch_id)

    @staticmethod
    def update(payment_id, body, batch_id):
        """
        Update a payment
            A payment_id, batch_id, and body are required::
            Payment.update('B-fjeracjmuflh',{"sourceAmount":"900.90"},'P-jddfjwojd')
        """
        return Configuration.gateway().payment.update(payment_id, body, batch_id)

    @staticmethod
    def delete(payment_id, batch_id):
        """
        Delete a payment
            A payment_id and batch_id are required::
            Payment.delete('P-dejrtewdsj',B-fjeracjmuflh')
        """
        return Configuration.gateway().payment.delete(payment_id, batch_id)

    @staticmethod
    def search(page=1, page_number=10, term=""):
        """
        Query for a payment
            Payment.search(1,10,'test')
        """
        return Configuration.gateway().payment.search(page, page_number, term)

    @staticmethod
    def _initialize(attributes):
        """Initialize fields and return a dict of attributes."""

        fields = [
            'id',
            'status',
            'isSupplyPayment',
            'returnedAmount',
            'sourceAmount',
            'sourceCurrency',
            'targetAmount',
            'targetCurrency',
            'exchangeRate',
            'fees',
            'recipientFees',
            'fxRate',
            'memo',
            'externalId',
            'processedAt',
            'createdAt',
            'updatedAt',
            'merchantFees',
            'compliance',
            'payoutMethod',
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
