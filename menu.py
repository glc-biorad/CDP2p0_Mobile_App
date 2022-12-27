import flet as ft

class Menu(ft.PopupMenuButton):
	"""
	Menu for the CDP 2.0 Mobile App
	"""
	def __init__(self) -> None:
		# View Routes
		self.thermocycle_view_route = "/thermocycle"
		self.optimize_view_route = "/optimize"
		self.build_protocol_view_route = "/build_protocol"

		# Items in the Menu
		items = [
			ft.PopupMenuItem(icon=ft.icons.CAMERA_ALT, text='Image', on_click=self.on_click_menu_image),
			ft.PopupMenuItem(icon=ft.icons.WHATSHOT, text='Thermocycle', on_click=self.on_click_menu_thermocycle),
			ft.PopupMenuItem(icon=ft.icons.VIEW_TIMELINE, text="Build Protocol", on_click=self.on_click_menu_build_protocol),
			ft.PopupMenuItem(icon=ft.icons.TUNE, text='Optimize', on_click=self.on_click_menu_optimize),
			ft.PopupMenuItem(icon=ft.icons.HOME_REPAIR_SERVICE, text='Service', on_click=self.on_click_menu_service),
			ft.PopupMenuItem(icon=ft.icons.WYSIWYG, text='Configure', on_click=self.on_click_menu_configure),
		]
		super().__init__(items=items)

	def on_click_menu_image(self, e):
		print('here')

	def on_click_menu_thermocycle(self, e):
		e.page.go(self.thermocycle_view_route)

	def on_click_menu_build_protocol(self, e):
		e.page.go(self.build_protocol_view_route)

	def on_click_menu_optimize(self, e):
		e.page.go(self.optimize_view_route)

	def on_click_menu_service(self, e):
		print('here')

	def on_click_menu_configure(self, e):
		print('here')
