class InvalidFileFormatError(Exception):
    pass

class InvalidDataError(Exception):
    pass


class FileManager:
    def read_file(self, filename):
        try:
            if not filename.endswith(".txt"):
                raise InvalidFileFormatError(
                    "Only .txt files are allowed"
                )

            with open(filename, "r") as file:
                data = file.read()

                if data == "":
                    raise InvalidDataError("File contains no data")

                print("File content:")
                print(data)

        except FileNotFoundError:
            print("Error: File not found")

        except PermissionError:
            print("Error: Permission denied")

        except InvalidFileFormatError as e:
            print("Error:", e)

        except InvalidDataError as e:
            print("Error:", e)


manager = FileManager()

manager.read_file("sample.txt")
manager.read_file("sample.pdf")