from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ee = create_engine('sqlite:///flashcard.db?check_same_thread=False')  # dont use echo here or get Failed
Base = declarative_base()

class MyClass(Base):                # create database layont
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    first_column = Column(String)
    second_column = Column(String)

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
                new_q = input("Question:\n")
            while not new_a:
                new_a = input("Answer:\n")

            # step 2 of 4 below sqlite
            new_data = MyClass(first_column=new_q, second_column=new_a)
            session.add(new_data)
            session.commit()

        else:
            print(f"{player_add} is not an option")


def practice_card():

    result_list = session.query(MyClass).all()

    if result_list == []:
        print("There is no flashcard to practice!")
        return
    
    for i in range(len(result_list)):
        print(f"Question: {result_list[i].first_column}")
        player_see = input('Please press "y" to see the answer or press "n" to skip:\n')
        
        if player_see == "n":
            continue
        
        elif player_see == "y":
            print(f"Answer: {result_list[i].second_column}")
            
        else:
            print(f"{player_main} is not an option")


Session = sessionmaker(bind=ee)
session = Session()
while True:
    player_main = input("1. Add flashcards\n2. Practice flashcards\n3. Exit\n")
    
    if player_main == "3":
        print("Bye!")
        break
    
    elif player_main == "2":
        practice_card()
    
    elif player_main == "1":
        add_card()
    
    else:
        print(f"{player_main} is not an option")
