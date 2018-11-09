class Constraint:
    parameters_order = None  # list of names of constraints parameters, will be useful when RAM->XML
    kind = None
    items = None  # field name
    reference = None  # table name
    props = None

    def __init__(self, kind):
        self.parameters_order = []
        if (self.kind is not None) | (self.kind != ""):
            self.kind = kind
            self.parameters_order.append("kind")

    def set_kind(self, kind):
        if (self.kind is not None) | (self.kind != ""):
            self.kind = kind
            self.parameters_order.append("kind")


    def getKind(self):
        return self.kind

    def set_reference(self, reference):
        if (self.reference is not None) | (self.reference != ""):
            self.reference = reference
            self.parameters_order.append("reference")

    def get_reference(self):
        return self.reference

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

    def set_items(self, items):
        if (self.items is not None) | (self.items != ""):
            self.items = items
            self.parameters_order.append("items")


    def get_items(self):
        return self.items