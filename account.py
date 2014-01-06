#!/usr/bin/env python

class Account(object):
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        """Get current balance."""
        return self._balance
        
    def deposit(self, n):
        """Add amount n to balance."""
        self._balance += n
        
    def withdraw(self, n):
        """Withdraw as much of amount n as possible from balance.
        
        If n <= balance, subtract n from balance and return n.
        If n > balance, record old balance and set balance to 0;
        return old balance."""
        
        if n <= self._balance:
            self._balance -= n
            return n
        # if we get this far, n must be greater than balance
        balance_before_withdrawal = self._balance
        self._balance = 0
        return balance_before_withdrawal