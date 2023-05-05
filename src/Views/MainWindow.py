import tkinter as tk

class MainWindow:

    def __init__(self,catalog_view,cart_view, checkout_view):
        self._catalog_view = catalog_view
        self._cart_view = cart_view
        self._checkout_view = checkout_view

    def assemble(self):
        self._catalog_view.frame().pack(side=tk.RIGHT)
        self._checkout_view.frame().pack(side=tk.BOTTOM)
        self._cart_view.frame().pack(side=tk.LEFT)

