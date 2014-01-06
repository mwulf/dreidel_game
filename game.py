#!/usr/bin/env python

"""Dreidel game.

The dreidel-game object controls a round of dreidel.
It has a list of players and its own account of items (the "pot").
"""

from account import Account
from player import Player
from math import ceil
from itertools import cycle
import sys
import argparse

OUT_TEMPLATE = '%s is out of the game.'
SEPARATOR_LENGTH = 20

class DreidelGame(object):

    def __init__(self, players, initial_amount=10, shin_amount=1):
        """Set up the game."""
        
        # validate the numeric arguments:
        # initial amount has to be at least 2,
        # or everyone will go out when they ante up:
        if initial_amount < 2:
            raise ValueError, "initial_amount must be at least 2"
        if shin_amount < 1:
            raise ValueError, "shin_amount must be at least 1"
            
        # get the list of players and keep track of how many are active
        self.players = players
        self.total_in = len(players)
        
        # create a zero-balance account: this is the "pot"
        self.account = Account()
        
        # set the amount that a player spinning "shin" must put in
        self.shin_amount = shin_amount
        
        # start counting turns
        self._turn_count = 1
        
        # map dreidel letters to corresponding methods
        self.actions = {
            'nun': self.do_nothing,
            'gimel': self.give_all,
            'hey': self.give_half,
            'shin': self.take
        }
        
        # deal the same initial amount of items to everyone;
        # show the initial status of everyone's balance
        for player in self.players:
            player.account.deposit(initial_amount)
        print 'Starting balances:'
        self.show_balances()
        print '-'*SEPARATOR_LENGTH
        
        # have everyone put one item in the pot to start the game off
        self.ante_up()

    def transfer(self, giver, receiver, amount):
        """Transfer items from giver to receiver."""
        
        # Try to withdraw the full amount from the giver.
        # This will be either the amount or the giver's full balance.
        # Whatever the result, deposit it to the receiver's account.
        receiver.account.deposit(
            giver.account.withdraw(amount)
        )

    def ante_up(self):
        """Have each player contribute 1 item to pot."""
        print 'Everyone antes up.'
        
        # Any player with a non-zero balance must put in one item.
        # If the player then has a zero balance, the player is out.
        for player in self.players:
            if player.account.balance > 0:
                self.transfer(player, self, 1)
                if player.account.balance == 0:
                    self.total_in -= 1
                    print OUT_TEMPLATE % (player,)
         
        # show updated status of everyone's balance 
        self.show_balances()
        print '-'*SEPARATOR_LENGTH

    def do_nothing(self, player):
        """Player has spun "nun"; this is a no-op."""
        return '%s spins \'nun\' and does nothing.' % (player,)

    def give_all(self, player):
        """Player has spun "gimel" and gets everything in the pot."""
        self.transfer(self, player, self.account.balance)
        return '%s spins \'gimel\' and gets everything.' % (player,)
    
    def give_half(self, player):
        """Player has spun "hey" and gets half of the pot, rounded up."""
        self.transfer(
            self,
            player,
            int(ceil(self.account.balance/2.0))
        )
        return '%s spins \'hey\' and gets half.' % (player,)
    
    def take(self, player):
        """Player has spun "shin" and has to put in a certain amount."""
        self.transfer(player, self, self.shin_amount)
        return '%s spins \'shin\' and puts in %d.' % (player,
                                                      self.shin_amount)
        
    def do_turn(self, player):
        """Have player spin dreidel and do what the dreidel says to do."""
        
        # if the player is out, skip the turn
        if player.account.balance == 0:
            pass
        else:
            # look up method based on dreidel spin;
            # pass player as argument to method;
            # print the result message along with the turn number
            print 'Turn #%d: %s' % (self._turn_count,
                                    self.actions[player.spin()](player),)
                                    
            # if the player ran out of items, the player is out;
            # decrement the number of active players.
            if player.account.balance == 0:
                self.total_in -= 1
                print OUT_TEMPLATE % (player,)
                
            # show updated status of everyone's balance
            self.show_balances()
            print '-'*SEPARATOR_LENGTH
            
            # increment the number of turns
            self._turn_count += 1
    
    def show_balances(self):
        """Display what everyone has, skipping players who are out."""
        print 'Pot: %d' % (self.account.balance,)
        for player in self.players:
            balance = player.account.balance
            if balance > 0:
                print '%s: %d' % (player, balance,)

    def play(self):
        """Play a round of dreidel.
        
        Go around the circle.
        Each player spins and does what the dreidel says.
        If the communal pot is empty and more than one player is left,
            everyone antes up.
        Round stops
            * when one player has everything, or
            * when everyone has gone out
        """
        
        # cycle through the list of players
        player_circle = cycle(self.players)

        # play until one of the two terminating conditions is met        
        while not ((self.total_in == 1 and self.account.balance == 0) \
        or (self.total_in == 0)):
            # the next player in the circle takes a turn
            current_player = player_circle.next()
            self.do_turn(current_player)
            
            # if the pot is empty, everyone antes up
            if self.account.balance <= 1 and self.total_in > 1:
                self.ante_up()
                
        # Play has stopped, which means that the current player won,
        # or that the current player is the last to go out.
        # A non-zero balance indicates a winner.
        
        if current_player.account.balance > 0:
            print '%s wins!' % (current_player)
        else:
            print 'Everyone is out of the game.'
                
if __name__ == '__main__':

    # read command-line args
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--player', dest='players', action='append',
                        required=True)
    parser.add_argument('-i', '--initial_amount', type=int,
                        dest='initial_amount', default=10,
                        choices=range(3,16))
    parser.add_argument('-s', '--shin_amount', type=int, dest='shin_amount', default=1)
    args = parser.parse_args()
    
    # set up the arguments for the game constructor
    players = [Player(name) for name in args.players]
    initial_amount = args.initial_amount
    shin_amount = args.shin_amount
    
    # create the game
    try:
        game = DreidelGame(players, initial_amount, shin_amount)
    except ValueError, e:
        print 'ValueError: %s' % e
        sys.exit(1)
        
    # play the game
    game.play()