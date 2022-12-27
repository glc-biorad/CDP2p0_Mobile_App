import flet as ft

class OtherBottomSheet(ft.BottomSheet):
	"""
	Other BottomSheet allowing the user to specify actions
	for the Build Protocol View within the CDP 2.0 Mobile App
	"""
	def __init__(self):
		super().__init__(
			ft.Container(
				ft.Column(
					[
						ft.Text(value="Select the Action"),
						ft.Dropdown(
							label='Action',
							hint_text="Select the Action",
							options=[
								ft.dropdown.Option("Home Pipettor"),
								ft.dropdown.Option("Move Lid 1"),
								ft.dropdown.Option("Move Lid 2"),
								ft.dropdown.Option("Move Lid 3"),
								ft.dropdown.Option("Move Lid 4"),
								ft.dropdown.Option("Move Chip 1"),
								ft.dropdown.Option("Move Chip 2"),
								ft.dropdown.Option("Move Chip 3"),
								ft.dropdown.Option("Move Chip 4"),
								ft.dropdown.Option("Generate Standard Droplets and Load - DG8 1000"),
								ft.dropdown.Option("Generate Standard Droplets and Load - DG8 0100"),
								ft.dropdown.Option("Generate Standard Droplets and Load - DG8 0010"),
								ft.dropdown.Option("Generate Standard Droplets and Load - DG8 0001"),
								ft.dropdown.Option("Generate Pico Droplets and Load - DG8 1000"),
								ft.dropdown.Option("Generate Pico Droplets and Load - DG8 0100"),
								ft.dropdown.Option("Generate Pico Droplets and Load - DG8 0010"),
								ft.dropdown.Option("Generate Pico Droplets and Load - DG8 0001"),
								ft.dropdown.Option("Transfer Plasma"),
								ft.dropdown.Option("Binding"),
								ft.dropdown.Option("Pooling"),
								ft.dropdown.Option("Wash 1"),
								ft.dropdown.Option("Wash 2"),
								ft.dropdown.Option("Pre-Elution"),
								ft.dropdown.Option("Elution"),
								ft.dropdown.Option("Extraction"),
								ft.dropdown.Option("Pre-Amp"),
								ft.dropdown.Option("Enrichment"),
								ft.dropdown.Option("Assay Prep"),
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
