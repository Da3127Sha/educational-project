from utils.XmlParser import *
from utils.DBInitializer import *

schemaTasks = createObjectFromXml("./resources/tasks.xml")
schemaPrjadm = createObjectFromXml("./resources/prjadm.xml")
print(schemaTasks.getTable("ADDRESS").getField("Region").getRname())
print(schemaPrjadm.getTable("CASCDEL").getField("KodKaskad").getRname())
print(schemaTasks.getFulltextEngine())
print(schemaPrjadm.getFulltextEngine())
inital = DBInitializer("database.db")
inital.initDB()