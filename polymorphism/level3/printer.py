class Printer:
    def print(self):
        print("Printing a document")

class PDFPrinter:
    def print(self):
        print("Printing a PDF document")


def start_printing(device):
    device.print()


start_printing(Printer())
start_printing(PDFPrinter())