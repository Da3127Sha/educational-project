from utils.XmlParser import *

schemaTasks = createObjectFromXml("./resources/tasks.xml")
schemaPrjadm = createObjectFromXml("./resources/prjadm.xml")
print(schemaTasks.getTable("ADDRESS").getField("Region").getRname())
print(schemaPrjadm.getTable("CASCDEL").getField("KodKaskad").getRname())