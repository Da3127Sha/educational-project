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
    + `XmlParser.py` - contains function `createObjectFromXml` which creates classes from xml description
    + `DBInitializer` - class, which contains functions for database initialization
    + `RAMToDBDConverter.py` - contains functions for inserting into database tables
+ `MainApplication.py` - main application
