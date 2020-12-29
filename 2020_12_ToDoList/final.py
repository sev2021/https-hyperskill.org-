# Write your code here
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(engine)


def add_task(task_name, task_time=datetime.now().date()):
    session = Session()
    new_row = Table(task=task_name, deadline=task_time)
    session.add(new_row)
    session.commit()
    session.close()


def get_tasks():
    session = Session()
    rows = session.query(Table).all()
    session.close()
    return rows


def delete_task(task_name, task_time):
    session = Session()
    rows = session.query(Table).filter(Table.task == task_name, Table.deadline == task_time).all()
    session.delete(rows[0])
    session.commit()
    session.close()


# app starts here
while True:
    inp = input("\n1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit\n")
    if inp == "1":
        today = datetime.now().date()
        print(f"Today {today.strftime('%d %b')}:")
        task_count = 0
        for i in get_tasks():
            if i.deadline == today:
                task_count += 1
                print(task_count, ". ", i.task)
        if task_count == 0:
            print("Nothing to do!")

    elif inp == "2":
        today = datetime.now().date()
        for i in range(7):
            print(f'\n{(today + timedelta(days=i)).strftime("%A %d %b")}:')
            task_count = 0
            for j in get_tasks():
                if j.deadline == today + timedelta(days=i):
                    task_count += 1
                    print(f"{task_count}. {j.task}")
            if task_count == 0:
                print("Nothing to do!")

    elif inp == "3":
        print("\nAll tasks:")
        task_count = 0
        tasklist = {}
        for i in get_tasks():
            task_count += 1
            tasklist[i.deadline] = f'{task_count}. {i.task}. {i.deadline.strftime("%#d %b")}'
        if task_count == 0:
            print("Nothing to do!")
        else:
            for i in sorted(tasklist.keys()):
                print(tasklist[i])

    elif inp == "4":
        print("\nMissed tasks:")
        task_count = 0
        task_missed = 0
        tasklist = {}
        for i in get_tasks():
            task_count += 1
            tasklist[i.deadline] = f'{task_count}. {i.task}. {i.deadline.strftime("%#d %b")}'
        for i in sorted(tasklist.keys()):
            if i < datetime.now().date():
                task_missed += 1
                print(tasklist[i])
        if task_count == 0:
            print("Nothing is missed!")

    elif inp == "5":
        inp_task = input("\nEnter task\n")
        inp_time = input("Enter deadline\n")
        add_task(inp_task, datetime.strptime(inp_time, '%Y-%m-%d'))
        print("The task has been added!")

    elif inp == "6":
        print("\nChoose the number of the task you want to delete:")
        task_count = 0
        tasklist = {}
        for i in get_tasks():
            task_count += 1
            tasklist[i.deadline] = f'{task_count}. {i.task}. {i.deadline.strftime("%#d %b")}'
        if task_count == 0:
            print("Nothing to delete!")
        else:
            task_count = 0
            for i in sorted(tasklist.keys()):
                print(tasklist[i])
            inp = int(input())
            for i in get_tasks():
                task_count += 1
                if inp == task_count:
                    delete_task(i.task, i.deadline)
                    print("The task has been deleted!")

    elif inp == "0":
        break
print("Bye!")
