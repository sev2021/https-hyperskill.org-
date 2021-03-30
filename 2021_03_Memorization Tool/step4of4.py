from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ee = create_engine('sqlite:///flashcard.db?check_same_thread=False')
Base = declarative_base()

class MyClass(Base):                # create database layont
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    first_column = Column(String)
    second_column = Column(String)
    third_column = Column(Integer)    # step 4 of 4 - test-sessions

Base.metadata.create_all(ee)    # create database from layout


def add_card():
    while True:
        player_add = input("1. Add a new flashcard\n2. Exit\n")
        
        if player_add == "2":
            break
        
        elif player_add == "1":
            new_q = ""
            new_a = ""
            while not new_q:
                new_q = input("\nQuestion:\n")
            while not new_a:
                new_a = input("Answer:\n")
            print()

            # step 2 of 4 below sqlite
            new_data = MyClass(first_column=new_q, second_column=new_a, third_column=1)  # step 4 of 4 - test-sessions
            session.add(new_data)
            session.commit()

        else:
            print(f"\n{player_add} is not an option\n")


def practice_card(try_run):    # step 4 of 4 - test-sessions

    result_list = session.query(MyClass).all()

    if result_list == []:
        print("There is no flashcard to practice!\n")
        return
    
    for i in range(len(result_list)):
        if result_list[i].third_column > try_run:    # step 4 of 4 - test-sessions
            continue

        print(f"\nQuestion: {result_list[i].first_column}")
        player_see = input('press "y" to see the answer:\npress "n" to skip:\npress "u" to update:\n')
        print("")

        if player_see == "y":                       # step 4 of 4 - print answer if asked
            print(f"\nAnswer: {result_list[i].second_column}")

        if player_see in "yn":                      # step 4 of 4 - check either answer printed or not
            player_answer = input('press "y" if your answer is correct:\npress "n" if your answer is wrong:\n')
            print("")

            if player_answer == "n":
                result_list[i].third_column = 1
                session.commit()

            elif player_answer == "y":
                result_list[i].third_column += 1
                if result_list[i].third_column > 3:
                    session.delete(result_list[i])
                session.commit()

            else:
                print(f"{player_answer} is not an option")

        elif player_see == "u":
            player_update = input('press "d" to delete the flashcard:\npress "e" to edit the flashcard:\n')
            print("")

            if player_update == "e":
                player_update_q = input(f'current question: {result_list[i].first_column}\nplease write a new question:\n')
                print("")
                player_update_a = input(f'current answer: {result_list[i].second_column}\nplease write a new answer:\n')
                print("")
                result_list[i].first_column = player_update_q
                result_list[i].second_column = player_update_a
                session.commit()

            elif player_update == "d":
                session.delete(result_list[i])
                session.commit()

            else:
                print(f"{player_update} is not an option")

        elif player_see not in "ynu":
            print(f"{player_see} is not an option")


Session = sessionmaker(ee)     # binding to database (bind=ee)
session = Session()
try_run = 0                    # step 4 of 4 - test-sessions
while True:
    player_main = input("1. Add flashcards\n2. Practice flashcards\n3. Exit\n")


    if player_main == "3":
        print("Bye!")
        break
    
    elif player_main == "2":
        try_run += 1
        practice_card(try_run)       # step 4 of 4 - test-sessions
    
    elif player_main == "1":
        add_card()
    
    else:
        print(f"{player_main} is not an option\n")
