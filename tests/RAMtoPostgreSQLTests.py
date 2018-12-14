from utils.XmlParser import *
from utils.DDLPostgreSQLGenerator import *

DATABASE_NAME = "database.db"
XML_FILE_NAME_1 = "../resources/tasks.xml"
XML_FILE_NAME_2 = "../resources/prjadm.xml"

schemas = create_list_of_objects_from_xml([XML_FILE_NAME_1, XML_FILE_NAME_2])

# This is for test
print(schemas[0].get_table("ADDRESS").get_field("Region").get_rname())
print(schemas[1].get_table("CASCDEL").get_field("KodKaskad").get_rname())
print(schemas[0].get_fulltext_engine())
print(schemas[1].get_fulltext_engine())

ddl_generator_1 = DDLPostgreSQLGenerator()
ddl_generator_1.generate_DDL(schemas[0])
ddl_generator_2 = DDLPostgreSQLGenerator()
ddl_generator_2.generate_DDL(schemas[1])



