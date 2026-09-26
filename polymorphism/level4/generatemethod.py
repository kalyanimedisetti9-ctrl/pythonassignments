class PDFReport:
    def generate(self):
        print("PDF report generated")

class ExcelReport:
    def generate(self):
        print("Excel report generated")

class WordReport:
    def generate(self):
        print("Word report generated")


def generate_report(report):
    report.generate()


generate_report(PDFReport())
generate_report(ExcelReport())
generate_report(WordReport())