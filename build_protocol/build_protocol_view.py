import flet as ft

import sys
sys.path.append("..")

from app_bar import AppBar

from build_protocol.tips_bottom_sheet import TipsBottomSheet
from build_protocol.motion_bottom_sheet import MotionBottomSheet
#from build_protocol.pipette_bottom_sheet import PipetteBottomSheet
from build_protocol.other_bottom_sheet import OtherBottomSheet
#from build_protocol.time_bottom_sheet import TimeBottomSheet

BUILD_PROTOCOL_VIEW_ROUTE = "/build_protocol"

class BuildProtocolView(ft.View):
	"""
	Build Protocol View of the CDP 2.0 Mobile App
	"""
	route = BUILD_PROTOCOL_VIEW_ROUTE
	def __init__(self):
		super().__init__(
			self.route,
			[
				AppBar(title=ft.Text("CDP 2.0 - Build Protocol")),
				BuildProtocolListView(),
			],
		)

class BuildProtocolListView(ft.ListView):
	"""
	Build Protocol ListView containing all the FilledButtons for the 
	ThermocycleView
	"""
	def __init__(self):
		super().__init__(
			expand=1,
			spacing=10,
			padding=10,
			controls=[
				BuildProtocolFilledButton(title='Tips'),
				BuildProtocolFilledButton(title='Motion'),
				BuildProtocolFilledButton(title='Pipettor'),
				BuildProtocolFilledButton(title='Other'),
				BuildProtocolFilledButton(title='Time'),
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


class BuildProtocolFilledButton(ft.FilledButton):
	"""
	Build Protocol FilledButton for the Build Protocol View of the
	CDP 2.0 Mobile App
	"""
	def __init__(self, title: str, color:str='#009933') -> None:	
		self.title = title
		self.color = color
		if self.title.lower().replace(' ', '_') == 'tips':
			self.bottom_sheet = TipsBottomSheet()
		elif self.title.lower().replace(' ', '_') == 'motion':
			self.bottom_sheet = MotionBottomSheet()
		elif self.title.lower().replace(' ', '_') == 'pipette':
			self.bottom_sheet = TipsBottomSheet()
			a = 1
		elif self.title.lower().replace(' ', '_') == 'other':
			self.bottom_sheet = OtherBottomSheet()
		elif self.title.lower().replace(' ', '_') == 'time':
			self.bottom_sheet = TipsBottomSheet()
			a = 1
		else:
			self.bottom_sheet = TipsBottomSheet()
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
