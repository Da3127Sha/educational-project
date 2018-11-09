from utils.XmlParser import *
from utils.DBInitializer import *

schema_tasks = create_object_from_xml("./resources/tasks.xml")
schema_prjadm = create_object_from_xml("./resources/prjadm.xml")
print(schema_tasks.get_table("ADDRESS").get_field("Region").get_rname())
print(schema_prjadm.get_table("CASCDEL").get_field("KodKaskad").get_rname())
print(schema_tasks.get_fulltext_engine())
print(schema_prjadm.get_fulltext_engine())
inital = DBInitializer("database.db")
inital.init_database()