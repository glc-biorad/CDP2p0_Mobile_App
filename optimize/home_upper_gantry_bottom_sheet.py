import flet as ft

class HomeUpperGantryBottomSheet(ft.BottomSheet):
	"""
	Home Upper Gantry Bottom Sheet for the Optimize View
	of the CDP 2.0 Mobile App
	"""
	def __init__(self):
		super().__init__(
			ft.Container(
				ft.Column(
					[
						ft.Text("Home the Upper Gantry"),
						ft.FilledButton(
							text="Home Upper Gantry", 
							style=ft.ButtonStyle(
								color=ft.colors.WHITE,
								bgcolor='#009933',
								shape=ft.buttons.CountinuosRectangleBorder(radius=0),
							),
							on_click=self.home_upper_gantry,
						),
						ft.Text("Home the Upper Gantry Z-Axis"),
						ft.FilledButton(
							text="Home Z-Axis", 
							style=ft.ButtonStyle(
								color=ft.colors.WHITE,
								bgcolor='#009933',
								shape=ft.buttons.CountinuosRectangleBorder(radius=0),
							),
							on_click=self.home_upper_gantry_z_axis,
						),
						ft.Text("Home the Upper Gantry Drip Plate"),
						ft.FilledButton(
							text="Home Drip Plate", 
							style=ft.ButtonStyle(
								color=ft.colors.WHITE,
								bgcolor='#009933',
								shape=ft.buttons.CountinuosRectangleBorder(radius=0),
							),
							on_click=self.home_upper_gantry_drip_plate,
						),
						ft.Text("Home the Upper Gantry Y-Axis"),
						ft.FilledButton(
							text="Home Y-Axis", 
							style=ft.ButtonStyle(
								color=ft.colors.WHITE,
								bgcolor='#009933',
								shape=ft.buttons.CountinuosRectangleBorder(radius=0),
							),
							on_click=self.home_upper_gantry_y_axis,
						),
						ft.Text("Home the Upper Gantry X-Axis"),
						ft.FilledButton(
							text="Home X-Axis", 
							style=ft.ButtonStyle(
								color=ft.colors.WHITE,
								bgcolor='#009933',
								shape=ft.buttons.CountinuosRectangleBorder(radius=0),
							),
							on_click=self.home_upper_gantry_x_axis,
						),
						ft.ElevatedButton('Close', on_click=self.close_bs),
					],
					tight=True,
				),
				padding=10,
			),
			open=True,
			on_dismiss=self.bs_dismissed,
		)

	def close_bs(self, e):
		self.open = False
		self.update()

	def show_bs(self, e):
		e.page.overlay.clear()
		e.page.overlay.append(self)
		self.open = True
		e.page.update()

	def bs_dismissed(self, e):
		print('Dismissed')

	def home_upper_gantry(self, e):
		print("Home the Upper Gantry")

	def home_upper_gantry_z_axis(self, e):
		print("Home the Upper Gantry Z-Axis")

	def home_upper_gantry_y_axis(self, e):
		print("Home the Upper Gantry Y-Axis")

	def home_upper_gantry_x_axis(self, e):
		print("Home the Upper Gantry X-Axis")

	def home_upper_gantry_drip_plate(self, e):
		print("Home the Upper Gantry Drip Plate")
