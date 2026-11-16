import random

secret_number = random.randint(1, 100)
print("Guess the number from 1 to 100!")

while True:
	try:
		guess = int(input("Your guess: "))
	except ValueError:
		print("Enter a whole number.")
		continue

	if guess < secret_number:
		print("Too low!")
	elif guess > secret_number:
		print("Too high!")
	else:
		print("You got it!")
		break
