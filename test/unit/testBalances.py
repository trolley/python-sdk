import sys
import os
import unittest

sys.path.append(os.path.abspath('.'))

import trolley.configuration
import trolley.balances
from mock import MagicMock, Mock, patch


import trolley.exceptions.notFoundException
import trolley.exceptions.invalidFieldException


def fake_find():
    payload = {"ok": "true", "balances": {"USD": {"primary": "true", "amount": "10000.00",
                                                  "currency": "USD", "type": "paymentrails",
                                                  "accountNumber": "null"}}}
    return payload


class TestBalances(unittest.TestCase):

    def setUp(self):
        self.patcher = patch('paymentrails.balances.Balances.find', fake_find)
        self.patcher.start()

    public_key = ("publickey")
    private_key = ("privatekey")

    def test_retrieve_payoutMethod(self):
        trolley.configuration.Configuration.set_public_key(
            TestBalances.public_key)
        trolley.configuration.Configuration.set_private_key(
            TestBalances.private_key)
        response = trolley.balances.Balances.find()
        status = {"ok": "true", "balances": {"USD": {"primary": "true", "amount": "10000.00",
                                                     "currency": "USD", "type": "paymentrails", "accountNumber": "null"}}}
        self.assertEqual(response, status)


if __name__ == '__main__':
    unittest.main()
