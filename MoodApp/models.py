from django.db import models

class happy_database(models.Model):
    author = models.TextField()
    phrase = models.TextField()
    authorPic = models.TextField()

class sad_database(models.Model):
    author = models.TextField()
    phrase = models.TextField()
    authorPic = models.TextField()

class angry_database(models.Model):
    author = models.TextField()
    phrase = models.TextField()
    authorPic = models.TextField()

class nervous_database(models.Model):
    author = models.TextField()
    phrase = models.TextField()
    authorPic = models.TextField()

# Start:
# 1- py manage.py shell
# 2- from MoodApp.models import DataBase

# Adding to the table:
# 1- add = DataBase(author='Emil', phrase='Refsnes')
# 2- add.save()

# Add Multiple Records
"""
member1 = Members(firstname='Tobias', lastname='Refsnes')
member2 = Members(firstname='Linus', lastname='Refsnes')
member3 = Members(firstname='Lene', lastname='Refsnes')
member4 = Members(firstname='Stale', lastname='Refsnes')
members_list = [member1, member2, member3, member4]
for x in members_list:
x.save()
"""

# Check the table values
# DataBase.objects.all().values()

# After creating new table:
# python manage.py migrate --run-syncdbpy
# manage.py makemigrations MoodApp
# python manage.py sqlmigrate MoodApp 0001
# Copy the line and creat a new sqlite3 table with the same structures and name
# python manage.py migrate

# After changing anything in the tabels from the terminal:
# python manage.py makemigrations MoodApp
# python manage.py migrate MoodApp
