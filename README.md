# educational-project
Educational project for collective application development

# Project structure
+ classes
    + `Constraint.py` - constraint class
    + `DBDSchema.py` - database schema class
    + `Domain.py` - domain class
    + `Field.py` - field class
    + `Index.py` - index class
    + `Table.py` - table class
+ resources
    + `prjadm.xml` - file with xml description of `PRJADM` database schema
    + `tasks.xml` - file with xml description of `TASKS` database schema
+ utils
    + `XmlParser.py` - contains function `create_list_of_objects_from_xml` which creates classes from xml description
    + `DBInitializer.py` - class, which contains functions for database initialization
    + `RAMToDBDConverter.py` - contains functions for inserting into database tables
    + `DDLPostgreSQLGenerator.py` - class, which contains functions for PostgreSQL ddl generation
    + `MSSQLMetadataGetter.py` - class, which contains functions for getting metadata from MS SQL to RAM
+ tests
    + `RAMToDBDTests.py` - test application of RAM to DBD
    + `XMLToRAMTests.py` - test application of XML to RAM
    + `RAMtoPostgreSQLTests.py` - test application of RAM to PostgreSQL
    + `MSSQLMetadataGetTests.py` - test application of getting metadata from MS SQL to RAM
+ `MainApplication.py` - in this application performed XML conversation to RAM
