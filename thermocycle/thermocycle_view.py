import flet as ft

import sys
sys.path.append("..")

from app_bar import AppBar
from thermocycle.cycles_bottom_sheet import CyclesBottomSheet
from thermocycle.temperatures_bottom_sheet import TemperaturesBottomSheet
from thermocycle.times_bottom_sheet import TimesBottomSheet
from thermocycle.trays_bottom_sheet import TraysBottomSheet
from thermocycle.clamps_bottom_sheet import ClampsBottomSheet

THERMOCYCLE_VIEW_ROUTE = "/thermocycle"

class ThermocycleView(ft.View):
	"""
	Thermocycler View of the CDP 2.0 Mobile App
	"""
	route = THERMOCYCLE_VIEW_ROUTE
	def __init__(self):
		super().__init__(
			self.route,
			[
				AppBar(title=ft.Text("CDP 2.0 - Thermocycle")),
				ThermocycleListView(),
			],
		)

class ThermocycleListView(ft.ListView):
	"""
	Thermocycle ListView containing all the FilledButtons for the 
	ThermocycleView
	"""
	def __init__(self):
		super().__init__(
			expand=1,
			spacing=10,
			padding=10,
			controls=[
				ThermocyclerDropdown(),
				ThermocycleFilledButton(title='Cycles'),
				ThermocycleFilledButton(title='Temperatures'),
				ThermocycleFilledButton(title='Times'),
				ThermocycleFilledButton(title='Trays'),
				ThermocycleFilledButton(title='Clamps'),
				ft.FilledButton(
					style=ft.ButtonStyle(
						color=ft.colors.WHITE,
						shape=ft.buttons.CountinuosRectangleBorder(radius=0),
						overlay_color=ft.colors.TRANSPARENT,
					),
					content=ft.Container(
						ft.Text(
							value='Start',
							size=30,
							color=ft.colors.WHITE,
						),
						bgcolor='#4d94ff',
						alignment=ft.alignment.center,
						border_radius=0,
						padding=20,
						margin=0,
						on_click=self.on_click,
					),
				),
			],
		)

	def on_click(self, e):
		hf = ft.HapticFeedback()
		e.page.overlay.clear()
		e.page.overlay.append(hf)
		e.page.update()
		hf.vibrate()

class ThermocyclerDropdown(ft.Dropdown):
	"""
	Thermocycler Dropdown for the Thermocycle View of the CDP 2.0 Mobile App
	"""
	def __init__(self):
		super().__init__(
			label='Thermocyclers',
			hint_text="Choose the Thermocycler to Configure",
			options=[
				ft.dropdown.Option('A'),
				ft.dropdown.Option('B'),
				ft.dropdown.Option('C'),
				ft.dropdown.Option('D'),
			],
			autofocus=True,
		)

class ThermocycleFilledButton(ft.FilledButton):
	def __init__(self, title: str, color:str='#009933') -> None:	
		self.title = title
		self.color = color
		if self.title.lower().replace(' ', '_') == 'cycles':
			self.bottom_sheet = CyclesBottomSheet('A')
		elif self.title.lower().replace(' ', '_') == 'temperatures':
			self.bottom_sheet = TemperaturesBottomSheet('A')
		elif self.title.lower().replace(' ', '_') == 'times':
			self.bottom_sheet = TimesBottomSheet('A')
		elif self.title.lower().replace(' ', '_') == 'trays':
			self.bottom_sheet = TraysBottomSheet()
		elif self.title.lower().replace(' ', '_') == 'clamps':
			self.bottom_sheet = ClampsBottomSheet()
		else:
			self.bottom_sheet = CyclesBottomSheet('A')
		super().__init__(
			style=ft.ButtonStyle(
				color=ft.colors.WHITE,
				shape=ft.buttons.CountinuosRectangleBorder(radius=0),
				overlay_color=ft.colors.TRANSPARENT,
			),
			content=ft.Container(
				ft.Text(
					value=self.title.title(),
					size=30,
					color=ft.colors.WHITE,
				),
				bgcolor=self.color,
				alignment=ft.alignment.center,
				border_radius=0,
				padding=20,
				margin=0,
				on_click=self.bottom_sheet.show_bs,
			),
		)

	def on_click(self, e):
		a = 1
		#e.page.overlay.append(self.bottom_sheet)
		#self.bottom_sheet.open = True
		#e.page.update()
