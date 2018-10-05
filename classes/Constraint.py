class Constraint:
    kind = None
    items = None # object of Field name
    reference = None # object of Table name
    props = None

    def __init__(self, kind):
        self.kind = kind

    def setKind(self, kind):
        self.kind = kind

    def getKind(self):
        return self.kind

    def setReference(self, reference):
        self.reference = reference

    def getReference(self):
        return self.reference

    def setProps(self, props):
        self.props = []
        for property in props.split(","):
            self.props.append(property.strip())

    def getProps(self):
        return self.props

    def setItems(self, items):
        self.items = items

    def getItems(self):
        return self.items