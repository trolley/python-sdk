from paymentrails.recipient_gateway import RecipientGateway
from paymentrails.balances_gateway import BalancesGateway
from paymentrails.batch_gateway import BatchGateway
from paymentrails.payment_gateway import PaymentGateway
from paymentrails.recipient_account_gateway import RecipientAccountGateway
import paymentrails.configuration


class Gateway(object):
    """
    PaymentRails gateway module
    """

    def __init__(self, config=None, **kwargs):
        if isinstance(config, paymentrails.configuration.Configuration):
            self.config = config
        else:
            self.config = paymentrails.configuration.Configuration(
                public_key=kwargs.get("public_key"),
                private_key=kwargs.get("private_key")
            )
        self.recipient = RecipientGateway(self, config)
        self.balances = BalancesGateway(self, config)
        self.batch = BatchGateway(self, config)
        self.payment = PaymentGateway(self, config)
        self.recipient_account = RecipientAccountGateway(self, config)
