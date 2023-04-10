import uuid
from Repositories import ProductRepository
from Models import Product


class LocalProductRepository(ProductRepository):

    def __init__(self):
        self.__products: dict[str, Product] = {}

        p = Product("Product 1", 10.00)
        self.__products[p.name] = p
        p = Product("Product 2", 20.00)
        self.__products[p.name] = p
        p = Product("Product 3", 30.00)
        self.__products[p.name] = p



    def get(self, name: str) -> Product:
        return self.__products[name]

    def get_all(self):
        return self.__products.values()

    def add(self, product):
        self.__products[product.name] = product

    def delete(self, name: str):
        del self.__products[name]

    def update(self, product):
        self.__products[product.name] = product
