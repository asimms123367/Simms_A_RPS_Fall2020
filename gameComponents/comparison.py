from gameComponents import gameVars, winLose
from random import randint

def compvPlayer(status):

	computer = gameVars.choices [randint (0, 2)]
	print("computer choice: " + computer)


	if (computer == gameVars.player):
		print("tie")

	elif (computer == "rock"):
		if gameVars.player == "scissors":
			gameVars.player_lives -= 1
			print("You lose! player lives: ", gameVars.player_lives)
		else:
	   		print("you win!")
	   		gameVars.computer_lives -=1

	elif (computer == "paper"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives -=1
			print("you lose! player lives: ", gameVars.player_lives)
		else:
	   		print("you win!")
	   		gameVars.computer_lives -=1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			gameVars.player_lives -=1
			print("you lose! player lives: ", gameVars.player_lives)
		else:
	   		print("you win!")
	   		gameVars.computer_lives -= 1