class DBDSchema:
    parameters_order = None  # list of names of schema parameters, will be useful when RAM->XML
    tables_order = None  # list of table names, will be useful when RAM->XML
    domains_order = None  # list of domain names, will be useful when RAM->XML
    fulltext_engine = None
    version = None
    name = None
    description = None
    domains = None  # dictionary of Domain type objects
    tables = None  # dictionary of Table type objects

    def __init__(self, fulltext_engine):
        self.fulltext_engine = fulltext_engine
        self.domains = {}
        self.tables = {}
        self.parameters_order = []
        if (self.fulltext_engine is not None) | (self.fulltext_engine != ""):
            self.parameters_order.append("fulltext_engine")
        self.tables_order = []
        self.domains_order = []

    def set_fulltext_engine(self, fulltext_engine):
        self.fulltext_engine = fulltext_engine
        if (self.fulltext_engine is not None) | (self.fulltext_engine != ""):
            self.parameters_order.append("fulltext_engine")

    def get_fulltext_engine(self):
        return self.fulltext_engine

    def set_version(self, version):
        self.version = version
        if (self.version is not None) | (self.version != ""):
            self.parameters_order.append("version")

    def get_version(self):
        return self.version

    def set_name(self, name):
        self.name = name
        if (self.name is not None) | (self.name != ""):
            self.parameters_order.append("name")

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description
        if (self.description is not None) | (self.description != ""):
            self.parameters_order.append("description")

    def get_description(self):
        return self.description

    def set_domain(self, domain_name, domain):
        self.domains[domain_name] = domain
        self.domains_order.append(domain_name)

    def get_domain(self, domain_name):
        return self.domains.get(domain_name)

    def get_domains(self):
        return self.domains

    def set_table(self, table):
        self.tables[table.name] = table
        self.tables_order.append(table.name)

    def get_table(self, table_name):
        return self.tables.get(table_name)

    def get_tables(self):
        return self.tables

    def get_parameters_order(self):
        return self.parameters_order

    def get_tables_order(self):
        return self.tables_order
