import tkinter as tk

from Context import Context
from Controllers import CatalogController, CartController, CheckoutController
from Controllers.MainWindowController import MainWindowController
from Views import View, CatalogView, CartView
from Views.CheckoutView import CheckoutView


class MainWindow(View):

    def __init__(self, parent, controller: MainWindowController):
        super().__init__(parent, controller)

    def assemble(self):

        context = Context()


        catalog_controller = CatalogController(context.product_service, context.cart_service)
        cart_controller = CartController(context.cart_service)
        checkout_controller = CheckoutController(context.cart_service)


        catalog_view = CatalogView(self.frame(), catalog_controller)
        cart_view = CartView(self.frame(), cart_controller)
        checkout_view = CheckoutView(self.frame(), checkout_controller)


        catalog_controller.set_view(catalog_view)
        cart_controller.set_view(cart_view)
        checkout_controller.set_view(checkout_view)

        catalog_view.frame().pack(side=tk.RIGHT)
        checkout_view.frame().pack(side=tk.BOTTOM)
        cart_view.frame().pack(side=tk.LEFT)

