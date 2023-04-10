class CartLine:

    def __init__(self, product_name, quantity, price):
        self.__product_name: str = product_name
        self.__quantity: int = quantity
        self.__price: float = price

    @property
    def name(self):
        return self.__product_name

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def price(self) -> float:
        return self.__price

    @property
    def total(self) -> float:
        return self.quantity * self.price

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.price == other.price

    def add_quantity(self, quantity: int = 1):
        self.__quantity += quantity
