#!/usr/bin/env python

"""
Unit tests for Account class.

Tests exercise deposit/withdrawal functionality.
"""
import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        """Each test should start with a zero-balance account."""
        self.account = Account()
    
    def test_deposit(self):
        """Deposit of n items correctly increases balance."""
        self.account.deposit(1)
        self.assertEqual(self.account.balance, 1)
        
    def test_withdraw_less_than_balance(self):
        """Withdrawal less than balance correctly lowers balance."""
        self.account.deposit(2)
        amount = self.account.withdraw(1)
        self.assertEqual( (amount,self.account.balance), (1,1) )
        
    def test_withdraw_equal_to_balance(self):
        """Withdrawal equal to balance yields balance, sets balance to 0."""
        self.account.deposit(1)
        amount = self.account.withdraw(1)
        self.assertEqual( (amount,self.account.balance), (1,0) )

    def test_withdraw_more_than_balance(self):
        """Withdrawal more than balance yields balance, sets balance to 0."""
        self.account.deposit(1)
        amount = self.account.withdraw(2)
        self.assertEqual( (amount,self.account.balance), (1,0) )
        
if __name__ == '__main__':
    unittest.main()