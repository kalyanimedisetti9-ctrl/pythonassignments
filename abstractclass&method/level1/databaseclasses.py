from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL Database")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL Database")

m = MySQLDatabase()
p = PostgreSQLDatabase()

m.connect()
p.connect()