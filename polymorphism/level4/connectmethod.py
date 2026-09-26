class MySQL:
    def connect(self):
        print("Connected to MySQL database")

class MongoDB:
    def connect(self):
        print("Connected to MongoDB database")

class Oracle:
    def connect(self):
        print("Connected to Oracle database")


def connect_database(database):
    database.connect()


connect_database(MySQL())
connect_database(MongoDB())
connect_database(Oracle())