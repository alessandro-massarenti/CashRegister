from Repositories import ProductRepository
from Models import Product
from interfaces import ObservableSubject, Observer


class ProductService(ObservableSubject):

    def __init__(self, product_repository: ProductRepository):
        super().__init__()
        self.product_repository = product_repository

    def get_all(self):
        return self.product_repository.get_all()

    def get(self,name) -> Product:
        return self.product_repository.get(name)

    def add(self, product: Product):
        #check if product already exists
        if product in self.product_repository.get_all():
            raise Exception(f'Product {product.name} already exists')

        self.product_repository.add(product)
        self._notify_observers()

    def delete(self, id):
        self.product_repository.delete(id)
        self._notify_observers()

    def update(self, product: Product):
        self.product_repository.update(product)
        self._notify_observers()
