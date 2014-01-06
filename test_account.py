import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account()
    
    def test_deposit(self):
        self.account.deposit(1)
        self.assertEqual(self.account.balance, 1)
        
    def test_withdraw_less_than_balance(self):
        self.account.deposit(2)
        amount = self.account.withdraw(1)
        self.assertEqual( (amount,self.account.balance), (1,1) )
        
    def test_withdraw_equal_to_balance(self):
        self.account.deposit(1)
        amount = self.account.withdraw(1)
        self.assertEqual( (amount,self.account.balance), (1,0) )

    def test_withdraw_more_than_balance(self):
        self.account.deposit(1)
        amount = self.account.withdraw(2)
        self.assertEqual( (amount,self.account.balance), (1,0) )
        
if __name__ == '__main__':
    unittest.main()