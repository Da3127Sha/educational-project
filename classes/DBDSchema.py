class DBDSchema:
    parametersOrder = None  # list of names of schema parameters
    tablesOrder = None  # list of table names
    domainsOrder = None  # list of domain names
    fulltextEngine = None
    version = None
    name = None
    description = None
    domains = None  # dictionary of Domain type objects
    tables = None  # dictionary of Table type objects

    def __init__(self, fulltextEngine):
        self.fulltextEngine = fulltextEngine
        self.domains = {}
        self.tables = {}
        self.parametersOrder = []
        if (self.fulltextEngine is not None) | (self.fulltextEngine != ""):
            self.parametersOrder.append("fulltextEngine")
        self.tablesOrder = []
        self.domainsOrder = []

    def setFulltextEngine(self, fulltextEngine):
        self.fulltextEngine = fulltextEngine
        if (self.fulltextEngine is not None) | (self.fulltextEngine != ""):
            self.parametersOrder.append("fulltextEngine")

    def getFulltextEngine(self):
        return self.fulltextEngine

    def setVersion(self, version):
        self.version = version
        if (self.version is not None) | (self.version != ""):
            self.parametersOrder.append("version")

    def getVersion(self):
        return self.version

    def setName(self, name):
        self.name = name
        if (self.name is not None) | (self.name != ""):
            self.parametersOrder.append("name")

    def getName(self):
        return self.name

    def setDescription(self, description):
        self.description = description
        if (self.description is not None) | (self.description != ""):
            self.parametersOrder.append("description")

    def getDescription(self):
        return self.description

    def setDomain(self, domainName, domain):
        self.domains[domainName] = domain
        self.domainsOrder.append(domainName)

    def getDomain(self, domainName):
        return self.domains.get(domainName)

    def getDomains(self):
        return self.domains

    def setTable(self, tableName, table):
        self.tables[tableName] = table
        self.tablesOrder.append(table.getName())

    def getTable(self, tableName):
        return self.tables.get(tableName)

    def getTables(self):
        return self.tables

    def getParametersOrder(self):
        return self.parametersOrder

    def getTablesOrder(self):
        return self.tablesOrder