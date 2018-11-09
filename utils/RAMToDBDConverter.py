import sqlite3
from classes.DBDSchema import DBDSchema
from classes.Domain import Domain
from classes.Table import Table
from classes.Field import Field
from classes.Constraint import Constraint
from classes.Index import Index

CURRENT_DBD_VERSION = '3.1'
TEMP_VALUE = 1

class RAMToDBDConverter:

    file_name = None
    connection = None
    cursor = None
    type_id_dict = None
    schema_id_dict = None
    table_id_dict = None
    domain_id_dict = None

    def __init__(self, file_name):
        self.type_id_dict = {}
        self.schema_id_dict = {}
        self.table_id_dict = {}
        self.domain_id_dict = {}

        self.file_name = file_name
        self.connection = sqlite3.connect(self.file_name)

    def get_type_id_dict(self):
        self.cursor.execute("""
        select id, type_id from dbd$data_types """)
        records = self.cursor.fetchall()
        for i, record in enumerate(records):
            self.type_id_dict[record[1]] = record[0]

    def get_schema_id_dict(self):
        self.cursor.execute("""
        select id, name from dbd$schemas """)
        records = self.cursor.fetchall()
        for i, record in enumerate(records):
            self.schema_id_dict[record[1]] = record[0]

    def get_domain_id_dict(self):
        self.cursor.execute("""
        select id, name from dbd$domains """)
        records = self.cursor.fetchall()
        for i, record in enumerate(records):
            self.domain_id_dict[record[1]] = record[0]

    def get_table_id_dict(self):
        self.cursor.execute("""
        select id, name from dbd$tables """)
        records = self.cursor.fetchall()
        for i, record in enumerate(records):
            self.table_id_dict[record[1]] = record[0]

    # TODO:
    def RAM_to_DBD(self, schemas):
        self.cursor = self.connection.cursor()
        self.cursor.execute("pragma foreign_keys=on;")
        self.get_type_id_dict()

        self.insert_schemas(schemas)
        self.get_schema_id_dict()
        for schema in schemas:
            self.insert_tables(schema.tables, schema.name)
            self.insert_domains(schema.domains)
        self.get_table_id_dict()
        self.get_domain_id_dict()
        for schema in schemas:
            for table in schema.tables.values():
                self.insert_fields(table.fields, table.name)
                self.insert_constraints(table.constraints, table.name)

        self.connection.commit()
        self.cursor.close()

    def insert_schemas(self, schemas):
        self.cursor.executemany(
            """insert into dbd$schemas (
            name,
            fulltext_engine,
            version,
            description) values (?)""",
            list((schema.name,
                  schema.fulltext_engine,
                  schema.version,
                  schema.description
                  ) for schema in schemas)
        )

    def insert_domains(self, domains):
        self.cursor.executemany(
            """insert into dbd$schemas (
            name,
            description,
            data_type_id,
            length,
            char_length,
            precision,
            scale,
            width,
            align,
            show_null,
            show_lead_nulls,
            thousands_separator,
            summable,
            case_sensitive) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            list((domain.name,
                  domain.description,
                  self.type_id_dict.get(domain.type),  # getting data type id
                  domain.length,
                  domain.char_length,
                  domain.precision,
                  domain.scale,
                  domain.width,
                  domain.align,
                  domain.if_prop_exists("show_null"),
                  domain.if_prop_exists("show_lead_nulls"),
                  domain.if_prop_exists("thousands_separator"),
                  domain.if_prop_exists("summable"),
                  domain.if_prop_exists("case_sensitive"),
                  ) for domain in domains.values())
        )

    def insert_tables(self, tables, schema_name):
        self.cursor.executemany(
            """insert into dbd$tables (
            schema_id, 
            name,
            description,
            can_add,
            can_edit,
            can_delete,
            ht_table_flags,
            access_level,
            temporal_mode,
            means) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            list((self.schema_id_dict.get(schema_name),
                  table.name,
                  table.description,
                  table.if_prop_exists("add"),
                  table.if_prop_exists("edit"),
                  table.if_prop_exists("delete"),
                  table.ht_table_flags,
                  table.access_level,
                  table.temporal_mode,
                  table.means,
                  ) for table in tables.values())
        )

    def insert_fields(self, fields, table_name):
        self.cursor.executemany(
            """insert into dbd$fields (
            table_id,
            position,
            name,
            russian_short_name,
            description,
            domain_id,
            can_input,
            can_edit,
            show_in_grid,
            show_in_details,
            is_mean,
            autocalculated,
            required) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            list((self.table_id_dict.get(table_name),
                  field.position,
                  field.name,
                  field.rname,
                  field.description,
                  self.domain_id_dict.get(field.domain),
                  field.if_exists("input"),
                  field.get_prop_if_exists("edit"),
                  field.get_prop_if_exists("show_in_grid"),
                  field.get_prop_if_exists("show_in_details"),
                  field.get_prop_if_exists("is_mean"),
                  field.get_prop_if_exists("autocalculated"),
                  field.get_prop_if_exists("required")
                  ) for field in fields.values())
        )

    def insert_constraints(self, constraints, table_name):
        self.cursor.executemany(
            """insert into dbd$constraints (
            table_id,
            name,
            constraint_type,
            reference,
            has_value_edit,
            cascading_delete) values (?, ?, ?, ?, ?, ?)""",
            list((self.schema_id_dict.get(table_name),
                  constraint.kind,
                  list(constraint.kind).pop(0),
                  self.table_id_dict.get(constraint.reference),
                  constraint.if_prop_exists("has_value_edit"),
                  constraint.if_prop_exists("cascading_delete")
                  ) for constraint in constraints)
        )
