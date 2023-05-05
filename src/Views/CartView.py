import tkinter as tk
import tkinter.ttk as ttk

from Controllers import CartController
from Views.View import View


class CartView(View):
    def __init__(self, parent, cart_controller: CartController):
        super().__init__(parent, cart_controller)
        self.__cart_controller = cart_controller

        # Create a label
        self.__view_title = tk.Label(self._frame, text="Cart")

        self.__tree = ttk.Treeview(self._frame, columns=('name', 'quantity', 'price', 'total'), show='headings')
        self.__tree.heading('name', text='Name')
        self.__tree.heading('quantity', text='Quantity')
        self.__tree.heading('price', text='Price')
        self.__tree.heading('total', text='Total')



        self.__view_title.pack()
        self.__tree.pack()

        self._frame.pack()

    def clear(self):
        self.__tree.delete(*self.__tree.get_children())

    def add_item(self, item):
        self.__tree.insert('', 'end', values=(item.name, item.quantity, item.price, item.total))