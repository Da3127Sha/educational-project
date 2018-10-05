class Table:
    name = None
    description = None
    props = None
    htTableFlags = None
    accessLevel = None
    fields = None # list of Field type objects
    constraints = None # list of Constraint type objects
    indices = None # list of Index type objects

    def __init__(self, name):
        self.name = name
        self.fields = {}
        self.constraints = []
        self.indices = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setProps(self, props):
        self.props = []
        for property in props.split(","):
            self.props.append(property.strip())

    def getProps(self):
        return self.props

    def setHtTableFlags(self, htTableFlags):
        self.htTableFlags = htTableFlags

    def getHtTableFlags(self):
        return self.htTableFlags

    def setAccessLevel(self, accessLevel):
        self.accessLevel = accessLevel

    def getAccessLevel(self):
        return self.accessLevel

    def setField(self, fieldName, field):
        self.fields[fieldName] = field

    def getField(self, fieldName):
        return self.fields.get(fieldName)

    def getFields(self):
        return self.fields

    def setConstraint(self, constraint):
        self.constraints.append(constraint)

    def getConstraints(self):
        return self.constraints

    def setIndex(self, index):
        self.indices.append(index)

    def getIndices(self):
        return self.indices