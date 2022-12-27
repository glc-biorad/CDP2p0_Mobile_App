import flet as ft

class ClampsBottomSheet(ft.BottomSheet):
	"""
	Clamps BottomSheet allowing the user to lower and raise the heaters for
	the thermocyclers from the ThermocycleView
	within the CDP 2.0 Mobile App
	"""
	def __init__(self):
		super().__init__(
			ft.Container(
				ft.Column(
					[
						ft.Text(value="Select the Clamp"),
						ft.Dropdown(
							label='Clamp',
							hint_text="Select the Clamp to control",
							options=[
								ft.dropdown.Option('A'),
								ft.dropdown.Option('B'),
								ft.dropdown.Option('C'),
								ft.dropdown.Option('D'),
							],
							autofocus=True,
						),
						ft.Row(
							[
								ft.FilledButton(
									text="Raise Clamp (Home)", 
									style=ft.ButtonStyle(
										color=ft.colors.WHITE,
										bgcolor='#009933',
										shape=ft.buttons.CountinuosRectangleBorder(radius=0),
									),
									on_click=self.on_click
								),
								ft.FilledButton(
									text="Lower Clamp", 
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
