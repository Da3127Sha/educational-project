class Table:
    parameters_order = None  # list of names of table parameters, will be useful when RAM->XML
    #fieldsOrder = None  # list of rnames of field parameters
    #constraintsOrder = None  # list of items of constraint parameters
    #indicesOrder = None  # list of field of index parameters
    name = None
    description = None
    props = None
    ht_table_flags = None
    access_level = None
    fields = None  # dictionary of Field type objects
    constraints = None  # list of Constraint type objects
    indices = None  # list of Index type objects
    temporal_mode = None
    means = None

    def __init__(self, name):
        self.name = name
        self.fields = {}
        self.constraints = []
        self.indices = []
        self.parametersOrder = []
        if (self.name is not None) | (self.name != ""):
            self.parameters_order.append("name")
        #self.constraints_order = []
        #self.fieldsOrder = []
        #self.indicesOrder = []

    def set_name(self, name):
        self.name = name
        if (self.name is not None) | (self.name != ""):
            self.parameters_order.append("name")

    def get_name(self):
        return self.name

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

    def set_ht_table_flags(self, ht_table_flags ):
        self.ht_table_flags = ht_table_flags
        if (self.ht_table_flags is not None) | (self.ht_table_flags != ""):
            self.parametersOrder.append("ht_table_flags ")

    def get_ht_table_flags(self):
        return self.ht_table_flags

    def set_access_level(self, access_level):
        if (access_level is not None) | (access_level != ""):
            self.access_level = int(access_level)
            self.parameters_order.append("access_level")

    def get_access_level(self):
        return self.access_level

    def set_field(self, field_name, field):
        self.fields[field_name] = field
        #if (self.fields is not None) | (len(self.fields) != 0):
            #self.fields_order.append(field.rname)

    def get_field(self, field_name):
        return self.fields.get(field_name)

    def get_fields(self):
        return self.fields

    def set_constraint(self, constraint):
        self.constraints.append(constraint)
        #self.constraints_order.append(constraint.getItems())

    def get_constraints(self):
        return self.constraints

    def set_index(self, index):
        self.indices.append(index)
        #self.indicesOrder.append(index.getFieldName())

    def get_indices(self):
        return self.indices