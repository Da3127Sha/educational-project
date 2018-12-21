import pyodbc


USER = r'mssqluser'
SERVER = r'sqlexpress'
PASSWORD = '123'
DATABASE = 'northwind'


class MSSQLMetadataGetter:
    connection = None

    def __init__(self):
        print("start")
        try:
            self.connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};" +
                                             "Server=noutdexp\sqlexpress;" +
                                             "Database=northwind;" +
                                             "uid=mssqluser;" +
                                             "pwd=123;")
            print("good!")
            self.connection.close()
        except (Exception) as error:
            print("Error while connecting to MS SQL", error)