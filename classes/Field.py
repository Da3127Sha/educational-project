class Field:
    parametersOrder = None  # list of names of field parameters
    name = None
    rname = None
    domain = None  # object of Domain type
    props = None

    def __init__(self, name, rname):
        self.name = name
        self.rname = rname
        self.parametersOrder = []
        if (self.name is not None) | (self.name != ""):
            self.parametersOrder.append("name")
        if (self.rname is not None) | (self.rname != ""):
            self.parametersOrder.append("rname")

    def setName(self, name):
        self.name = name
        if (self.name is not None) | (self.name != ""):
            self.parametersOrder.append("name")

    def getName(self):
        return self.name

    def setRname(self, rname):
        self.rname = rname
        if (self.rname is not None) | (self.rname != ""):
            self.parametersOrder.append("rname")

    def getRname(self):
        return self.rname

    def setDomain(self, domain):
        self.domain = domain
        if (self.domain is not None) | (self.domain != ""):
            self.parametersOrder.append("domain")

    def getDomain(self):
        return self.domain

    def setProps(self, props):
        self.props = []
        for property in props.split(","):
            self.props.append(property.strip())
        if (self.props is not None) | (len(self.props) != 0):
            self.parametersOrder.append("props")

    def getProps(self):
        return self.props