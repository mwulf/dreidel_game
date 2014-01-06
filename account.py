#!/usr/bin/env python

"""Account that corresponds to a pile of items in a dreidel game.

This is a simple Account class to keep track of
    * the number of items a player has
    * the number of items in the communal "pot"

It handles the basic deposit and withdrawal actions.
It does not allow for a negative balance:
if you try to overdraw against the account,
you get the full balance and no more.
"""

class Account(object):
    def __init__(self):
        """Create account and set initial balance to 0."""
        self._balance = 0
    
    @property
    def balance(self):
        """Get current balance."""
        return self._balance
        
    def deposit(self, n):
        """Add n items to balance."""
        self._balance += n
        
    def withdraw(self, n):
        """Withdraw as many of n items as possible from account.
        
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