# Austin Lindgren
# Period 1
# Dice Rolling Simulator

# random.randint(1,6)

import random

print("Welcome to the Dice Rolling Simulator!")
# Asks the player for how many times they would like to roll the dice
NumRolls = int(input("How many times do you want to roll the dice: "))

# Variables defined
Reroll = 1
Count1s = 0
Count2s = 0
Count3s = 0
Count4s = 0
Count5s = 0
Count6s = 0

while Reroll <= NumRolls:
	# Generates the result for roll of the die.
	RollResult = random.randint(1,6)
	if RollResult == 1:
		# Outputs the current roll and the roll result
		print("Roll " + str(Reroll) + ": " + str(RollResult))
		Reroll += 1
		Count1s += 1
	elif RollResult == 2:
		print("Roll " + str(Reroll) +  ": " + str(RollResult))
		Reroll += 1
		Count2s += 1
	elif RollResult == 3:
		print("Roll " + str(Reroll) + ": " + str(RollResult))
		Reroll += 1
		Count3s += 1
	elif RollResult == 4:
		print("Roll " + str(Reroll) + ": " + str(RollResult))
		Reroll += 1
		Count4s += 1
	elif RollResult == 5:
		print("Roll " + str(Reroll) + ": " + str(RollResult))
		Reroll += 1
		Count5s += 1
	else:
		print("Roll " + str(Reroll) + ": " + str(RollResult))
		Reroll += 1
		Count6s += 1

#Percentage's Calculated
Num1sPercentage = int(Count1s) / int(NumRolls)
Num2sPercentage = int(Count2s) / int(NumRolls)
Num3sPercentage = int(Count3s) / int(NumRolls)
Num4sPercentage = int(Count4s) / int(NumRolls)
Num5sPercentage = int(Count5s) / int(NumRolls)
Num6sPercentage = int(Count6s) / int(NumRolls)

#Make blank line
print('\n')
# Outputs the total number of time the dice was rolled
print("Total Number of Rolls: " + str(NumRolls))
print('\n')
# Outputs the number of times a number was rolled
print("Number of times a number was rolled:")
print("Number of 1s rolled: " + str(Count1s))
print("Number of 2s rolled: " + str(Count2s))
print("Number of 3s rolled: " + str(Count3s))
print("Number of 4s rolled: " + str(Count4s))
print("Number of 5s rolled: " + str(Count5s))
print("Number of 6s rolled: " + str(Count6s))
print('\n')
# Outputs the percentage of each number that has been rolled
print("The percentage of each number that has been rolled:")
print("Percentage of 1s rolled: " + str(Num1sPercentage))
print("Percentage of 2s rolled: " + str(Num2sPercentage))
print("Percentage of 3s rolled: " + str(Num3sPercentage))
print("Percentage of 4s rolled: " + str(Num4sPercentage))
print("Percentage of 5s rolled: " + str(Num5sPercentage))
print("Percentage of 6s rolled: " + str(Num6sPercentage))