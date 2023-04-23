from flet import *
from myconnect import mycursor,mydb




def LoginView(page):
	nametxt = TextField(label="email")
	passwordtxt = TextField(label="password")


	def is_email_verified(email):
		mycursor.execute("SELECT  is_verified from fletusers WHERE email = %s ",(nametxt.value,))
		result = mycursor.fetchone()
		# IF is_verified = 1 IS YOU EMAIL VERIFIFY
		# IF 0 YOU EMAIL NOT VERIED AND CANNOT LOGIN
		if result[0] == 1:
			return True
		else:
			return False





	def processlogin(e):
		mycursor.execute("SELECT * from fletusers WHERE email = %s AND PASSWORD = %s ",(nametxt.value,passwordtxt.value))
		result = mycursor.fetchone()
		
		if result is None:
			print("YOu email password wrong")
			page.snack_bar = SnackBar(
				Text("Wrong Email Password",size=30),
				bgcolor="red"
				)
			page.snack_bar.open = True
			page.update()
		if not is_email_verified(nametxt.value):
			print("YOU EMAIL NOT VERIFIED")

			page.snack_bar = SnackBar(
				Text("EMail Not Verify",size=30),
				bgcolor="red"
				)
			page.snack_bar.open = True
			page.update()

		# NOW IF YOU SUCCESS LOGIN THEN REDIRECT 
		# TO PAGE DASHBOARD
		if result:
			print(result)
			get_token = result[4]
			# AND TO DASHBPARD
			page.go("/dashboard")

			page.client_storage.set("login",get_token)

		page.update()








		# AND NOW CHECK IF YOU EMAIL IS NOT VERIFY
		# THEN SEND MESSAGE ERROR YOU MAIL NOT VERIFIED






	return Column([
		Text("you login page",size=30,weight="bold"),
		nametxt,
		passwordtxt,
		ElevatedButton("login now",
			bgcolor="green",color="white",
			on_click=processlogin
			),
		# AND CREATE BUTTON REGISTER BUTTON
		Row([
			TextButton("no Have Account register now",
			on_click=lambda e:page.go("/register")
			),
			],alignment="center")

		# FOR TEST I FORCE GO TO DASHBOARRD WITHOUT LOGIN

		])