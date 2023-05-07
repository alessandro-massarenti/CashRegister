from Repositories import LocalProductRepository
from Services import CartService, ProductService
from interfaces.SingletonMeta import SingletonMeta


class Context(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._cart_service = CartService()
        self._product_service = ProductService(LocalProductRepository())



    @property
    def cart_service(self):
        return self._cart_service

    @property
    def product_service(self):
        return self._product_service

