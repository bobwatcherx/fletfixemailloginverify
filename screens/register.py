from flet import *
from myconnect import mycursor,mydb
import string
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def RegisterView(page):
	nametxt = TextField(label="email")
	passwordtxt = TextField(label="password")


	def generate_token():
		letters = string.ascii_letters
		return ''.join(random.choice(letters) for i in range(10))

	def send_email_verification(email,token):
		subject = "Please Verifify email here"
		body = "EMail verify url here http://localhost:5000/verify_email?token=" + token + "&email=" + email 

		message = MIMEMultipart()
		message['From'] = "noreplayYOuCompany@fake.com"
		message['To'] = email
		message['Subject'] = subject
		message.attach(MIMEText(body,"plain"))

		# NOW FOR SMTP SERVICE I USE mailtrap 
		# FOR TEST SEND EMAIL IF YOU USE GMAIL
		# YOU CAN CHANGE SMTP ADDRESS LIKE USERNAME URL AND PASSWORD
		with smtplib.SMTP("smtp.mailtrap.io",2525) as smtp:
			smtp.login("27b3da367addfa","bc4d9ff24e96cb")
			smtp.sendmail("noreplayYOuCompany@fake.com",email,message.as_string())





	def registermyaccount(e):
		mycursor.execute("SELECT * from fletusers WHERE email = %s",(nametxt.value,))
		result = mycursor.fetchone()
		# NOW I CHECK IF YOU EMAIL ACCOUNT IS ALREADY REGISTER
		# THEN SEND MESSAGE ERRROR
		if result:
			print("YOu email already register ")
			return
		# NOW CREATE RANDOM TOKEN FOR VERIFICATION TOKEN
		token = generate_token()
		sql = "INSERT INTO fletusers (email,password,verification_token) VALUES(%s,%s,%s)"
		val = (nametxt.value,passwordtxt.value,token)
		mycursor.execute(sql,val)
		mydb.commit()

		# NOW I CREATE SEND EMAIL VERIFICATION

		send_email_verification(nametxt.value,token)
		print("success registration")
		page.snack_bar = SnackBar(
				Text("SEE EMAIL IN INBOX",size=30),
				bgcolor="blue"
				)
		page.snack_bar.open = True
		nametxt.value = ""
		passwordtxt.value = ""
		
		page.update()





	return Column([
		Text("You Register",size=30,weight="bold"),
		nametxt,
		passwordtxt,
		ElevatedButton("register my accout",
			bgcolor="blue",color="white",
			on_click=registermyaccount

			),
			ElevatedButton("login now",
			bgcolor="green",color="white",
			on_click=lambda e:page.go("/login")

			),

		])
