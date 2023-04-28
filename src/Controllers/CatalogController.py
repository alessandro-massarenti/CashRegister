import logging

from Models import Product
from Views import CatalogView
from Services import ProductService, CartService
from interfaces import Observer, ObservableSubject


class CatalogController(Observer):

    def __init__(self, product_service: ProductService, cart_service:CartService):
        self.__product_service = product_service
        self.__cart_service = cart_service
        self.__catalog_view: CatalogView

    def __del__(self):
        self.__product_service.unregister(self)

    def set_view(self, catalog_view: CatalogView):
        self.__catalog_view = catalog_view
        self.__product_service.register(self)
        self.update_from_service()

    def update(self, observable: ObservableSubject) -> None:
        self.update_from_service()

    def update_from_service(self):
        products = self.__product_service.get_all()
        buttons = self.__catalog_view.get_product_names()

        # update only the products that are not in the view
        for product in products:
            if product.name not in self.__catalog_view.get_product_names():
                self.__catalog_view.add_product_button(product.name, lambda p=product: self.add_item(p))

    def add_item(self, product):
        # Add an item to the catalog
        self.__cart_service.add(product)
