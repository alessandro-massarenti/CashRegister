# Import tkinter
import tkinter as tk
from Controllers import CatalogController


class CatalogView:

    def __init__(self, parent, catalog_controller: CatalogController):
        self.catalog_controller = catalog_controller
        self.__frame = tk.Frame(parent)

        # Create a label
        self.__view_title = tk.Label(self.__frame, text="Catalog")

        self.__buttons = []

        # Pack the label and button
        self.__view_title.pack()

        # Pack the frame
        self.__frame.pack()

    def add_product_button(self, product_name: str, callback):
        button = tk.Button(self.__frame, text=product_name, command=callback)
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
