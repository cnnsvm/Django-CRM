# https://codemy.com/git

# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 
# python mydb.py
# python manage.py migrate
# python manage.py createsuperuser
#git add .
# git commit -am 'Initial Commit'
#  Create a new repository in github'
# git remote add origin https://github.com/cnnsvm/Django-CRM.git
# git branch -M main
# git push -u origin main
# python manage.py runserver
# super user Girija
#pwd Weekend@2023
# edit "dcrm/urls.py" file
#localhost:8000/admin


import mysql.connector

dataBase = mysql.connector.connect(
 host='localhost',
 user='root',
 passwd='Weekend@2023' 

)

#Prepare a cursor object
cursorobject = dataBase.cursor()

#Create a databse
cursorobject.execute('CREATE DATABASE elderco')

print("All done")