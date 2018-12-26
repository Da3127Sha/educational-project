from lxml import etree


class RAMToDBDConverter:
    schema = None

    def __init__(self, schema):
        self.schema = schema

    def create_schema(self, schema):
        schema_root = etree.Element('dbdSchema')

        if schema.fulltext_engine is not None:
            schema_root.set("fulltext_engine", schema.fulltext_engine)
        if schema.version is not None:
            schema_root.set("version", str(schema.version))
        if schema.name is not None:
            schema_root.set("name", schema.name)
        if schema.description is not None:
            schema_root.set("description", schema.description)

        # создание доменов
        domains_root = etree.Element("domains")
        for domain in schema.domains.values():
            self.create_domain(domains_root, domain)
        schema_root.append(domains_root)

        # создание таблиц
        tables_root = etree.Element("tables")
        for table in schema.tables.values():
            self.create_table(domains_root, table)
        schema_root.append(tables_root)

        return etree.tostring(schema_root, pretty_print=True).decode()

    def create_domain(self, root_elem, domain):
        element = etree.Element("domain")

        if domain.name is not None:
            element.set("name", domain.name)
        if domain.type is not None:
            element.set("type", domain.type)
        if domain.align is not None:
            element.set("align", domain.align)
        if domain.width is not None:
            element.set("width", str(domain.width))
        if domain.char_length is not None:
            element.set("char_length", str(domain.char_length))
        if domain.description is not None:
            element.set("description", domain.description)
        if domain.props is not None:
            element.set("props", ", ".join(domain.props))
        if domain.precision is not None:
            element.set("precision", str(domain.precision))
        if domain.scale is not None:
            element.set("scale", str(domain.scale))
        if domain.length is not None:
            element.set("length", str(domain.length))

        root_elem.append(element)

    def create_table(self, root_elem, table):
        element = etree.Element("table")

        if table.name is not None:
            element.set("name", table.name)
        if table.description is not None:
            element.set("description", table.description)
        if table.props is not None:
            element.set("props", ", ".join(table.props))
        if table.ht_table_flags is not None:
            element.set("ht_table_flags", table.ht_table_flags)
        if table.access_level is not None:
            element.set("access_level", str(table.access_level))
        if table.means is not None:
            element.set("means", str(table.means))

        # создание полей
        for field in table.fields.values():
            self.create_field(element, field, table.name)
        # создание ограничений
        for index in table.indices:
            self.create_index(element, index)
        # создание индексов
        for constraint in table.constraints:
            self.create_constraint(element, constraint)

        root_elem.append(element)

    def create_field(self, root_elem, field, table_name):
        element = etree.Element("field")

        if field.name is not None:
            element.set("name", field.name)
        if field.rname is not None:
            element.set("rname", field.rname)
        if field.domain is not None:

            if type(field.domain) == str:
                domain_name = field.domain
            elif field.domain.name is not None:
                domain_name = field.domain.name

            if domain_name in self.schema.domains:
                domain_name = "Unnamed_" + table_name + field.name

            element.set("domain", domain_name)
        if field.description is not None:
            element.set("description", field.description)
        if field.props is not None:
            element.set("props", ", ".join(field.props))

        root_elem.append(element)

    def create_index(self, root_elem, index):
        element = etree.Element("index")

        if index.field_name is not None:
            element.set("name", index.field_name)
        if index.props is not None:
            element.set("props", ", ".join(index.props))

        root_elem.append(element)

    def create_constraint(self, root_elem, constraint):
        element = etree.Element("constraint")

        if constraint.kind is not None:
            element.set("kind", constraint.kind)
        if constraint.items is not None:
            element.set("items", constraint.items)
        if constraint.reference is not None:
            element.set("reference", constraint.reference)
        if constraint.position is not None:
            element.set("position", str(constraint.position))
        if constraint.props is not None:
            element.set("props", ", ".join(constraint.props))

        root_elem.append(element)