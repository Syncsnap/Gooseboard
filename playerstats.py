import random

class player:
	def __init__(self, name, roll1, roll2):
		self.position = 0
		self.skipTurn = False
		self.name = name
		self.roll1 = roll1
		self.roll2 = roll2
		self.totalRoll = roll1 + roll2

	def getName(self):
		return '{}'.format(self.name)

	def roll(self, nr_of_dice):
		global roll1
		global roll2
		self.roll1 = random.randint(1,6)
		self.roll2 = random.randint(1,6)