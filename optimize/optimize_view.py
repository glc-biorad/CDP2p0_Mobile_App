import flet as ft

import sys
sys.path.append("..")

from app_bar import AppBar

from optimize.configure_relative_moves_bottom_sheet import ConfigureRelativeMovesBottomSheet
from optimize.home_upper_gantry_bottom_sheet import HomeUpperGantryBottomSheet

OPTIMIZE_VIEW_ROUTE = "/optimize"

class OptimizeView(ft.View):
	"""
	Optimize View of the CDP 2.0 Mobile App
	"""
	route = OPTIMIZE_VIEW_ROUTE
	def __init__(self):
		super().__init__(
			self.route,
			[
				AppBar(title=ft.Text("CDP 2.0 - Optimize")),
				OptimizeListView(),
				OptimizeGestureContainer(),
			],
		)

class OptimizeListView(ft.ListView):
	"""
	Optimize ListView containing all the FilledButtons and 
	Dropdowns for the OptimizeView
	"""
	def __init__(self):
		# ListView Parameters
		self.consumable = None
		self.tray = None
		self.column = None
		# Bottom Sheets
		self.configure_relative_moves_bottom_sheet = ConfigureRelativeMovesBottomSheet()
		self.home_upper_gantry_bottom_sheet = HomeUpperGantryBottomSheet()
		super().__init__(
			expand=1,
			spacing=10,
			padding=10,
			controls=[
				ft.Container(
					ft.Column(
						[
							ft.Dropdown(
								label='Consumable',
								hint_text="Select the Consumable",
								options=[
									ft.dropdown.Option("Reagent Cartridge"),
									ft.dropdown.Option("Tip Tray"),
									ft.dropdown.Option("Quant Strip"),
									ft.dropdown.Option("Sample Rack"),
									ft.dropdown.Option("Aux Heater"),
									ft.dropdown.Option("Heater/Shaker"),
									ft.dropdown.Option("Mag Separator"),
									ft.dropdown.Option("Chiller"),
									ft.dropdown.Option("Pre-Amp Thermocycler"),
									ft.dropdown.Option("Lid Tray"),
									ft.dropdown.Option("Tip Transfer Tray"),
									ft.dropdown.Option("Assay Strip"),
								],
								on_change=self.on_change_dropdown,
								autofocus=True,
							),
							ft.Row(
								[
									ft.Dropdown(
										label='Tray',
										hint_text="Select the Tray",
										options=[
											ft.dropdown.Option("A"),
											ft.dropdown.Option("B"),
											ft.dropdown.Option("C"),
											ft.dropdown.Option("D"),
											ft.dropdown.Option(" "),
										],
										on_change=self.on_change_dropdown,
										expand=1,
									),
									ft.Dropdown(
										label='Column',
										hint_text="Select the Column",
										options=[
											ft.dropdown.Option("1"),
											ft.dropdown.Option("2"),
											ft.dropdown.Option("3"),
											ft.dropdown.Option("4"),
											ft.dropdown.Option("5"),
											ft.dropdown.Option("6"),
											ft.dropdown.Option("7"),
											ft.dropdown.Option("8"),
											ft.dropdown.Option("9"),
											ft.dropdown.Option("10"),
											ft.dropdown.Option("11"),
											ft.dropdown.Option("12"),
											ft.dropdown.Option(" "),
										],
										on_change=self.on_change_dropdown,
										expand=1,
									),
								],
								alignment = ft.MainAxisAlignment.CENTER,
								spacing=1,
							),
							ft.Row(
								[
									ft.FilledButton(
										style=ft.ButtonStyle(
											color=ft.colors.WHITE,
											shape=ft.buttons.CountinuosRectangleBorder(radius=0),
											overlay_color=ft.colors.TRANSPARENT,
										),
										content=ft.Container(
											ft.Text(
												value='Move',
												size=20,
												color=ft.colors.WHITE,
											),
											bgcolor='#009933',
											alignment=ft.alignment.center,
											border_radius=0,
											padding=20,
											margin=0,
											on_click=self.on_click_move,
										),
										expand=1,
									),
									ft.FilledButton(
										style=ft.ButtonStyle(
											color=ft.colors.WHITE,
											shape=ft.buttons.CountinuosRectangleBorder(radius=0),
											overlay_color=ft.colors.TRANSPARENT,
										),
										content=ft.Container(
											ft.Text(
												value='Update',
												size=20,
												color=ft.colors.WHITE,
											),
											bgcolor='#4d94ff',
											alignment=ft.alignment.center,
											border_radius=0,
											padding=20,
											margin=0,
											on_click=self.on_click_update,
										),
										expand=1,
									),
								],
								alignment = ft.MainAxisAlignment.CENTER,
							),
							ft.Row(
								[
									ft.FilledButton(
										style=ft.ButtonStyle(
											color=ft.colors.WHITE,
											shape=ft.buttons.CountinuosRectangleBorder(radius=0),
											overlay_color=ft.colors.TRANSPARENT,
										),
										content=ft.Container(
											ft.Text(
												value='Home',
												size=20,
												color=ft.colors.WHITE,
											),
											bgcolor='#009933',
											alignment=ft.alignment.center,
											border_radius=0,
											padding=20,
											margin=0,
											on_click=self.home_upper_gantry_bottom_sheet.show_bs,
										),
										expand=1,
									),
									ft.FilledButton(
										style=ft.ButtonStyle(
											color=ft.colors.WHITE,
											shape=ft.buttons.CountinuosRectangleBorder(radius=0),
											overlay_color=ft.colors.TRANSPARENT,
										),
										content=ft.Container(
											ft.Text(
												value="Configure Relative Moves",
												size=20,
												color=ft.colors.WHITE,
											),
											bgcolor='#4d94ff',
											alignment=ft.alignment.center,
											border_radius=0,
											padding=20,
											margin=0,
											on_click=self.configure_relative_moves_bottom_sheet.show_bs,
										),
										expand=1,
									),
								],
								alignment = ft.MainAxisAlignment.CENTER,
							),
						],
					),
				),
			],
		)

	def on_click_move(self, e):
		if self.consumable != None and self.consumable != ' ':
			action_msg = f"Move to {self.consumable}"
			if self.tray != None and self.tray != ' ':
				action_msg = action_msg + f" Tray {self.tray}"
			if self.column != None and self.column != ' ':
				action_msg = action_msg + f" Column {self.column}"
			print(action_msg)

	def on_click_update(self, e):
		print('update')

	def on_change_dropdown(self, e):
		label = e.control.label
		value = e.control.value
		if label == 'Consumable':
			self.consumable = value
		elif label == 'Tray':
			self.tray = value
		elif label == 'Column':
			self.column = value

class OptimizeGestureContainer(ft.Container):
	"""
	Optimze Gesture Container for detecting touch gestures for relative moves.
	"""
	def __init__(self):
		self.gd = ft.GestureDetector(
			mouse_cursor=ft.MouseCursor.MOVE,
			drag_interval=50,
			on_horizontal_drag_end=self.on_horizontal_drag_end,
			on_vertical_drag_end=self.on_vertical_drag_end,
		)
		super().__init__(
			self.gd,
			bgcolor=ft.colors.WHITE,
			width=380,
			height=300,
			alignment=ft.alignment.center,
		)

	def on_vertical_drag_end(self, e: ft.DragEndEvent):
		# Obtain the amount to move relative
		print('vertical')
		if e.velocity_y > 0:
			dy = e.page.session.get('dy_ug')
			#e.page.session.get('upper_gantry').move_relative('forwards', dy, velocity='fast')
			print(f"upper_gantry.move_relative('forwards', {dy}, velocity='fast')")
		elif e.velocity_y < 0:
			dy = e.page.session.get('dy_ug')
			#e.page.session.get('upper_gantry').move_relative('backwards', dy, velocity='fast')
			print(f"upper_gantry.move_relative('backwards', {dy}, velocity='fast')")

	def on_horizontal_drag_end(self, e: ft.DragEndEvent):
		print('horizontal')
		if e.velocity_x > 0:
			dx = e.page.session.get('dx_ug')
			#e.page.session.get('upper_gantry').move_relative('right', dx, velocity='fast')
			print(f"upper_gantry.move_relative('right', {dx}, velocity='fast')")
		elif e.velocity_x < 0:
			dx = e.page.session.get('dx_ug')
			#e.page.session.get('upper_gantry').move_relative('left', dx, velocity='fast')
			print(f"upper_gantry.move_relative('left', {dx}, velocity='fast')")

