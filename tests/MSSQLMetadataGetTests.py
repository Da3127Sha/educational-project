from utils.MSSQLMetadataGetter import *

SCHEMA = "dbo"

metadata_getter = MSSQLMetadataGetter()
metadata_getter.get_metadata(SCHEMA)