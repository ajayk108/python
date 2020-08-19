import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'medicine_system',
)

mycursor = mydb.cursor()

mycursor.execute('show tables')

for data in mycursor:
    print(data)