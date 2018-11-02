import sqlite3

CURRENT_DBD_VERSION = '3.1'


class RAMToDBDConverter:

    fileName = None
    connection = None
    cursor = None

    def __init__(self, fileName):
        self.fileName = fileName
        self.connection = sqlite3.connect(self.fileName)

    # TODO:
    def init(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute("pragma foreign_keys=on;")

        self.connection.commit()
        self.cursor.close()

    # TODO:
    def insertSchemas(self):
        cursor = self.connection.cursor()
        cursor.executemany(
            """insert into """
        )
        cursor.close()
