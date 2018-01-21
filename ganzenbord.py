import random
import playerstats
player1 = playerstats.player(raw_input("Player1, please enter your name\n >"), 0, 0)
player2 = playerstats.player(raw_input("Player2, please enter your name\n >"), 0, 0)
currentPlayer = "potatoes"

def whoStarts():
	"""Throw a single die, highest throw == starting player"""
	global currentPlayer
	global player1
	global player2
	player1.roll(1)
	player2.roll(1)
	
	print "---------------\n%s's throw\n---------------" % player1.name 
	next = raw_input("throw your dice\n")
	print player1.roll1, '\n'
	print "---------------\n%s's throw\n---------------" % player2.name 
	next = raw_input("throw your dice\n")
	print player2.roll1, '\n'
	
	if player1.roll1 > player2.roll1:
		print "%s starts" % player1.name
		currentPlayer = player1
		otherPlayer = player2
		throwingPhase()
	elif player1.roll1 < player2.roll1:
		print "%s starts" % player2.name
		currentPlayer = player2
		throwingPhase()
	else:
		print "That's a draw. Throw again!"
		whoStarts()

def throwingPhase():
	"""Roll dice, check for special start throws, route to appropriate throwing form"""
	global totalRoll
	currentPlayer.roll(2)
	totalRoll = currentPlayer.roll1 + currentPlayer.roll2
	
	print "\n---------------"
	print "%s position:" %(player1.name)
	print(player1.position)
	print "%s position:" %(player2.name)
	print(player2.position)
	print "---------------\n%s's turn" % currentPlayer.name
	next = raw_input("Throw your dice!")
	print "You threw a %d and a %d" %(currentPlayer.roll1, currentPlayer.roll2)
	
	if currentPlayer.position == 0:
		zeroRoll()
	else:
		currentPlayer.position = currentPlayer.position + totalRoll
		print "Move to position %d" %(currentPlayer.position)
		normalThrow()


def playerSwitch():
	"""Check which player may throw, keeps track of special skip turn properties"""
	global currentPlayer
	global player1
	global player2
	
	if currentPlayer == player1 and player2.skipTurn == True:
		print "InTheSkip"
		if player2.position == 31 and currentPlayer.position < 31:
			throwingPhase()
		elif player2.position == 52 and currentPlayer.position < 52:
			throwingPhase()
		elif player2.position == 31 and currentPlayer.position <= 31:
			player2.skipTurn == False
			currentPlayer = player2
			throwingPhase()
		elif player2.position == 52 and currentPlayer.position <= 52:
			player2.skipTurn == False
			currentPlayer = player2
			throwingPhase()
		else:
			player2.skipTurn = False
			throwingPhase()
	
	elif currentPlayer == player1 and player2.skipTurn == False:
		currentPlayer = player2
		throwingPhase()
	
	elif currentPlayer == player2 and player1.skipTurn == True:
		print "InTheSkip"
		if player1.position == 31 and currentPlayer.position < 31:
			throwingPhase()
		elif player1.position == 52 and currentPlayer.position < 52:
			throwingPhase()
		elif player1.position == 31 and currentPlayer.position <= 31:
			player1.skipTurn == False
			currentPlayer = player1
			throwingPhase()
		elif player1.position == 52 and currentPlayer.position <= 52:
			player1.skipTurn == False
			currentPlayer = player1
			throwingPhase()
		else:
			player1.skipTurn = False
			throwingPhase()
	
	elif currentPlayer == player2 and player1.skipTurn == False:
		currentPlayer = player1
		throwingPhase()
	
	else:
		print "Zieke error"

def zeroRoll():
	"""First roll special throws"""
	global currentPlayer
	global player1
	global player2
	global totalRoll
	doubleTime = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
	totalRoll = currentPlayer.roll1 + currentPlayer.roll2
	currentPlayer.position = totalRoll

	if currentPlayer.roll1 == 5 and currentPlayer.roll2 == 4:
		print "You threw the magic combination!!! Move to position 53"
		currentPlayer.position = 53
		playerSwitch()
	elif currentPlayer.roll1 == 4 and currentPlayer.roll2 == 5:
		print "You threw the magic combination!!! Move to position 53"
		currentPlayer.position = 53
		playerSwitch()
	elif currentPlayer.roll1 == 3 and currentPlayer.roll2 == 6:
		print "You threw the almost magic combinatio!! Move to position 26"
		currentPlayer.position = 26
		playerSwitch()
	elif currentPlayer.roll1 == 6 and currentPlayer.roll2 == 3:
		print "ou threw the almost magic combinatio!! Move to position 26"
		currentPlayer.position = 26
		playerSwitch()
	elif currentPlayer.position in doubleTime:
		print "You landed on a goose! Move another %d steps!" %totalRoll
		currentPlayer.position = currentPlayer.position + totalRoll
		playerSwitch()
	elif currentPlayer.position == 6:
		print "You landed on the special 6, move to position 12"
		currentPlayer.position = 12
		playerSwitch()
	else:
		print "Move to position %d" %(currentPlayer.position)
		playerSwitch()

def normalThrow():
	"""Check if player lands on special position"""
	global totalRoll
	totalRoll = currentPlayer.roll1 + currentPlayer.roll2
	doubleTime = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
	
	if currentPlayer.position in doubleTime:
		print "You landed on a goose! Move another %d steps!" %totalRoll
		currentPlayer.position = currentPlayer.position + totalRoll
		playerSwitch()
	elif currentPlayer.position == 19:
		print "You went for a beer in the tavern, wait until the next turn for your hangover to be over!"
		currentPlayer.skipTurn = True
		playerSwitch()
	elif currentPlayer.position == 31:
		print "You fell into a well, stay here until another goose passes!"
		currentPlayer.skipTurn = True
		playerSwitch()
	elif currentPlayer.position == 42:
		print "You got lost in a maze! go back to position 39"
		currentPlayer.position = 39
		playerSwitch()
	elif currentPlayer.position == 52:
		print "This is not your day, you got locked up in jail.. Wait until you get help from another goose!"
		currentPlayer.skipTurn = True
		playerSwitch()
	elif currentPlayer.position == 58:
		print "You died. go back to start"
		currentPlayer.position = 0
		playerSwitch()
	elif currentPlayer.position == 63:
		print(currentPlayer.name)
		print "YOU WON!!"
	elif currentPlayer.position >63:
		stepBack = currentPlayer.position - 63
		print "You passed over 63, go back %d places" %stepBack
		currentPlayer.position = 63 - stepBack
		playerSwitch()
	else:
		playerSwitch()
		
		
whoStarts()
