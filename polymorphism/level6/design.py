from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def close(self):
        pass


class MySQL(Database):
    def connect(self):
        print("MySQL connected")

    def insert(self):
        print("Data inserted into MySQL")

    def close(self):
        print("MySQL connection closed")


class MongoDB(Database):
    def connect(self):
        print("MongoDB connected")

    def insert(self):
        print("Data inserted into MongoDB")

    def close(self):
        print("MongoDB connection closed")


databases = [MySQL(), MongoDB()]

for database in databases:
    database.connect()
    database.insert()
    database.close()