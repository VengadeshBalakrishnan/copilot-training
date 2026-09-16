import unittest


def combine_account_balances(first_balance, second_balance):
    return first_balance + second_balance


class TestCombineAccountBalances(unittest.TestCase):
    def test_basic_balance_combination(self):
        self.assertEqual(combine_account_balances(200, 300), 500)

    def test_withdrawal_offset(self):
        self.assertEqual(combine_account_balances(-100, 100), 0)

    def test_zero_balances(self):
        self.assertEqual(combine_account_balances(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
