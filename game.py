#!/usr/bin/env python

from account import Account
from math import ceil
from itertools import cycle
from player import Player
import sys
import argparse

OUT_TEMPLATE = '%s is out of the game.'
SEPARATOR_LENGTH = 20

class DreidelGame(object):

    def __init__(self, players, initial_amount=10, shin_amount=1):
        self.players = players
        self.total_in = len(players)
        self.account = Account()
        self.shin_amount = shin_amount
        self._turn_count = 1
        self.actions = {
            'nun': self.do_nothing,
            'gimel': self.give_all,
            'hey': self.give_half,
            'shin': self.take
        }
        for player in self.players:
            player.account.deposit(initial_amount)
        print 'Starting balances:'
        self.show_balances()
        print '-'*SEPARATOR_LENGTH
        self.ante_up()

    def transfer(self, giver, receiver, amount):
        """Transfer items from giver to receiver."""
        receiver.account.deposit(giver.account.withdraw(amount))

    def ante_up(self):
        """Have each player contribute 1 item to pot."""
        print 'Everyone antes up.'
        for player in self.players:
            if player.account.balance > 0:
                self.transfer(player, self, 1)
                if player.account.balance == 0:
                    self.total_in -= 1
                    print OUT_TEMPLATE % (player,)
        self.show_balances()
        print '-'*SEPARATOR_LENGTH

    def do_nothing(self, player):
        """No-op that represents no change in status of game"""
        return '%s spins \'nun\' and does nothing.' % (player,)

    def give_all(self, player):
        self.transfer(self, player, self.account.balance)
        return '%s spins \'gimel\' and gets everything.' % (player,)
    
    def give_half(self, player):     
        self.transfer(self, player, int(ceil(self.account.balance/2.0)))
        return '%s spins \'hey\' and gets half.' % (player,)
    
    def take(self, player):
        self.transfer(player, self, self.shin_amount)
        return '%s spins \'shin\' and puts in %d.' % (player, self.shin_amount)        
        
    def do_turn(self, player):
        if player.account.balance == 0:
            pass
        else:
            print 'Turn #%d: %s' % (self._turn_count, self.actions[player.spin()](player),)
            if player.account.balance == 0:
                # player is out
                self.total_in -= 1
                print OUT_TEMPLATE % (player,)
            self.show_balances()
            print '-'*SEPARATOR_LENGTH
            self._turn_count += 1
    
    def show_balances(self):
        print 'Pot: %d' % (self.account.balance,)
        for player in self.players:
            balance = player.account.balance
            if balance > 0:
                print '%s: %d' % (player, balance,)

    def play(self):
        player_circle = cycle(self.players)      
        while not ((self.total_in == 1 and self.account.balance == 0) \
        or (self.total_in == 0)):
            current_player = player_circle.next()
            self.do_turn(current_player)
            if self.account.balance <= 1 and self.total_in > 1:
                self.ante_up()
        # TODO: print final status
        # make it part of show_balances?
        if current_player.account.balance > 0:
            print '%s wins!' % (current_player)
                
if __name__ == '__main__':
    #TODO: make this getopts or similar instead;
    # add options for starting amount, shin amount
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--player', dest='players', action='append', required=True)
    parser.add_argument('-i', '--initial_amount', type=int, dest='initial_amount', default=10, choices=range(3,16))
    parser.add_argument('-s', '--shin_amount', type=int, dest='shin_amount', default=1)
    args = parser.parse_args()
    players = [Player(name) for name in args.players]
    initial_amount = int(args.initial_amount)
    shin_amount = int(args.shin_amount)
    game = DreidelGame(players, initial_amount, shin_amount)
    game.play()