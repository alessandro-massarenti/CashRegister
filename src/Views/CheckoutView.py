from Views.View import View
import tkinter as tk


class CheckoutView(View):

    def __init__(self,parent,checkout_controller):
        super().__init__(parent,checkout_controller)
        self.__checkout_controller = checkout_controller

        self.__view_title = tk.Label(self._frame, text="Checkout")
        self.__view_title.pack()

        # Add Payment button
        self.__add_payment_button = tk.Button(self._frame, text="Add Payment", command=self.__checkout_controller.pay)
        self.__add_payment_button.pack()

        # Store Transaction button
        self.__store_transaction_button = tk.Button(self._frame, text="Store Payment", command=self.__checkout_controller.store_transaction)
        self.__store_transaction_button.pack()

    def disable(self):
        self.__add_payment_button.config(state=tk.DISABLED)
        self.__store_transaction_button.config(state=tk.DISABLED)

    def enable(self):
        self.__add_payment_button.config(state=tk.NORMAL)
        self.__store_transaction_button.config(state=tk.NORMAL)
