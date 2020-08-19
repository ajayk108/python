import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = 'medicine_system'
)
print("connected successful")

mycursor = mydb.cursor()

# mycursor.execute('USE medicine_system')
mycursor.execute('show tables')
for data in mycursor:
    print(data)
    
mycursor.execute("select * from users")
for data in mycursor:
    print(data)
