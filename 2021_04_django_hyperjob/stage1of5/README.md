Objectives
We need to safely store all the vacancies and resumes in a database. Your first task is to develop data models to manage the database tables.

Use the default settings of the project with the predefined SQLite database.
Throughout the project, we will need at least two models: Vacancy and Resume. Both of them should have description and author fields. The description field is a text field for no more than 1024 symbols and the author field is a foreign key linked to the django.contrib.auth.models.User model.

Define Vacancy and Resume in the models.py module and migrate them to the database.

Follow these steps:
1) In your IDE (I used PyCharm) open 2 folders:
   "resume" and "vacancy" and then in those folders open both "models.py"
   
2) Now, you should have 2 python files open, this is where you'll write your models. Write one class or "model" for each python files (1 vacancy, 1 resume) as we did in the practice exercises. Make sure to import the needed django modules.

3) To reference the ForeignKey(django.contrib.auth.User) you should import by writing "from django.conf import settings" and then write 
"ForeignKey(settings.AUTH_USER_MODEL, ...)" for author.

4) Almost done, finally you need to open your CLI (Terminal on Mac) and write the 2 lines that begin with python manage.py .., and BE SURE that you are in the correct directory using "cd". cd to the correct directory by doing this: cd PycharmProjects --> cd HyperJob Agency --> cd Hyperjob Agency --> cd task --> cd hyperjop. Now you're in the correct directory and can fun "python manage.py ..."

5) At this point you should be done with the first part of the project, but make sure to run over your code and really understand what's happening. Read over the MVC lesson again, because that is what is being implemented here.
