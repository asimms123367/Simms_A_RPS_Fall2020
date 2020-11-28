
from random import randint


from gameComponents import gameVars, winLose, comparison

while gameVars.player ==  False:

	
	print ("===============*/ RPS / *===================")
	print ("Computer Lives:", gameVars.computer_lives,"/", gameVars.total_lives)
	print ("Player Lives:", gameVars.player_lives,"/", gameVars.total_lives)
	print ("==================================")
	print ("Choose your weapon! or type quit to exit\n")

	gameVars.player = input ("Choose rock, paper or scissors: \n")

	if gameVars.player == "quit":
		print("You chose to quit, quitter!")
		exit()

	

	print("user chose: " + gameVars.player)

	comparison.compvPlayer(gameVars.player)
	

	
	if gameVars.player_lives == 0:
		winLose.winorlose("lost")
		

	elif gameVars.computer_lives == 0:
		 winLose.winorlose("won")
		

	else:
		gameVars.player = False


