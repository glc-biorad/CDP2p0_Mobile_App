import flet as ft

class MotionBottomSheet(ft.BottomSheet):
	"""
	Motion BottomSheet allowing the user to specify where to move the pipettor
	for the Build Protocol View within the CDP 2.0 Mobile App
	"""
	def __init__(self):
		super().__init__(
			ft.Container(
				ft.Column(
					[
						ft.Text(value="Select the Consumable"),
						ft.Dropdown(
							label='Consumable',
							hint_text="Select the Consumable",
							options=[
								ft.dropdown.Option("Sample Rack"),
								ft.dropdown.Option("Reagent Cartridge"),
								ft.dropdown.Option("Heater/Shaker"),
								ft.dropdown.Option("Mag Separator"),
								ft.dropdown.Option("Assay Strip"),
								ft.dropdown.Option("Chiller"),
								ft.dropdown.Option("Pre-Amp Thermocycler"),
								ft.dropdown.Option("Quant Strip"),
								ft.dropdown.Option(' '),
							],
							autofocus=True,
						),
						ft.Text(value="Select the Tray"),
						ft.Dropdown(
							label='Tray',
							hint_text="Select the Tray",
							options=[
								ft.dropdown.Option('A'),
								ft.dropdown.Option('B'),
								ft.dropdown.Option('C'),
								ft.dropdown.Option('D'),
								ft.dropdown.Option(' '),
							],
						),
						ft.Text(value="Select the Column"),
						ft.Dropdown(
							label='Column',
							hint_text="Select the Column",
							options=[
								ft.dropdown.Option('1'),
								ft.dropdown.Option('2'),
								ft.dropdown.Option('3'),
								ft.dropdown.Option('4'),
								ft.dropdown.Option('5'),
								ft.dropdown.Option('6'),
								ft.dropdown.Option('7'),
								ft.dropdown.Option('8'),
								ft.dropdown.Option('9'),
								ft.dropdown.Option('10'),
								ft.dropdown.Option('11'),
								ft.dropdown.Option('12'),
								ft.dropdown.Option(' '),
							],
							autofocus=True,
						),
						ft.Text(value="Select the Tip"),
						ft.Dropdown(
							label='Tip',
							hint_text="Select the Tip",
							options=[
								ft.dropdown.Option('1000'),
								ft.dropdown.Option('50'),
								ft.dropdown.Option('200'),
							],
							autofocus=True,
						),
						ft.ElevatedButton('Add', on_click=self.on_click),
						ft.ElevatedButton('Close', on_click=self.close_bs),
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
		print('Add to protocol')
