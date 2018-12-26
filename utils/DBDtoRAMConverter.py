import sqlite3

from classes.DBDSchema import DBDSchema
from classes.Domain import Domain
from classes.Table import Table
from classes.Field import Field
from classes.Constraint import Constraint
from classes.Index import Index


class DBDtoRAM:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.connection.row_factory = sqlite3.Row

    def dbd_to_ram(self):
        return self.get_schema()

    def get_schema(self):
        cursor = self.connection.cursor()

        schema_result = cursor.execute(
            """
            select
                name,
                fulltext_engine,
                version,
                description
            from dbd$schemas
            """).fetchone()

        schema_fulltext_engine = schema_result["fulltext_engine"]
        schema = DBDSchema(schema_fulltext_engine)
        schema.name = schema_result["name"]
        schema.description = schema_result["description"]
        schema.version = schema_result["version"]

        schema.domains = self.get_domains()
        schema.tables = self.get_tables()

        self.connection.commit()
        self.connection.close()

        return schema

    def get_domains(self):
        cursor = self.connection.cursor()
        domain_list = list()
        domain_attributes = cursor.execute("""select 
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
            case_sensitive
            from dbd$domains
            """).fetchall()

        for value in domain_attributes:
            domain_name = value["name"]
            domain_type = cursor.execute("""
                select type_id
                from dbd$data_types 
                where dbd$data_types.id = ?""", (value["data_type_id"],)).fetchone()[0]
            domain_unnamed = True
            domain = Domain(domain_name, domain_type, domain_unnamed)
            domain.name = value["name"]
            domain.description = value["description"]
            domain.length = value["length"]
            domain.char_length = value["char_length"]
            domain.precision = value["precision"]
            domain.scale = value["scale"]
            domain.width = value["width"]
            domain.align = value["align"]
            props = list()
            props.append(value["show_null"])
            props.append(value["show_lead_nulls"])
            props.append(value["case_sensitive"])
            props.append(value["summable"])
            domain.props = props
            domain_list.append(domain)

        return domain_list

    def get_tables(self):
        cursor = self.connection.cursor()
        tables_list = list()

        tables_attributes = cursor.execute("""\
            select
            id,
            name,
            description,
            can_add,
            can_edit,
            can_delete,
            ht_table_flags,
            access_level,
            temporal_mode,
            means
            from dbd$tables""").fetchall()

        for value in tables_attributes:
            table_id = value["id"]
            table_name = value["name"]
            table = Table(table_name)
            table.description = value["description"]
            props = list()
            props.append(value["can_add"])
            props.append(value["can_edit"])
            props.append(value["can_delete"])
            table.props = props
            table.ht_table_flags = value["ht_table_flags"]
            table.access_level = value["access_level"]
            table.temporal_mode = value["temporal_mode"]
            table.means = value["means"]

            table.fields = self.get_fields(table_id)
            table.constraints = self.get_constraints(table_id)
            table.indices = self.get_indices(table_id)

            tables_list.append(table)

        return tables_list

    def get_fields(self, table_id):
        cursor = self.connection.cursor()
        field_list = list()
        filed_attributes = cursor.execute("""\
        select 
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
            required 
        from dbd$fields
        where dbd$fields.table_id = ?""", (table_id,)).fetchall()

        for value in filed_attributes:
            field_name = value["name"]
            field_position = value["position"]
            field = Field(field_name, field_position)
            field.rname = value["russian_short_name"]
            field.description = value["description"]
            props = list()
            props.append(value["can_input"])
            props.append(value["can_edit"])
            props.append(value["show_in_grid"])
            props.append(value["show_in_details"])
            props.append(value["is_mean"])
            props.append(value["autocalculated"])
            props.append(value["required"])
            field.props = props
            domain_id = value["domain_id"]
            field.domain = cursor.execute("""
                        select name 
                        from dbd$domains 
                        where dbd$domains.id = ?""", (domain_id,)).fetchone()[0]
            field_list.append(field)

        return field_list

    def get_constraints(self, table_id):
        cursor = self.connection.cursor()
        constraints_list = list()
        constraints_attributes = cursor.execute("""
            select
            id,
            table_id,
            name,
            constraint_type,
            reference,
            has_value_edit,
            cascading_delete
            from dbd$constraints
            where dbd$constraints.table_id = ?""", (table_id,)).fetchall()

        for value in constraints_attributes:
            id = value["id"]
            kind = value["constraint_type"]
            constraint = Constraint(kind, 1)
            constraint.reference = value["reference"]
            props = list()
            props.append(value["has_value_edit"])
            props.append(value["cascading_delete"])
            constraint.props = props

            constraint.items = cursor.execute("""
                    select name
                    from dbd$fields
                    where dbd$fields.id = (\
                            select field_id
                            from dbd$constraint_details\
                            where dbd$constraint_details.constraint_id = ?)""",
                                              (id,)).fetchone()[0]

            constraints_list.append(constraint)

        return constraints_list

    def get_indices(self, table_id):
        cursor = self.connection.cursor()
        indices_list = list()
        indices_attributes = cursor.execute("""
            select 
                id,
                table_id
            from dbd$indices\
            where dbd$indices.table_id = ?""", (table_id,)).fetchall()

        for value in indices_attributes:
            id = value["id"]
            table_id = value["table_id"]

            field = cursor.execute("""
                select 
                name,
                position
                from dbd$fields 
                where dbd$fields.id = (\
                    select 
                    field_id 
                    from dbd$index_details\
                    where dbd$index_details.index_id = ?)""", (id,)).fetchone()

            field_name = field["name"]
            field_position = field["position"]
            index = Index(field_name, field_position)

            indices_list.append(index)
        return indices_list