import flet as ft

class TraysBottomSheet(ft.BottomSheet):
	"""
	Trays BottomSheet allowing the user to open and close trays for
	the thermocyclers from the ThermocycleView
	within the CDP 2.0 Mobile App
	"""
	def __init__(self):
		super().__init__(
			ft.Container(
				ft.Column(
					[
						ft.Text(value="Select the Tray"),
						ft.Dropdown(
							label='Tray',
							hint_text="Select the Tray to control",
							options=[
								ft.dropdown.Option('AB'),
								ft.dropdown.Option('CD'),
							],
							autofocus=True,
						),
						ft.Row(
							[
								ft.FilledButton(
									text="Home Tray", 
									style=ft.ButtonStyle(
										color=ft.colors.WHITE,
										bgcolor='#009933',
										shape=ft.buttons.CountinuosRectangleBorder(radius=0),
									),
									on_click=self.on_click
								),
								ft.FilledButton(
									text="Close Tray", 
									style=ft.ButtonStyle(
										color=ft.colors.WHITE,
										bgcolor='#009933',
										shape=ft.buttons.CountinuosRectangleBorder(radius=0),
									),
									on_click=self.on_click
								),
							],
						),
						ft.ElevatedButton('Close', on_click=self.close_bs)
					],
					tight=True,
				),
				padding=10,
			),
			open=True,
			on_dismiss=self.bs_dismissed,
		)

	def bs_dismissed(self, e):
		print('Dismissed')

	def show_bs(self, e):
		e.page.overlay.clear()
		e.page.overlay.append(self)
		self.open = True
		e.page.update()

	def close_bs(self, e):
		self.open = False
		self.update()

	def on_click(self, e):
		print('clicked')
