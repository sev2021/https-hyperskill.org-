def g():
	# Added access to results file "rating.txt"
	#
	# Form of the file:
	#
	# Tim 350
	# Jane 200
	# Alex 400
	#
	
	import random

	moves = ["rock", "paper", "scissors", "!exit", "!rating"]
	winner = ["rockscissors", "paperrock", "scissorspaper"]

	player_name = input("Enter your name: ")
	print(f"Hello, {player_name}")

	players = open("rating.txt").readlines()

	if player_name in str(players):
		player_rating = int([i.split() for i in players if player_name in i][0][1])
	else:
		player_rating = 0

	while True:
		player = input()

		while player not in moves:
			print("Invalid input")
			player = input()

		if player == "!exit":
			break
		if player == "!rating":
			print(f"Your rating: {player_rating}")
			continue

		computer = random.choice(moves[:3])

		if player == computer:
			print(f"There is a draw ({computer})")
			player_rating += 50
		elif (player + computer) in winner:
			print(f"Well done. Computer chose {computer} and failed")	
			player_rating += 100
		else:
			print(f"Sorry, but computer chose {computer}")

	print("Bye!")
