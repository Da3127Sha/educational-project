class DBDSchema:
    fulltextEngine = None
    version = None
    name = None
    description = None
    domains = None # list of Domain type objects
    tables = None # list of Table type objects

    def __init__(self, fulltextEngine):
        self.fulltextEngine = fulltextEngine
        self.domains = {}
        self.tables = {}

    def setFulltextEngine(self, fulltextEngine):
        self.fulltextEngine = fulltextEngine

    def getFulltextEngine(self):
        return self.fulltextEngine

    def setVersion(self, version):
        self.version = version

    def getVersion(self):
        return self.version

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setDomain(self, domainName, domain):
        self.domains[domainName] = domain

    def getDomain(self, domainName):
        return self.domains.get(domainName)

    def getDomains(self):
        return self.domains

    def setTable(self, tableName, table):
        self.tables[tableName] = table

    def getTable(self, tableName):
        return self.tables.get(tableName)

    def getTables(self):
        return self.tables