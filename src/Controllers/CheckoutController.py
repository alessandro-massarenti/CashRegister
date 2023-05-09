from Context import Context
from Controllers.Controller import Controller
from Views.CheckoutView import CheckoutView
from interfaces import ObservableSubject


class CheckoutController(Controller):

    def __init__(self, cart_service):
        super().__init__()
        self.__cart_service = cart_service
        self.__checkout_view: CheckoutView

    def set_view(self, checkout_view: CheckoutView):
        self.__checkout_view = checkout_view
        self.__cart_service.register(self)
        self.update(self.__cart_service)

    def update(self, observable: ObservableSubject) -> None:
        if self.__cart_service.is_empty:
            self.__checkout_view.disable()
        else:
            self.__checkout_view.enable()

    def pay(self):

        printer_service = Context().printer_service
        printer_service.print("Mammamiaa")
        self.__cart_service.clear()

        print("paying")

    def store_transaction(self):
        print("storing transaction")
