from flet import *
from myconnect import mycursor,mydb

def DashboardView(page):

	def logoutnow(e):
		# NOW REMOVE CLIENT STORAGE AND REDIRECT TO /login
		page.client_storage.remove("login")
		page.go("/login")
		print(page.route)
		page.update()

	def backtologin(e):
		if page.client_storage.get("login") is not None:
			page.go("/dashboard")
			page.snack_bar = SnackBar(
				Text("YOU CANt to login Before you logout",size=30),
				bgcolor="red"
				)
			page.snack_bar.open = True
			page.update()
		else:
			page.go("/login")
		page.update()

	return Column([
		Text("YOu in Dashboard Now",size=30,weight="bold"),
		ElevatedButton("logout",
			bgcolor="red",color="white",
			on_click=logoutnow
			),

		# NOW I CREATE BUTTON TO /login IF YOU AFTER LOGIN
		# IF YOU AFTER LOGIN THEN BACK AGAIN TO LOGIN
		# YOU CANNOT BACK TO LOGIN BEFORE YOU LOGOUT BUTTON
		ElevatedButton("Back TO Login",
			bgcolor="red",color="white",
			on_click=backtologin
			),


		])
