# Import tkinter
import tkinter as tk
from Controllers import CatalogController
from Views.View import View


class CatalogView(View):

    def __init__(self, parent, catalog_controller: CatalogController):
        super().__init__(parent, catalog_controller)
        self.catalog_controller = catalog_controller

        # Create a label
        self.__view_title = tk.Label(self._frame, text="Catalog")

        self.__buttons = []

        # Pack the label and button
        self.__view_title.pack()

    def add_product_button(self, product_name: str, callback):
        button = tk.Button(self._frame, text=product_name, command=callback)
        button.pack()
        self.__buttons.append(button)

    def get_product_names(self):
        return [button['text'] for button in self.__buttons]


if __name__ == '__main__':
    from Controllers import CatalogController

    # Create the root window
    root = tk.Tk()

    # Create the catalog view
    catalog_view = CatalogView(root, CatalogController())

    # Run the mainloop
    root.mainloop()
