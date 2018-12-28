from utils.MSSQLMetadataGetter import *
from utils.DDLPostgreSQLGenerator import *
from utils.MSSQLToPostgreSQL import *

SCHEMA = "dbo"

metadata_getter = MSSQLMetadataGetter()
schema = metadata_getter.get_metadata(SCHEMA)

ddl_generator = DDLPostgreSQLGenerator()
ddl_generator.generate_DDL(schema)

main(schema)