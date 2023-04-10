from Models import Product
from Models import CartLine


class Tabulation:

    def __init__(self, client_name):
        self.__table_data: list[CartLine] = []

    def get(self, product_name: str) -> list[CartLine]:
        return [tab_line for tab_line in self.__table_data if tab_line.name == product_name]

    def add(self, product: Product):
        tab_line = CartLine(product.name, 1, product.price)
        # Se la tabline esiste già aggiungi più uno alla tabline
        # altrimenti aggiungi la tabline alla table data
        if tab_line in self.__table_data:
            self.__table_data[self.__table_data.index(tab_line)].add_quantity()
        else:
            self.__table_data.append(tab_line)

    def remove(self, product: Product):

        # se la tabline esiste già rimuovi una unità
        # altrimenti rimuovi la tabline dalla table data
        tab_line = CartLine(product.name, 1, product.price)
        if tab_line in self.__table_data:
            self.__table_data[self.__table_data.index(tab_line)].add_quantity(-1)
            if self.__table_data[self.__table_data.index(tab_line)].quantity == 0:
                self.__table_data.remove(tab_line)
        else:
            raise Exception("Nulla da rimuovere")

    def get_total(self) -> float:
        return sum([tab_line.total for tab_line in self.__table_data])

    def get_total_quantity(self) -> int:
        return sum([tab_line.quantity for tab_line in self.__table_data])

    def get_total_products(self) -> int:
        return len(self.__table_data)
