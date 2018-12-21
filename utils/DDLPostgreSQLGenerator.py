import psycopg2
from psycopg2 import sql
from classes.DBDSchema import DBDSchema

USERNAME = "postgres"


class DDLPostgreSQLGenerator:
    connection = None
    cursor = None
    prefix = None

    def __init__(self):
        try:
            self.connection = psycopg2.connect(host="localhost",
                                               port="5432",
                                               database="mydb",
                                               user=USERNAME,
                                               password="postgres")
            self.cursor = self.connection.cursor()
        except (Exception) as error:
            print("Error while connecting to PostgreSQL", error)

    def generate_DDL(self, schema):
        try:
            if (self.schema_exists(schema.get_name())):
                self.create_schema(schema.get_name())
                self.prefix = schema.get_name() + "."
                self.create_domains(schema.get_domains().values())
                self.create_tables(schema.get_tables().values())
                self.create_foreign_keys(schema)
                self.create_indices(schema.get_tables().values())
                self.connection.commit()
            else: print("Схема существует")
        except (Exception) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (self.connection):
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")

    def create_schema(self, schema_name):
        self.cursor.execute(sql.SQL("""CREATE SCHEMA {name}
                                    AUTHORIZATION {user}"""
                                    .format(name=schema_name,
                                            user=USERNAME)))
        print("Создали схему " + schema_name)

    def create_domains(self, domains):
        for domain in domains:
            if ((domain.type.lower() == "blob") or
                    ((domain.type.lower() == "byte"))):
                domain_type = "bytea"
            elif ((domain.type.lower() == "string") or
                  ((domain.type.lower() == "word")) or
                  ((domain.type.lower() == "code"))):
                domain_type = "varchar"
            elif (domain.type.lower() == "largeint"):
                domain_type = "bigint"
            elif (domain.type.lower() == "memo"):
                domain_type = "text"
            else:
                domain_type = domain.type.lower()

            if ((domain_type.lower() == "varchar") and (
                    (domain.char_length is not None) and
                    (domain.char_length != ""))):
                domain_type = domain_type + "(" \
                              + str(domain.char_length) + ")"
            self.cursor.execute(
                sql.SQL("""CREATE DOMAIN {name} AS {type}"""
                        .format(name=self.prefix + domain.name,
                                type=domain_type)))

    def create_tables(self, tables):
        for table in tables:
            query = """CREATE TABLE {name} (""" \
                .format(name=self.prefix + table.name)
            pk = ""
            for constraint in table.get_constraints():
                if (constraint.kind.lower() == "primary"):
                    pk = constraint.items
            step = 0
            for field in table.get_fields().values():
                if (step != 0):
                    query = query + ", "
                query = query + """{field_name} {domain}""" \
                    .format(field_name=field.name,
                            domain=self.prefix + field.domain)
                if (field.name == pk):
                    query = query + " PRIMARY KEY"
                step += 1
            query = query + ")"
            self.cursor.execute(sql.SQL(query))

    def create_foreign_keys(self, schema):
        for table in schema.get_tables().values():
            for constraint in table.get_constraints():
                if (constraint.kind.lower() != "primary"):
                    query = """ALTER TABLE {name} """ \
                        .format(name=self.prefix + table.name)
                    query = query + """ADD CONSTRAINT {fk_name} FOREIGN KEY ({field_name}) """ \
                        .format(fk_name=constraint.items, field_name=constraint.items) + \
                            "REFERENCES {parent_table} " \
                                .format(parent_table=self.prefix + constraint.reference) + \
                            "({parent_pk})" \
                                .format(parent_pk=self.get_parent_pk(constraint.reference,
                                                                     schema))
                    if ((constraint.if_prop_exists("full_cascading_delete".lower())) or
                            (constraint.if_prop_exists("cascading_delete".lower()))):
                        query = query + "ON DELETE CASCADE"
                    self.cursor.execute(sql.SQL(query))

    def get_parent_pk(self, reference, schema):
        pk = ""
        for constraint in schema.get_table(reference).get_constraints():
            if (constraint.kind.lower() == "primary"):
                pk = constraint.items
        return pk

    def create_indices(self, tables):
        for table in tables:
            for index in table.get_indices():
                query = "CREATE "
                if (index.if_prop_exists("uniqueness".lower())):
                    query = query + "UNIQUE "
                query = query + "INDEX {name} " \
                    .format(name=self.prefix.replace(".", "_") +
                                 table.name + "_" + index.field_name) + \
                        "ON {table_name} ({column_name}) " \
                            .format(table_name=self.prefix + table.name,
                                    column_name=index.field_name)
                self.cursor.execute(sql.SQL(query))

    def schema_exists(self, name):
        self.cursor.execute(
            sql.SQL("""SELECT schema_name FROM information_schema.schemata """ +
                   """WHERE schema_name = '""" + name.lower() + "'"))
        temp_name = self.cursor.fetchone()
        if (self.cursor.fetchone() is not None):
            return False
        else:
            return True
