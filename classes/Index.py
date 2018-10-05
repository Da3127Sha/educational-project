class Index:
    fieldName = None # object of Field name
    props = None

    def __init__(self, fieldName):
        self.field = fieldName

    def setFieldName(self, fieldName):
        self.fieldName = fieldName

    def getFieldName(self):
        return self.fieldName

    def setProps(self, props):
        self.props = []
        for property in props.split(","):
            self.props.append(property.strip())

    def getProps(self):
        return self.props