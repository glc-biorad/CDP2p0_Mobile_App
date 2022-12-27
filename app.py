#!/usr/bin/env python

import flet as ft

from app_bar import AppBar
from thermocycle.thermocycle_view import ThermocycleView
from optimize.optimize_view import OptimizeView
from build_protocol.build_protocol_view import BuildProtocolView

class App():
	"""
	CDP 2.0 Mobile Application
	"""

	def __init__(self, page: ft.Page):
		self.page = page
		self.page.title = "CDP 2.0 Mobile Application"
		self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

		# Views.
		self.thermocycle_view = ThermocycleView()
		self.optimize_view = OptimizeView()
		self.build_protocol_view = BuildProtocolView()

		# Navigation and Routing.
		self.page.on_route_change = self.route_change
		self.on_view_pop = self.view_pop
		self.page.go(self.page.route)

		# Allow scrolling.
		self.page.scroll = 'always'

		# Public Values: Upper Gantry Relative Moves.
		self.page.session.set('dx_ug', 500)
		self.page.session.set('dy_ug', 5000)
		self.page.session.set('dz_ug', 5000)
		
	def route_change(self, route):
		# Clear the current view list
		self.page.views.clear()
		# Set the root view
		self.page.views.append(
			ft.View(
				"/",
				[
					AppBar()
				],
			)
		)		
		if self.page.route == self.thermocycle_view.route:
			self.page.views.append(
				self.thermocycle_view,
			)
		elif self.page.route == self.optimize_view.route:
			self.page.views.append(
				self.optimize_view,
			)
		elif self.page.route == self.build_protocol_view.route:
			self.page.views.append(
				self.build_protocol_view,
			)
		# Update the page with the view
		self.page.update()
		

	def view_pop(self, view) -> None:
		self.page.views.pop()
		self.page.go(self.page.views[-1].route)

if __name__ == '__main__':
	ft.app(target=App, view=ft.WEB_BROWSER)
