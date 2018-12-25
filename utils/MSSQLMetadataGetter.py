import pyodbc
from classes.DBDSchema import DBDSchema
from classes.Table import Table
from classes.Field import Field
from classes.Domain import Domain
from classes.Constraint import Constraint
from classes.Index import Index


class MSSQLMetadataGetter:
    connection = None
    cursor = None

    def __init__(self):
        print("start")
        try:
            self.connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};" +
                                             "Server=noutdexp\sqlexpress;" +
                                             "Database=northwind;" +
                                             "uid=mssqluser;" +
                                             "pwd=123;")
            self.cursor = self.connection.cursor()
        except (Exception) as error:
            print("Error while connecting to MS SQL", error)

    def get_metadata(self, schema_name):
        try:
            if (self.schema_exists(schema_name)):
                schema = DBDSchema(None)  # no fulltext_engine
                schema.set_name(schema_name)
                tables = []
                for t in self.cursor.tables(schema=schema_name, tableType='TABLE'):
                    if (t.table_name != "sysdiagrams"):  # exclude system table
                        print("table " + t.table_name)
                        table = Table(t.table_name)
                        table.set_description(t.remarks)
                        tables.append(table)
                        # TODO: props and flags

                print("-------------------------")
                for table in tables:
                    print("table " + table.name)
                    for column in self.cursor.columns(schema=schema_name):
                        if (column.table_name == table.name):
                            #print("column " + column.column_name)
                            field = Field(column.column_name, column.ordinal_position)
                            field.set_description(column.remarks)
                            # TODO: field and domain props
                            domain_name = "Unnamed_" + table.name + "_" + field.name
                            domain = Domain(domain_name, column.type_name, True)
                            domain.set_char_length(column.column_size)
                            domain.set_position_for_unnamed(table.name, field.name)
                            #print("type name " + str(column.type_name))
                            #print("type length " + str(column.column_size))
                            field.set_domain(domain.name)
                            schema.set_domain(domain.name, domain)

                            table.set_field(field.name, field)

                    for pk in self.cursor.primaryKeys(schema=schema_name, table=table.name):
                        primary_key = Constraint("PRIMARY", 1)
                        primary_key.set_items(pk.column_name)
                        primary_key.set_name(pk.pk_name)
                        print("pk " + pk.pk_name)
                        print("pk col " + pk.column_name)
                        table.set_constraint(primary_key)

                    # TODO: fk and indices

                    schema.set_table(table)


        except (Exception) as error:
            print("Error while connecting to MS SQL", error)
        finally:
            if (self.connection):
                self.cursor.close()
                self.connection.close()
                print("MS SQL connection is closed")

    def schema_exists(self, schema_name):
        self.cursor.execute("""select name from sys.schemas where name=?""", (schema_name))
        row = self.cursor.fetchone()
        if (row.name == schema_name):
            print("Схема найдена")
            return True
        else:
            return False