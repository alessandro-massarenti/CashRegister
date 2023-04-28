
def run_app():
    # open the catalog view
    from Views import CatalogView, CartView
    from Controllers import CatalogController, CartController
    from Services import ProductService, CartService
    from Repositories import LocalProductRepository
    from tkinter import Tk

    root = Tk()
    cart_service = CartService()
    product_service = ProductService(LocalProductRepository())

    catalog_controller = CatalogController(product_service, cart_service)
    catalog_view = CatalogView(root, catalog_controller)
    catalog_controller.set_view(catalog_view)

    cart_controller = CartController(cart_service)
    cart_view = CartView(root, cart_controller)
    cart_controller.set_view(cart_view)

    root.mainloop()


if __name__ == '__main__':
    run_app()
