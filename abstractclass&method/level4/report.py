from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("PDF report generated")

class ExcelReport(Report):
    def generate(self):
        print("Excel report generated")

class WordReport(Report):
    def generate(self):
        print("Word report generated")

reports = [PDFReport(), ExcelReport(), WordReport()]

for report in reports:
    report.generate()