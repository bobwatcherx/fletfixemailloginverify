# NOW I CREATE FLASK SERVER FOR VERIFY EMAIL
# FOR CHANGE is_verified from 0 to 1 in table 
# if 1 is verified and if 0 is not verified


from flask import Flask,request,redirect

import mysql.connector
mydb = mysql.connector.connect(
  host="172.17.0.2",
  user="root",
  password="admin12345",
  database="dbcustomer"
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/verify_email")
def verify_email():
	token = request.args.get('token')
	email = request.args.get('email')
	mycursor = mydb.cursor()

	# AND NOW CHANGE value from 0 to 1 
	sql = "UPDATE fletusers SET verification_token = %s, is_verified = 1 WHERE email = %s "
	val =(token,email)
	mycursor.execute(sql,val)
	mydb.commit()
	print("YOu EMAIL IS SUCCESS VERIFY")
	return redirect("/verify_success")

@app.route("/verify_success")
def verify_success():
	return "you email success verified"
if __name__ == "__main__":
	app.run(debug=True)
