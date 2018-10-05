class Field:
    name = None
    rname = None
    domain = None # object of Domain type
    props = None

    def __init__(self, name, rname):
        self.name = name
        self.rname = rname

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRname(self, rname):
        self.rname = rname

    def getRname(self):
        return self.rname

    def setDomain(self, domain):
        self.domain = domain

    def getDomain(self):
        return self.domain

    def setProps(self, props):
        self.props = []
        for property in props.split(","):
            self.props.append(property.strip())

    def getProps(self):
        return self.props