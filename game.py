#inport packages to extend (just like we extend sublime, or Atom or  VS code)
from random import randint

#re-import our game variables
from gameComponents import gameVars, winLose





# set up our game loop
while gameVars.gameVars.player ==  False:
	#this is the gameVars.player choice
	print ("===============*/ RPS / *===================")
	print ("Computer Lives:", computer_lives,"/", gameVars.total_lives)
	print ("gameVars.Player Lives:", gameVars.player_lives,"/", gameVars.total_lives)
	print ("==================================")
	print ("Choose your weapon! or type quit to exit\n")
	gameVars.player = input ("Choose rock, paper or scissors: \n")

	# if the gameVars.player chooses to quit, thend ont do anything else
	#just exit the process (kill Python) and quit the game
	if gameVars.player == "quit":
		print ("You chose to quit, quitter!")
		exit()

	#this will be the AI choice > a random pick grom the choice array
	computer = gameVars.choices[randint(0, 2)]

	#check to see what the user input

	# print outputs whatever is in the round brackets > in this case it out puts gameVars.players to the command prompt window
	print ("user chose: " + gameVars.player)

	# validate that the random choice workd for the AI
	print("AI choice: " + computer)

	if computer == gameVars.player:
		print("tie")

	elif computer =="rock":
		if gameVars.player == "scissors":
			gameVars.player_lives = gameVars.player_lives -=1
			print("You lose! gameVars.player lives:", gameVars.player_lives)
		else:
	   		print("you win!")
	   		computer_lives = computer_lives -=1

	elif (computer == "paper"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives = gameVars.player_lives -=1
			print("you lose! gameVars.player lives:",gameVars.player_lives)
		else:
	   		print("you win!")
	   		computer_lives = computer_lives -=1

	elif (computer == "scissors"):
		if (gameVars.player == "rock"):
			gameVars.player_lives -=1
			print("you lose! gameVars.player lives:", gameVars.player_lives)
		else:
	   		print("you win!")
	   		computer_lives = computer_lives -1

	# check gameVars.player lives and AI lives
	if gameVars.player_lives == 0:
		winLose.winorlose("lost")
		# print ("You lost! Loser! Would you like to play again?")
		# choice = input ("Y / N")

		# if choice == "Y" or choice == "y":
		# 	#reset the game and start over again
		# 	gameVars.player_lives = 2
		# 	computer_lives = 2
		# 	gameVars.player = False

		# elif choice == "N" or choice =="n":
		# 	# exit message and quit
		# 	print (" You chose to quit. Better luck next time!")
		# 	exit()

		# else:

		# 	print ("Make a valid selection - Y or N" )
		# 	#this is generating a bug -> need to fix this check
		# 	choice = input ("Y / N")

	elif computer_lives == 0:
		wwinLose.inorlose("won")
		# print ("You won! Winner! Would you like to play again?")
		# choice = input ("Y / N")

		# if choice == "Y" or choice == "y":
		# 	#reset the game and start over again
		# 	player_lives = 2
		# 	computer_lives = 2
		# 	player = False

		# elif choice == "N" or choice =="n":
		# 	# exit message and quit
		# 	print (" You chose to quit. Better luck next time!")
		# 	exit()

		# else:

		# 	print ("Make a valid selection - Y or N" )
		# 	#this is generating a bug -> need to fix this check
		# 	choice = input ("Y / N")

	else:
		player = False


