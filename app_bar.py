import flet as ft

from menu import Menu

class AppBar(ft.AppBar):
	"""
	App Bar for Navigating the CDP 2.0 Mobile App
	"""
	def __init__(self, title: ft.Text = ft.Text("CDP 2.0 - Home")) -> None:
		self.title = title
		super().__init__(
			leading=ft.Icon(ft.icons.ABC), 
			leading_width=40, 
			title=self.title, 
			center_title=False, 
			bgcolor=ft.colors.SURFACE_VARIANT, 
			actions=[Menu()]
		)
