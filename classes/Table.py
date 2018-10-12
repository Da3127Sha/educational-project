class Table:
    parametersOrder = None  # list of names of table parameters
    fieldsOrder = None  # list of rnames of field parameters
    constraintsOrder = None  # list of items of constraint parameters
    indicesOrder = None  # list of field of index parameters
    name = None
    description = None
    props = None
    htTableFlags = None
    accessLevel = None
    fields = None  # list of Field type objects
    constraints = None  # list of Constraint type objects
    indices = None  # list of Index type objects

    def __init__(self, name):
        self.name = name
        self.fields = {}
        self.constraints = []
        self.indices = []
        self.parametersOrder = []
        if (self.name is not None) | (self.name != ""):
            self.parametersOrder.append("name")
        self.constraintsOrder = []
        self.fieldsOrder = []
        self.indicesOrder = []

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

    def setProps(self, props):
        self.props = []
        for property in props.split(","):
            self.props.append(property.strip())
        if (self.props is not None) | (len(self.props) != 0):
            self.parametersOrder.append("props")

    def getProps(self):
        return self.props

    def setHtTableFlags(self, htTableFlags):
        self.htTableFlags = htTableFlags
        if (self.htTableFlags is not None) | (self.htTableFlags != ""):
            self.parametersOrder.append("htTableFlags")

    def getHtTableFlags(self):
        return self.htTableFlags

    def setAccessLevel(self, accessLevel):
        self.accessLevel = accessLevel
        if (self.accessLevel is not None) | (self.accessLevel != ""):
            self.parametersOrder.append("accessLevel")

    def getAccessLevel(self):
        return self.accessLevel

    def setField(self, fieldName, field):
        self.fields[fieldName] = field
        if (self.fields is not None) | (len(self.fields) != 0):
            self.fieldsOrder.append(field.getRname())

    def getField(self, fieldName):
        return self.fields.get(fieldName)

    def getFields(self):
        return self.fields

    def setConstraint(self, constraint):
        self.constraints.append(constraint)
        self.constraintsOrder.append(constraint.getItems())

    def getConstraints(self):
        return self.constraints

    def setIndex(self, index):
        self.indices.append(index)
        self.indicesOrder.append(index.getFieldName())

    def getIndices(self):
        return self.indices