





choices =["rock", "paper", "scissors"]

#this is the player choice
player = input("choose rock, paper or scissors: ")

#this will be the AI choice > a random pick grom the choice array
computer = choices[randint(0, 2)]

#check to see what the user input

# print outputs whatever is in the round brackets > in this case it out puts players to the command prompt window
print ("user chose: " + player)

# validate that the random choice workd for the AI
print("AI choice: " + computer)

if (computer ==player):
	print("tie")

elif(computer =="rock"):
	if(player == "scissors")
	   print("you lose!")
	else:
	   print("you win!")

elif (computer == "paper"):
	if (player == "scissors"):
		print("you lose!")
	else:
		print("you win!")
