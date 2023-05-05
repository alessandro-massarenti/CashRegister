import tkinter as tk

class MainWindow:

    def __init__(self,catalog_view,cart_view):
        self.catalog_view = catalog_view
        self.cart_view = cart_view

    def assemble(self):
        self.catalog_view.frame().pack(side=tk.RIGHT)
        self.cart_view.frame().pack(side=tk.LEFT)
