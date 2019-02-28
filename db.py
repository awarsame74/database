import mysql.connector

mydb= mysql.connector.connect(
	host= "localhost",
	user= "root",
	passwd= "1234",
	#Specify the Database
    database= "newdb",
	)

#Create Cursor Instance
my_cursor= mydb.cursor()

#Create a Database
#my_cursor.execute("CREATE DATABASE newdb")

# Create Customer Table
#my_cursor.execute("CREATE TABLE customer (uid INTEGER AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), age INTEGER, gender VARCHAR(255), occupation VARCHAR(255), username VARCHAR(255), country VARCHAR(255), email VARCHAR(255), phone VARCHAR(255))")

sqlStuff= "INSERT INTO customer(firstname, lastname, age, gender, occupation, username, country, email, phone) VALUES (%s, %s, %s, %s, %s,%s, %s,%s, %s)" 
record1= ("Terry", "James", 19, "male", "Student", "TJames", "England", "TJ@email.com", "075339876549")

#my_cursor.execute(sqlStuff, record1)
#mydb.commit()

# Create Purchase Table
#my_cursor.execute("CREATE TABLE purchase (paymentid INTEGER AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), date VARCHAR(15), time VARCHAR(10), cardholder_name VARCHAR(255), cardnumber VARCHAR(255), expirydate VARCHAR(255))")

sqlStuff= "INSERT INTO purchase(username, date, time, cardholder_name, cardnumber, expirydate) VALUES (%s, %s, %s, %s, %s, %s)" 
record2= ("TJames", "28/02/2019", "12:03","Terry", "2385828492982", "9/12/22" )

#my_cursor.execute(sqlStuff, record2)
#mydb.commit()

# Create Product Table
#my_cursor.execute("CREATE TABLE product (productid INTEGER PRIMARY KEY, product_name VARCHAR(255), product_price VARCHAR(255), product_type VARCHAR(255))")

sqlStuff= "INSERT INTO product(productid, product_name, product_price, product_type) VALUES (%s, %s, %s, %s)" 
record3= (1228, "Fitness App", "3.99","Software")

#my_cursor.execute(sqlStuff, record3)
#mydb.commit()
