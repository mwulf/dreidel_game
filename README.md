dreidel_game
============

"I have a little dreidel; I made it out of code...."

This is a small command-line simulation of a round of dreidel,
the spinning-top game traditionally played during the Jewish
holiday of Hanukkah.  For a summary of the rules, see this
Wikipedia article:

    https://en.wikipedia.org/wiki/Dreidel
    
It's meant as a simple example of object-oriented design in
Python.  I originally intended it for a small informal
Python class I was leading for my department at work.
    
The three main files in the project are:

    * account.py: an Account class to keep track of
                  how many items a player (or the "pot")
                  has.
                  
                  test_account.py is a unit-test module
                  for this class.
    
    * player.py:  a simple Player class.  A player has a
                  name and an account.
    
    * game.py:    a class that encapsulates the round.
                  A game has players and an account.
                  It manages the order of the players'
                  turns, the transfer of money between its
                  own account and the players' accounts, and
                  the termination of the round.

Here's a sample run with three players A, B and C.
They each get 3 items at the beginning of the game.
Anyone who spins "shin" must put 1 item into the pot.

>python game.py -p A -p B -p C -i 3 -s 1
Starting balances:
Pot: 0
A: 3
B: 3
C: 3

Everyone antes up.
Pot: 3
A: 2
B: 2
C: 2

Turn #1: A spins 'shin' and puts in 1.
Pot: 4
A: 1
B: 2
C: 2

Turn #2: B spins 'gimel' and gets everything.
Pot: 0
A: 1
B: 6
C: 2

Everyone antes up.
A is out of the game.
Pot: 3
B: 5
C: 1

Turn #3: C spins 'nun' and does nothing.
Pot: 3
B: 5
C: 1

Turn #4: B spins 'hey' and gets half.
Pot: 1
B: 7
C: 1

Everyone antes up.
C is out of the game.
Pot: 3
B: 6

Turn #5: B spins 'shin' and puts in 1.
Pot: 4
B: 5

Turn #6: B spins 'hey' and gets half.
Pot: 2
B: 7

Turn #7: B spins 'hey' and gets half.
Pot: 1
B: 8

Turn #8: B spins 'gimel' and gets everything.
Pot: 0
B: 9

B wins!