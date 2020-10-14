# Write your code here
import random
print("H A N G M A N")
comp_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
player_word = list("-" * len(comp_word))
turn = 8
player_letters = []   #  this is just for collecting used letter 
while turn > 0:

    while True:
        print("\n" + "".join(player_word))
        player_letter = input("Input a letter: ")
        

          
        if len(player_letter) > 1:
            print("You should input a single letter")
            continue

        if not player_letter.isalpha():
            print("Please enter a lowercase English letter")
            continue

                       
        if player_letter.isupper() == True:
            print("Please enter a lowercase English letter")
            continue  
                        
        if player_letter in player_letters:
            print("You've already guessed this letter")
            continue
            
        player_letters.append(player_letter)
        break
        
    if player_letter in comp_word:
        player_word = [j if j == player_letter else player_word[i] for i,j in enumerate(comp_word)]
        if not "-" in player_word:
            break
    else:
        print("That letter doesn't appear in the word")
        turn -= 1
                
if "-" in player_word:
    print("You lost!")
else:
    print("You guessed the word!\nYou survived!")
