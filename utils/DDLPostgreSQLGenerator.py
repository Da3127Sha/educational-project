import psycopg2
from psycopg2 import sql
from classes.DBDSchema import DBDSchema

USERNAME = "postgres";


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
            self.create_schema(schema.get_name())
            self.prefix = schema.get_name() + "."
            self.create_domains(schema.get_domains().values())
            #self.create_tables(schema.get_tables().values())
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

    # TODO: add properties, width, length, etc...
    def create_domains(self, domains):
        for domain in domains:
            if ((domain.type.lower() == "blob")or
                  ((domain.type.lower() == "byte"))):
                domain_type = "bytea"
            elif ((domain.type.lower() == "string")or
                  ((domain.type.lower() == "word"))or
                  ((domain.type.lower() == "code"))):
                domain_type = "varchar"
            elif (domain.type.lower() == "largeint"):
                domain_type = "bigint"
            elif (domain.type.lower() == "memo"):
                domain_type = "text"
            else:
                domain_type = domain.type
            self.cursor.execute(
                sql.SQL("""CREATE DOMAIN {name} AS {type}"""
                        .format(name=self.prefix + domain.name,
                                type=domain_type)))


