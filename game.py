#inport packages to extend (just like we extend sublime, or Atom or  VS code)
from random import randint

#[] => this is an array. An arayis a special  tyep of container  that can hold multiple items\
# arrays are indexed (their content get assigned a number)
# the index always starts at 0
choices =["rock", "paper", "scissors"]




player_lives = 5
computer_lives = 5

total_lives = 5

player = False # True and False are Booleans - data types that can be truthy or falsey

# set up our game loop
while player ==  False:
	#this is the player choice
	print ("===============*/ RPS / *===================")
	print ("Computer Lives:", computer_lives,"/", total_lives)
	print ("Player Lives:", player_lives,"/", total_lives)
	print ("==================================")
	print ("Choose your weapon! or type quit to exit\n")
	player = input ("Choose rock, paper or scissors: \n")

	# if the player chooses to quit, thend ont do anything else
	#just exit the process (kill Python) and quit the game
	if player == "quit":
		print ("You chose to quit, quitter!")
		exit()

	#this will be the AI choice > a random pick grom the choice array
	computer = choices[randint(0, 2)]

	#check to see what the user input

	# print outputs whatever is in the round brackets > in this case it out puts players to the command prompt window
	print ("user chose: " + player)

	# validate that the random choice workd for the AI
	print("AI choice: " + computer)

	if computer == player:
		print("tie")

	elif computer =="rock":
		if player == "scissors":
			player_lives = player_lives - 1
			print("You lose! player lives:", player_lives)
		else:
	   		print("you win!")
	   		computer_lives = computer_lives -1

	elif (computer == "paper"):
		if (player == "scissors"):
			player_lives = player_lives - 1
			print("you lose! player lives:",player_lives)
		else:
	   		print("you win!")
	   		computer_lives = computer_lives -1

	elif (computer == "scissors"):
		if (player == "rock"):
			player_lives = player_lives - 1
			print("you lose! player lives:", player_lives)
		else:
	   		print("you win!")
	   		computer_lives = computer_lives -1

	# check player lives and AI lives
	if player_lives == 0:
		print ("You lost! Loser! Would you like to play again?")
		choice = input ("Y / N")

		if choice == "Y" or choice == "y":
			#reset the game and start over again
			player_lives = 2
			computer_lives = 2
			player = False

		elif choice == "N" or choice =="n":
			# exit message and quit
			print (" You chose to quit. Better luck next time!")
			exit()

		else:

			print ("Make a valid selection - Y or N" )
			#this is generating a bug -> need to fix this check
			choice = input ("Y / N")

	elif computer_lives == 0:
		print ("You won! Winner! Would you like to play again?")
		choice = input ("Y / N")

		if choice == "Y" or choice == "y":
			#reset the game and start over again
			player_lives = 2
			computer_lives = 2
			player = False

		elif choice == "N" or choice =="n":
			# exit message and quit
			print (" You chose to quit. Better luck next time!")
			exit()

		else:

			print ("Make a valid selection - Y or N" )
			#this is generating a bug -> need to fix this check
			choice = input ("Y / N")

	else:
		player = False


