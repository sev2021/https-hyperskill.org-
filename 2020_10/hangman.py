# Write your code here
import random
print("H A N G M A N\n")
comp_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
player_word = list("-" * len(comp_word))
turn = 8
while turn > 0:
    print("\n" + "".join(player_word))
    
    if not "-" in player_word:
        break
    player_letter = input("Input a letter:")
    
    if player_letter in comp_word:
        if player_letter in player_word:
            print("No improvements")
            turn -= 1
        player_word = [j if j == player_letter else player_word[i] for i,j in enumerate(comp_word)]
    else:
        print("That letter doesn't appear in the word")
        turn -= 1
                
if "-" in player_word:
    print("You lost!")
else:
    print("You guessed the word!\nYou survived!")
