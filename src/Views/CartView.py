import tkinter as tk
import tkinter.ttk as ttk

from Controllers import CartController


class CartView:
    def __init__(self, parent, cart_controller: CartController):
        self.__cart_controller = cart_controller
        self.__frame = tk.Frame(parent)

        # Create a label
        self.__view_title = tk.Label(self.__frame, text="Cart")

        self.__tree = ttk.Treeview(self.__frame, columns=('name', 'quantity', 'price', 'total'), show='headings')
        self.__tree.heading('name', text='Name')
        self.__tree.heading('quantity', text='Quantity')
        self.__tree.heading('price', text='Price')
        self.__tree.heading('total', text='Total')



        self.__view_title.pack()
        self.__tree.pack()

        self.__frame.pack()

    def clear(self):
        self.__tree.delete(*self.__tree.get_children())

    def add_item(self, item):
        self.__tree.insert('', 'end', values=(item.name, item.quantity, item.price, item.total))