class Field:
    parameters_order = None  # list of names of field parameters, will be useful when RAM->XML
    name = None
    rname = None
    domain = None  # name of Domain
    props = None
    position = None
    description = None

    def __init__(self, name, position):
        self.parameters_order = []
        if (self.name is not None) | (self.name != ""):
            self.name = name
            self.parameters_order.append("name")
        if (self.position is not None) | (self.position != ""):
            self.position = int(position)

    def set_name(self, name):
        if (self.name is not None) | (self.name != ""):
            self.name = name
            self.parameters_order.append("name")

    def get_name(self):
        return self.name

    def set_rname(self, rname):
        if (self.rname is not None) | (self.rname != ""):
            self.rname = rname
            self.parameters_order.append("rname")

    def get_rname(self):
        return self.rname

    def set_domain(self, domain):
        if (self.domain is not None) | (self.domain != ""):
            self.domain = domain
            self.parameters_order.append("domain")

    def get_domain(self):
        return self.domain

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

    def set_description(self, description):
        self.description = description
        if (self.description is not None) | (self.description != ""):
            self.parameters_order.append("description")

    def get_description(self):
        return self.description