# Write your code here
import random

# List as below is needed in case set of options will be shorter or in different order
winning_cases = {
    'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

player_name = input("Enter your name: ") #  getting player name
print(f"Hello, {player_name}")

players = open("rating.txt").readlines()  #  getting player rating
if player_name in str(players):
	player_rating = int([i.split() for i in players if player_name in i][0][1])
else:
	player_rating = 0

game_moves = input()  # optional new game moves
if game_moves == "":
	moves = ["rock", "paper", "scissors"]
else:
	moves = game_moves.split(",")
print("Okay, let's start")


while True:  # game start here
	player_move = input()
	
	while player_move not in moves + ["!exit", "!rating"]:
		print("Invalid input")
		player_move = input()
	
	if player_move == "!exit":
		break
	if player_move == "!rating":
		print(f"Your rating: {player_rating}")
		continue
	
	computer_move = random.choice(moves)
	
	if player_move == computer_move:
		print(f"There is a draw ({computer_move})")
		player_rating += 50

	elif computer_move in winning_cases[player_move]:
		print(f"Well done. Computer chose {computer_move} and failed")	
		player_rating += 100		
		
	else:
		print(f"Sorry, but computer chose {computer_move}")
		
print("Bye!")
