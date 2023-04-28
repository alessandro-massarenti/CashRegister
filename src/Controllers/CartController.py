from Models import Product
from interfaces import ObservableSubject, Observer
from Views import CartView


class CartController(Observer):

    def __init__(self, cart_service):
        self.__cart_service = cart_service
        self.__cart_view: CartView

    def __del__(self):
        self.__cart_service.unregister(self)

    def set_view(self, cart_view: CartView):
        self.__cart_view = cart_view
        self.__cart_service.register(self)

        # TODO: remove this
        self.__cart_service.add(Product("Product 1", 10.00))
        self.__cart_service.add(Product("Product 1", 10.00))
        self.__cart_service.add(Product("Product 2", 20.00))
        self.__cart_service.add(Product("Product 3", 30.00))

    def update(self, observable: ObservableSubject) -> None:
        self.update_view()

    def update_view(self):
        # clear the view
        self.__cart_view.clear()
        # add the items in the cart to the view
        for item in self.__cart_service.get_all():
            self.__cart_view.add_item(item)
