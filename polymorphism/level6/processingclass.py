from abc import ABC, abstractmethod

class FileProcessor(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class TextFile(FileProcessor):
    def read(self):
        print("Reading text file")

    def write(self):
        print("Writing text file")


class PDFFile(FileProcessor):
    def read(self):
        print("Reading PDF file")

    def write(self):
        print("Writing PDF file")


files = [TextFile(), PDFFile()]

for file in files:
    file.read()
    file.write()