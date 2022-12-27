import flet as ft

class ConfigureRelativeMovesBottomSheet(ft.BottomSheet):
	"""
	Configure Relative Moves Bottom Sheet for the Optimize View
	of the CDP 2.0 Mobile App
	"""
	def __init__(self):
		super().__init__(
			ft.Container(
				ft.Column(
					[
						ft.Text("Set the distance to move relative along the X-axis in microsteps"),
						ConfigureRelativeMovesTextField('x'),
						ft.Text("Set the distance to move relative along the Y-axis in microsteps"),
						ConfigureRelativeMovesTextField('y'),
						ft.Text("Set the distance to move relative along the Z-axis in microsteps"),
						ConfigureRelativeMovesTextField('z'),
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

class ConfigureRelativeMovesTextField(ft.TextField):
	"""
	Configure Relative Moves TextField for setting the relative move amount
	for a given direction within the Optimize View for the CDP 2.0 Mobile App
	"""
	def __init__(self, axis: str):
		self.axis = axis
		if axis.lower() == 'x':
			val = 500
		elif axis.lower() == 'y':
			val = 5000
		elif axis.lower() == 'z':
			val = 5000
		super().__init__(
			label=f'd{axis.lower()}',
			value=val,
			on_change=self.textbox_changed,
		)

	def textbox_changed(self, e):
		e.page.session.set(f'd{self.axis.lower}_ug', self.value)
