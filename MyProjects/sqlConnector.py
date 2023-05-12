import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="my_database"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE my_database")   # Create database

# mycursor.execute("SHOW DATABASES")    # Show databases    
# for x in mycursor:                


# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")   # Create table

query = "select * from employees"   # Show tables
# mycursor.execute("DESC TABLES")    # Show tables
mycursor.execute(query)
result = mycursor.fetchall()
for x in result:
    print(x)

mycursor.close()
mydb.close()