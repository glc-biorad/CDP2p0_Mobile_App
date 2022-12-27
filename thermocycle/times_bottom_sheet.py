import flet as ft

class TimesBottomSheet(ft.BottomSheet):
	"""
	Times BottomSheet allowing the user to set the denature 
	and anneal times for a thermocycler from the ThermocycleView
	within the CDP 2.0 Mobile App
	"""
	def __init__(self, thermocycler: str):
		super().__init__(
			ft.Container(
				ft.Column(
					[
						ft.Text(f"Set the initial denature time for Thermocycler {thermocycler} in minutes"),
						TimesTextField(mode='initial'),
						ft.Text(f"Set the denature time for Thermocycler {thermocycler} in seconds"),
						TimesTextField(mode='denature'),
						ft.Text(f"Set the anneal time for Thermocycler {thermocycler} in seconds"),
						TimesTextField(mode='anneal'),
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

class TimesTextField(ft.TextField):
	"""
	Times TextField for providing the denature or anneal times for a 
	given Thermocycler
	"""
	def __init__(self, mode: str):
		if mode == 'denature':
			label = "Denature Time for Thermocycler A (seconds)"
			value = 30
		elif mode == 'anneal':
			label = "Anneal Time for Thermocycler A (seconds)"
			value = 40
		else:
			label = "Initial Denature Time for Thermocycler A (minutes)"
			value = 3
		super().__init__(
			label=label,
			on_change=self.textbox_changed,
			value=value,
		)

	def textbox_changed(self, e):
		print(self.value)
