from gameComponents import gameVars
# Defining a win or lose function
def winorlose(status):


	if status == "won":
		pre_message = "You are the yuuuuuuugest winner ever! "
	else:
		pre_message = "You done trumped it, loser! "

	print(pre_message + "Would you like to play again?")
	
	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":
		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False

	elif choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice - Y or N")
		choice = input("Y / N")
		if choice == "Y" or choice == "y":
			gameVars.player_lives = 5
			gameVars.computer_lives = 5
			gameVars.player = False
		else:
			print("You chose to quit. Better luck next time!")
			exit()

		