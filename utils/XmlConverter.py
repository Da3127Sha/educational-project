from xml.dom import minidom
from classes.DBDSchema import DBDSchema
from classes.Domain import Domain
from classes.Table import Table
from classes.Field import Field
from classes.Constraint import Constraint
from classes.Index import Index

doc = minidom.parse("../resources/Test2.xml")

xmlSchema = doc.getElementsByTagName("dbd_schema")[0]
schema = DBDSchema(xmlSchema.getAttribute("fulltext_engine"))
schema.setVersion(xmlSchema.getAttribute("version"))
schema.setName(xmlSchema.getAttribute("name"))
schema.setDescription("description")

xmlDomains = doc.getElementsByTagName("domain")
for xmlDomain in xmlDomains:
    domain = Domain(xmlDomain.getAttribute("name"),
                    xmlDomain.getAttribute("type"))
    domain.setAlign(xmlDomain.getAttribute("align"))
    domain.setWidth(xmlDomain.getAttribute("width"))
    domain.setCharLength(xmlDomain.getAttribute("char_length"))
    domain.setDescription(xmlDomain.getAttribute("description"))
    domain.setProps(xmlDomain.getAttribute("props"))
    domain.setPrecision(xmlDomain.getAttribute("precision"))
    domain.setLength(xmlDomain.getAttribute("length"))
    domain.setScale(xmlDomain.getAttribute("scale"))
    schema.setDomain(domain.getName(), domain)
    #if (domain.getPrecision() != ""):
    #    print(domain.getPrecision())

xmlTables = doc.getElementsByTagName("table")
for xmlTable in xmlTables:
    table = Table(xmlTable.getAttribute("name"))
    table.setDescription(xmlTable.getAttribute("description"))
    table.setProps(xmlTable.getAttribute("props"))
    table.setHtTableFlags(xmlTable.getAttribute("ht_table_flags"))
    table.setAccessLevel(xmlTable.getAttribute("access_level"))

    xmlFields = xmlTable.getElementsByTagName("field")
    for xmlField in xmlFields:
        field = Field(xmlField.getAttribute("name"),
                      xmlField.getAttribute("rname"))
        field.setDomain(schema.getDomain(xmlField.getAttribute("domain")))
        field.setProps(xmlField.getAttribute("props"))
        table.setField(field.getName(), field)

    xmlConstraints = xmlTable.getElementsByTagName("constraint")
    for xmlConstraint in xmlConstraints:
        constraint = Constraint(xmlConstraint.getAttribute("kind"))
        constraint.setProps(xmlConstraint.getAttribute("props"))
        constraint.setReference(xmlConstraint.getAttribute("reference"))
        constraint.setItems(xmlConstraint.getAttribute("items"))
        table.setConstraint(constraint)

    xmlIndices = xmlTable.getElementsByTagName("index")
    for xmlIndex in xmlIndices:
        index = Index(xmlIndex.getAttribute("field"))
        index.setProps(xmlIndex.getAttribute("props"))

    schema.setTable(table.getName(), table)

print(xmlSchema.getAttribute("fulltext_engine"))
print(schema.getTable("ADDRESS").getField("Region").getRname())

