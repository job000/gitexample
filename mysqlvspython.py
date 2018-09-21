import mysql.connector


mydb = mysql.connector.connect(

	host = "localhost",
	user = "root",
	passwd = "otico"
	)

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE PYTHONDATA")


mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x)
