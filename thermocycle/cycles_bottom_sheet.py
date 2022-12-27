import flet as ft

class CyclesBottomSheet(ft.BottomSheet):
	"""
	Cycles BottomSheet allowing the user to set the number of 
	cycles for a thermocycler from the ThermocycleView
	within the CDP 2.0 Mobile App
	"""
	def __init__(self, thermocycler: str):
		super().__init__(
			ft.Container(
				ft.Column(
					[
						ft.Text(f"Set the number of cycles for Thermocycler {thermocycler}"),
						CyclesTextField(),
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

class CyclesTextField(ft.TextField):
	"""
	Cycles TextField or providing the number of cycles for a 
	gien Thermocycler
	"""
	def __init__(self):
		super().__init__(
			label="Cycles for Thermocycler A",
			on_change=self.textbox_changed,
			value=40,
		)

	def textbox_changed(self, e):
		print(self.value)
