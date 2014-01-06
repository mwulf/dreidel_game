#!/usr/bin/env python

"""Player in dreidel game.

A player has an account and can spin a dreidel.
"""

from account import Account
from random import randint

# lookup for letter names
DREIDEL_SIDES = ['nun','gimel','hey','shin']

class Player(object):
    """Represents player in game."""

    def __init__(self, name):
        """Name the player and set him/her up with zero-balance account."""
        self._name = name
        self.account = Account()
        
    @property
    def name(self):
        return self._name
        
    def __str__(self):
        """Special method to make it easier to print player's name."""
        return self._name
        
    def spin(self):
        """Spin dreidel and return the name of the letter it lands on.
        
        Looks up letter name based on random integer between 0 and 3.
        """
        return DREIDEL_SIDES[randint(0,3)]