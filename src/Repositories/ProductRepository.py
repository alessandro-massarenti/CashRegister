from abc import ABC, abstractmethod

from Models import Product


class ProductRepository(ABC):

    @abstractmethod
    def get(self, name: str) -> Product:
        pass

    @abstractmethod
    def get_all(self) -> list[Product]:
        pass

    @abstractmethod
    def add(self, product):
        pass

    @abstractmethod
    def delete(self, name: str):
        pass

    @abstractmethod
    def update(self, product):
        pass
