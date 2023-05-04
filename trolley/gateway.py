from trolley.recipient_gateway import RecipientGateway
from trolley.balances_gateway import BalancesGateway
from trolley.batch_gateway import BatchGateway
from trolley.payment_gateway import PaymentGateway
from trolley.recipient_account_gateway import RecipientAccountGateway
import trolley.configuration


class Gateway(object):
    """
    Trolley gateway module
    """

    def __init__(self, config=None, **kwargs):
        if isinstance(config, trolley.configuration.Configuration):
            self.config = config
        else:
            self.config = trolley.configuration.Configuration(
                public_key=kwargs.get("public_key"),
                private_key=kwargs.get("private_key")
            )
        self.recipient = RecipientGateway(self, config)
        self.balances = BalancesGateway(self, config)
        self.batch = BatchGateway(self, config)
        self.payment = PaymentGateway(self, config)
        self.recipient_account = RecipientAccountGateway(self, config)