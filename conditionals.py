# set up a varibale, check its value, and then go down some different paths depending on the ourcome

#cast our user input - which by default


temperature = int(input("input a value between 0 and 100: ")



if (temperature <= 4):
	#water is frozen
	print ("water's state is solid (ice)")
elif (temperature < 100): 
	# water is liquid
	print ("water's state is liquid")
else:
	# water is boiling, so it's steam
	print("water is vapor")
