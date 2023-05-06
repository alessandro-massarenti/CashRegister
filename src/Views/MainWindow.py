import tkinter as tk

from Controllers import CatalogController, CartController, CheckoutController
from Controllers.MainWindowController import MainWindowController
from Views import View, CatalogView, CartView
from Views.CheckoutView import CheckoutView


class MainWindow(View):

    def __init__(self, parent, controller: MainWindowController):
        super().__init__(parent, controller)



    def assemble(self):

        #TODO: Create the context injection for the services via a singleton pattern class as a dependency injection container

        catalog_controller = CatalogController(product_service, cart_service)
        catalog_view = CatalogView(self.frame(), catalog_controller)

        catalog_controller.set_view(catalog_view)

        cart_controller = CartController(cart_service)
        cart_view = CartView(self.frame(), cart_controller)

        cart_controller.set_view(cart_view)

        checkout_controller = CheckoutController(cart_service)
        checkout_view = CheckoutView(self.frame(), checkout_controller)

        checkout_controller.set_view(checkout_view)

        self._catalog_view.frame().pack(side=tk.RIGHT)
        self._checkout_view.frame().pack(side=tk.BOTTOM)
        self._cart_view.frame().pack(side=tk.LEFT)

