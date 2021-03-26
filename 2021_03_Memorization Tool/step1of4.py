# write your code here

def add_card(questions_answers):
    while True:
        player_add = input("1. Add a new flashcard\n2. Exit\n")
        
        if player_add == "2":
            break
        
        elif player_add == "1":
            new_q = ""
            new_a = ""
            while not new_q:
                new_q = input("Question:\n")
            while not new_a:
                new_a = input("Answer:\n")
            questions_answers[new_q] = new_a

        else:
            print(f"{player_add} is not an option")


def practice_card(questions_answers):
    
    if questions_answers == {}:
        print("There is no flashcard to practice!")
        return
    
    for q,a in questions_answers.items():
        print(f"Question: {q}")
        player_see = input('Please press "y" to see the answer or press "n" to skip:\n')
        
        if player_see == "n":
            continue
        
        elif player_see == "y":
            print(f"Answer: {a}")
            
        else:
            print(f"{player_main} is not an option")


questions_answers = {}
while True:
    player_main = input("1. Add flashcards\n2. Practice flashcards\n3. Exit\n")
    
    if player_main == "3":
        break
    
    elif player_main == "2":
        practice_card(questions_answers)
    
    elif player_main == "1":
        add_card(questions_answers)
    
    else:
        print(f"{player_main} is not an option")
    
print("Bye!")
