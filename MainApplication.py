from utils.XmlParser import *
from utils.DBInitializer import *
from utils.RAMToDBDConverter import *
import os

DATABASE_NAME = "database.db"
XML_FILE_NAME_1 = "./resources/tasks.xml"
XML_FILE_NAME_2 = "./resources/prjadm.xml"

schemas = create_list_of_objects_from_xml([XML_FILE_NAME_1, XML_FILE_NAME_2])

# This is for test
print(schemas[0].get_table("ADDRESS").get_field("Region").get_rname())
print(schemas[1].get_table("CASCDEL").get_field("KodKaskad").get_rname())
print(schemas[0].get_fulltext_engine())
print(schemas[1].get_fulltext_engine())

create = not os.path.exists(DATABASE_NAME)
if create:
    initializer = DBInitializer(DATABASE_NAME)
    initializer.init_database()
    converter_to_database = RAMToDBDConverter(DATABASE_NAME)
    converter_to_database.RAM_to_DBD(schemas)

# This is for test
print("-------------")
connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()
cursor.execute("pragma foreign_keys=on;")
cursor.execute("""select * from dbd$domains """)
records = cursor.fetchall()
for i, record in enumerate(records):
    print(record)
cursor.close()



