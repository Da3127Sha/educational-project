class Domain:
    parameters_order = None  # list of names of domain parameters, will be useful when RAM->XML
    name = None
    type = None
    align = None
    width = None
    char_length = None
    description = None
    props = None  # set of props
    precision = None
    scale = None
    length = None

    def __init__(self, name, type):
        self.parameters_order = []
        self.name = name
        if (self.name is not None) | (self.name != ""):
            self.parameters_order.append("name")
        self.type = type
        if (self.type is not None) | (self.type != ""):
            self.parameters_order.append("type")

    def set_name(self, name):
        self.name = name
        if (self.name is not None) | (self.name != ""):
            self.parameters_order.append("name")

    def get_name(self):
        return self.name

    def set_type(self, type):
        self.type = type
        if (self.type is not None) | (self.type != ""):
            self.parameters_order.append("type")

    def get_type(self):
        return self.type

    def set_align(self, align):
        if (self.align is not None) | (self.align != ""):
            self.align = list(align).pop(0)
            self.parameters_order.append("align")

    def get_align(self):
        return self.align

    def set_width(self, width):
        if (self.width is not None) | (self.width != ""):
            self.width = int(width)
            self.parameters_order.append("width")

    def get_width(self):
        return self.width

    def set_char_length(self, char_length):
        if (self.char_length is not None) | (self.char_length != ""):
            self.char_length = int(char_length)
            self.parameters_order.append("char_length")

    def get_char_length(self):
        return self.char_length

    def set_description(self, description):
        self.description = description
        if (self.description is not None) | (self.description != ""):
            self.parameters_order.append("description")

    def get_description(self):
        return self.description

    def set_props(self, props):
        props_temp = []
        for prop in props.split(","):
            props_temp.append(prop.strip())
        if (props_temp is not None) | (len(props_temp) != 0):
            self.parameters_order.append("props")
        self.props = set(props_temp)

    def get_props(self):
        return self.props

    def if_prop_exists(self, prop):
        if (prop in self.props):
            return True
        else:
            return False

    def set_precision(self, precision):
        if (self.precision is not None) | (self.precision != ""):
            self.precision = int(precision)
            self.parameters_order.append("precision")

    def get_precision(self):
        return self.precision

    def set_scale(self, scale):
        if (self.scale is not None) | (self.scale != ""):
            self.scale = int(scale)
            self.parameters_order.append("scale")

    def get_scale(self):
        return self.scale

    def set_length(self, length):
        if (self.length is not None) | (self.length != ""):
            self.length = int(length)
            self.parameters_order.append("length")

    def get_length(self):
        return self.length
