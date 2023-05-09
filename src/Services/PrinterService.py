from interfaces.Printable import Printable


class PrinterService:

    def __init__(self):
        from escpos.printer import Usb
        #Setup the TM-T20 printer
        self._printer = Usb(0x04b8, 0x0e03, 0)
        self.cutting = True

    def cutting(self, cutting:bool = True):
        self.cutting = cutting

    def print(self,printable):
        self._printer.text(printable)
        if self.cutting:
            self._printer.cut()

if __name__ == '__main__':
    PrinterService()
