class Domain:
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
        self.name = name
        self.type = type

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setAlign(self, align):
        self.align = align

    def getAlign(self):
        return self.align

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setCharLength(self, charLength):
        self.charLength = charLength

    def getCharLength(self):
        return self.charLength

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

    def setPrecision(self, precision):
        self.precision = precision

    def getPrecision(self):
        return self.precision

    def setScale(self, scale):
        self.scale = scale

    def getScale(self):
        return self.scale

    def setLength(self, length):
        self.length = length

    def getLength(self):
        return self.length


