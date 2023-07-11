# https://codemy.com/git

# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 
# python mydb.py
# python manage.py migrate
# python manage.py createsuperuser
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