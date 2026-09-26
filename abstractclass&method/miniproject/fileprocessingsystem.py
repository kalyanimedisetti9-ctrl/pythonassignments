from abc import ABC, abstractmethod

class FileHandler(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def process(self):
        pass

class PDFHandler(FileHandler):
    def process(self):
        print("Processing PDF file:", self.filename)

class CSVHandler(FileHandler):
    def process(self):
        print("Processing CSV file:", self.filename)

class ExcelHandler(FileHandler):
    def process(self):
        print("Processing Excel file:", self.filename)

class JSONHandler(FileHandler):
    def process(self):
        print("Processing JSON file:", self.filename)

files = [
    PDFHandler("report.pdf"),
    CSVHandler("data.csv"),
    ExcelHandler("marks.xlsx"),
    JSONHandler("users.json")
]

for file in files:
    file.process()