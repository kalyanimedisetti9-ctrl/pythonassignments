class PDF:
    def read(self):
        print("Reading PDF file")

    def write(self):
        print("Writing PDF file")

class Excel:
    def read(self):
        print("Reading Excel file")

    def write(self):
        print("Writing Excel file")

class Word:
    def read(self):
        print("Reading Word file")

    def write(self):
        print("Writing Word file")

class CSV:
    def read(self):
        print("Reading CSV file")

    def write(self):
        print("Writing CSV file")


def process_file(file):
    file.read()
    file.write()


files = [PDF(), Excel(), Word(), CSV()]

for file in files:
    process_file(file)