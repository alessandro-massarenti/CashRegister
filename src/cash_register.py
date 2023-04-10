def run_app():
    # open the catalog view
    from Views import CatalogView
    from Controllers import CatalogController
    from Services import ProductService
    from Repositories import LocalProductRepository
    from tkinter import Tk

    root = Tk()

    catalog_controller = CatalogController(ProductService(LocalProductRepository()))
    catalog_view = CatalogView(root, catalog_controller)
    catalog_controller.set_view(catalog_view)

    root.mainloop()


if __name__ == '__main__':
    run_app()
