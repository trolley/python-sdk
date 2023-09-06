import sys
import os
import unittest

sys.path.append(os.path.abspath('.'))

from TestSetup import TestSetup


class BalanceTest(unittest.TestCase):

    client = None

    def setUp(self):
        self.client = TestSetup.getClient()

    def test_balances(self):
        balances = self.client.balances.get_trolley_balance()
        for b in balances:
            self.assertEqual(b.type, 'paymentrails')

        balances = self.client.balances.get_paypal_balance()
        for b in balances:
            self.assertEqual(b.type, 'paypal')

        balances = self.client.balances.get_all_balances()
        for b in balances:
            self.assertTrue((b.type == 'paypal' or b.type == 'paymentrails'))

if __name__ == '__main__':
    unittest.main()
