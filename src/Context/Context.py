from Repositories import LocalProductRepository
from Services import CartService, ProductService
from Services.PrinterService import PrinterService
from interfaces.SingletonMeta import SingletonMeta


class Context(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._cart_service = CartService()
        self._product_service = ProductService(LocalProductRepository())
        self._printer_service = PrinterService()



    @property
    def cart_service(self):
        return self._cart_service

    @property
    def product_service(self):
        return self._product_service

    @property
    def printer_service(self):
        return self._printer_service
