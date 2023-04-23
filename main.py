from flet import *
# NOW SET URL AND YOU VIEW 
from screens.login import LoginView
from screens.dashboard import DashboardView
from screens.register import RegisterView




def main(page:Page):
	

	def route_change(route):
		# CLEAR SCREEN
		page.views.clear()
		# NOW CREATE URL AAND VIEW
		page.views.append(
			View(
				"/login",
			[
				LoginView(page),
				# NOW I CREATE BUTTON IF YOU NOT LOGIN
				# YOU CANOT ACCESS DASHBOARD BEFORE YOU LOGIN

				ElevatedButton("Go to DAshboard WIthout login",
				on_click=lambda e:page.go("/dashboard")
				)			

			]
				)

			)
		if page.route == "/register":
			page.views.append(
				View(
					"/register",
					[
					RegisterView(page)

					]
				)

				)
		if page.route == "/dashboard":
			# NOW I CREATE CONDITION IF NOT CLIENTS_storage
			# FOUND THEN YOU CANT ACCESS DASH/BOARD
			# THEN YOU BACK AGAIN FOR LOGIN
			if not page.client_storage.get("login"):
				page.go("/login")
				print(page.client_storage.get("login"))
				print(page.route)
				page.update()
			else:
				page.views.append(
				View(
					"/dashboard",
					[
					DashboardView(page)

					]
				)

				)
		# NOW IF ROute is / THEN REDIRECT TO /login
		if page.route == "/":
			page.go("/login")
		page.update()



			

	page.on_route_change = route_change
	page.go(page.route)


flet.app(target=main)
