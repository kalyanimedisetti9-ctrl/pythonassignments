class TextFile:
    def read(self):
        print("Reading text file")

class PDFFile:
    def read(self):
        print("Reading PDF file")

class WordFile:
    def read(self):
        print("Reading Word file")


def read_file(file):
    file.read()


read_file(TextFile())
read_file(PDFFile())
read_file(WordFile())