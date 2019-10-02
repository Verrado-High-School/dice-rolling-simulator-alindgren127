# Austin Lindgren
# Period 1
# Dice Rolling Simulator

# random.randint(1,6)

import random

print("Welcome to the Dice Rolling Simulator!")
# Asks the player for how many times they would like to roll the dice
NumRolls = int(input("How many times do you want to roll the dice: "))
Reroll = 1

while Reroll <= NumRolls:
	# Generates the result for roll of the die.
	RollResult = random.randint(1,6)
	if RollResult == 1:
		print("1")
		Reroll += 1
	elif RollResult == 2:
		print("2")
		Reroll += 1
	elif RollResult == 3:
		print("3")
		Reroll += 1
	elif RollResult == 4:
		print("4")
		Reroll += 1
	elif RollResult == 5:
		print("5")
		Reroll += 1
	else:
		print("6")
		Reroll += 1

# Outputs the total number of time the dice was rolled
print("Total Number of Rolls: " + str(NumRolls))
# Make a blank line
print('\n')
# Outputs the number of times a number was rolled
print("Number of times a number was rolled:")
# in loop = output what number roll rolled what example (roll 2: 5)
# in loop = keep count of result (number of 4s rolled: 38)
# output = total number of times a number is rolled (var NumCount)
# output = the precentage of each number that has been rolled (car NumPercentage)