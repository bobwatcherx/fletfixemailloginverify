import mysql.connector
mydb = mysql.connector.connect(
  host="172.17.0.2",
  user="root",
  password="admin12345",
  database="dbcustomer"
)

mycursor = mydb.cursor()