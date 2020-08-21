def g():
	import random

	moves = ["rock", "paper", "scissors", "!exit", "!rating"]
	winner = ["rockscissors", "paperrock", "scissorspaper"]
	playerp = 0
	
	while True:
		player = input()
		
		while player not in moves:
			print("Invalid input")
			player = input()
		
		if player == "!exit":
			break
		if player == "!rating":
			print(f"Your rating: {playerp}")
			playerp += 50
			continue
		
		computer = random.choice(moves[:3])
		print(player, "-", computer, "-", playerp)
		
		if player == computer:
			print(f"There is a draw ({computer})")
		elif (player + computer) in winner:
			print(f"Well done. Computer chose {computer} and failed")	
			playerp += 100
		else:
			print(f"Sorry, but computer chose {computer}")
	print("Bye!")
