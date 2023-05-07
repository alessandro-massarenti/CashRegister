from Controllers.CheckoutController import CheckoutController
from Controllers.MainWindowController import MainWindowController
from Views.CheckoutView import CheckoutView
from Views.MainWindow import MainWindow


def run_app():
    # open the catalog view
    from Services import ProductService, CartService
    from Repositories import LocalProductRepository
    from tkinter import Tk

    root = Tk()

    main_window_controller = MainWindowController()
    main_window = MainWindow(root, main_window_controller)

    main_window_controller.set_view(main_window)

    main_window.assemble()

    main_window.show()
    root.mainloop()


if __name__ == '__main__':
    run_app()
