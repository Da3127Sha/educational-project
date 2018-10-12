class Domain:
    parametersOrder = None  # list of names of domain parameters
    name = None
    type = None
    align = None
    width = None
    charLength = None
    description = None
    props = None
    precision = None
    scale = None
    length = None

    def __init__(self, name, type):
        self.parametersOrder = []
        self.name = name
        if (self.name is not None) | (self.name != ""):
            self.parametersOrder.append("name")
        self.type = type
        if (self.type is not None) | (self.type != ""):
            self.parametersOrder.append("type")

    def setName(self, name):
        self.name = name
        if (self.name is not None) | (self.name != ""):
            self.parametersOrder.append("name")

    def getName(self):
        return self.name

    def setType(self, type):
        self.type = type
        if (self.type is not None) | (self.type != ""):
            self.parametersOrder.append("type")

    def getType(self):
        return self.type

    def setAlign(self, align):
        self.align = align
        if (self.align is not None) | (self.align != ""):
            self.parametersOrder.append("align")

    def getAlign(self):
        return self.align

    def setWidth(self, width):
        self.width = width
        if (self.width is not None) | (self.width != ""):
            self.parametersOrder.append("width")

    def getWidth(self):
        return self.width

    def setCharLength(self, charLength):
        self.charLength = charLength
        if (self.charLength is not None) | (self.charLength != ""):
            self.parametersOrder.append("charLength")

    def getCharLength(self):
        return self.charLength

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

    def setPrecision(self, precision):
        self.precision = precision
        if (self.precision is not None) | (self.precision != ""):
            self.parametersOrder.append("precision")

    def getPrecision(self):
        return self.precision

    def setScale(self, scale):
        self.scale = scale
        if (self.scale is not None) | (self.scale != ""):
            self.parametersOrder.append("scale")

    def getScale(self):
        return self.scale

    def setLength(self, length):
        self.length = length
        if (self.length is not None) | (self.length != ""):
            self.parametersOrder.append("length")

    def getLength(self):
        return self.length


