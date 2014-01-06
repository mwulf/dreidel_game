#!/usr/bin/env python
from account import Account
from random import randint

DREIDEL_SIDES = ['nun','gimel','hey','shin']

class Player(object):
    """Represents player in game."""

    def __init__(self, name):
        self._name = name
        self.account = Account()
        
    @property
    def name(self):
        return self._name
        
    def __str__(self):
        return self._name
        
    def spin(self):
        return DREIDEL_SIDES[randint(0,3)]
        
        
        