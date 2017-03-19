#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 Pig Dice Game"""

import random

#---------------------Here we starting a game by choosing yes on the question-----------------------------
def startNewGame():
	start = raw_input("Start New Game? Y or N ->  ")
	if start == 'Y' or start == 'y' or start == 'Yes' or start == 'yes':
		Gamer1 = Gamer()
		Gamer2 = Gamer()
		die = Dice()
		newgame = Game(Gamer1,Gamer2,die)

#------------------This function gives us an option to either hold the dice of roll it--------------------
class Dice():
	def __init__(x):
		x.value = int()
		seed = 0
	def roll(x):
		x.value = random.randint(1,6)


class Gamer():
	def __init__(x):
		x.Gamers_turn = False
		x.roll = True
		x.hold = False
		x.score = 0
	
	def choose(x):
		choice = raw_input('%s: Please type (h) for Hold or (r) for Roll? ' % x.name)
		choice = str(choice)
		if choice == 'h':
			x.hold = True
			x.roll = False
		elif choice == 'r':
			x.hold = False
			x.roll = True
		else:
			print('You have entered an incorrect input. Please enter (h) for Hold or (r) for Roll')
			x.choose()

#---------------------------This function let us know who will go first-------------------------------------
class Game():
	def __init__(x,Gamer1,Gamer2,die):
		x.ts = 0
		x.die = die
		x.Gamer1 = Gamer1
		x.Gamer2 = Gamer2
		x.Gamer1.score = 0
		x.Gamer2.score = 0
		x.Gamer1.name = "1st player"
		x.Gamer2.name = "2nd player"
		
		CoinFlip = random.randint(1,2)
		if CoinFlip == 1:
			x.current_Gamer = Gamer1
			print "1st player will start first"
		elif CoinFlip == 2:
			x.current_Gamer = Gamer2
			print "2nd player will start first"
		else:
			print "Error, please try again later"
		x.Gamers_turn()

#------------------------------This function let us know what is our score------------------------------------
	def Gamers_turn(x):
		print "1st player score is:", x.Gamer1.score				
		print "2nd player score is:", x.Gamer2.score
		x.die.roll()
		if(x.die.value == 1):
			print "Upps... You got 1! Your score is 0!"
			x.ts = 0
			x.Next()
		else:
			x.ts = x.ts + x.die.value
			print "Rolling result is:",x.die.value
			print "Total score is:", x.ts
			x.current_Gamer.choose()
			if(x.current_Gamer.hold == True and x.current_Gamer.roll == False):
				x.current_Gamer.score = x.current_Gamer.score + x.ts
				x.Next()
			elif(x.current_Gamer.hold == False and x.current_Gamer.roll == True):
				x.Gamers_turn()

#---------------------This function let us who won the game and total score of the winner----------------------
	def Next(x):
		x.ts = 0
		if x.Gamer1.score >= 100:
			print "1st player won. Congratulations!"
			print "Your total score is:",x.Gamer1.score
			x.End()
			startNewGame()
		elif x.Gamer2.score >= 100:
			print "2nd player won. Congratulations!"
			print "Your total score is:",x.Gamer2.score
			x.End()
			startNewGame()
		else:
			if x.current_Gamer == x.Gamer1:
				x.current_Gamer = x.Gamer2
			elif x.current_Gamer == x.Gamer2:
				x.current_Gamer = x.Gamer1
			else:
				print "Error, please try again later"

			print "New Gamers_turn, player is now:", x.current_Gamer.name
			x.Gamers_turn()
		
	def End(x):
		x.Gamer1 = None
		x.Gamer2 = None
		x.die = None
		x.ts = None
		
startNewGame()
