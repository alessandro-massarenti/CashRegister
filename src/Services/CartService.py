from Models import Product, CartLine
from interfaces import ObservableSubject


class CartService(ObservableSubject):

    def __init__(self):
        super().__init__()
        self._items: list[CartLine] = []

    def add(self, product: Product):
        # check if the product is already in the cart
        for item in self._items:
            if item.name == product.name:
                item.add_quantity()
                self._notify_observers()
                return
        # if the product is not in the cart, add it to the cart
        self._items.append(CartLine(product.name, 1, product.price))
        self._notify_observers()

    def get_all(self) -> list[CartLine]:
        return self._items

    def remove(self, product_name: str):
        # riduce la quantità di un prodotto nel carrello
        for item in self._items:
            if item.name == product_name:
                item.add_quantity(-1)
                if item.quantity == 0:
                    self._items.remove(item)
                self._notify_observers()
                return


