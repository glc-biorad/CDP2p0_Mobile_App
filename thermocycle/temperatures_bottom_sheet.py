import flet as ft

class TemperaturesBottomSheet(ft.BottomSheet):
	"""
	Temperatures BottomSheet allowing the user to set the denature 
	and anneal temperatures for a thermocycler from the ThermocycleView
	within the CDP 2.0 Mobile App
	"""
	def __init__(self, thermocycler: str):
		super().__init__(
			ft.Container(
				ft.Column(
					[
						ft.Text(f"Set the denaturing temperature for Thermocycler {thermocycler}"),
						TemperaturesTextField(mode='denature'),
						ft.Text(f"Set the annealing temperature for Thermocycler {thermocycler}"),
						TemperaturesTextField(mode='anneal'),
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

class TemperaturesTextField(ft.TextField):
	"""
	Temperatures TextField for providing the denature or anneal temp for a 
	given Thermocycler
	"""
	def __init__(self, mode: str):
		if mode == 'denature':
			label = "Denaturing Temperature for Thermocycler A"
			value = 84
		else:
			label = "Annealing Temperature for Thermocycler A"
			value = 55
		super().__init__(
			label=label,
			on_change=self.textbox_changed,
			value=value,
		)

	def textbox_changed(self, e):
		print(self.value)
