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

    def update(self, observable: ObservableSubject) -> None:
        pass

    def pay(self):
        print("paying")

    def store_transaction(self):
        print("storing transaction")
