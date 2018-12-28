from utils.MSSQLMetadataGetter import *
from utils.RAMtoXDBConverter import RAMToXDBConverter

SCHEMA = "dbo"

metadata_getter = MSSQLMetadataGetter()
schema = metadata_getter.get_metadata(SCHEMA)
if (schema is not None):
    for d in schema.get_domains().values():
        if (d.unnamed):
            print("Неименованный домен: " + d.name)
        else:
            print("Домен: " + d.name)
    for t in schema.get_tables().values():
        print("-------Таблица: " + t.name)
        for f in t.get_fields().values():
            print("Поле: " + f.name)
        for co in t.get_constraints():
            if (co.kind == "PRIMARY"):
                print("Первичный ключ на поле: " + co.items)
            else:
                print("Внешний ключ на поле: " + co.items)
                print("     Ссылается на таблицу: " + co.reference)
        for i in t.get_indices():
            print("Индекс на поле : " + i.field_name)

converter = RAMToXDBConverter(schema)
schema_xml = converter.create_schema(schema)
print(schema_xml)