class Node:
    split_value = ""
    output_values = []
    node_number = 0
    is_leaf = True
    to_be_deleted = False
    classification = ""
    id = 0
    iD = 0
    # constructor that creates a Node object and sets its classification value
    # and node type (leaf or non-leaf)

    def __init__(self, ex=[], out=[], number=0):
        self.instance_list = ex
        self.outputValues = out
        self.node_number = number
        self.set_node_type()
        self.set_classification()
        self.id = self.id + 1

    # returns the number of the node
    def get_number(self):
        return self.node_number

    # Automatically sets classification if this is a leaf node
    def set_classification(self):
        if len(self.instance_list) == 0:
            self.classification = self.get_majority_classification()
        if self.is_leaf:
            for i in self.outputValues:
                if self.outputValues[i] == 1:
                    self.classification = 1
                elif self.outputValues[i] == 0:
                    self.classification = 0
        return self.classification

    def get_classification(self):
        return self.classification

    def get_split_value(self):
        return self.split_value

    def get_attribute(self):
        return self.splitAttribute

    def set_node_type(self):
        if len(self.instance_list) == 0:
            self.is_leaf = True
        else:
            for e in self.outputValues:
                if not e == self.get_classification():
                    self.is_leaf = False
                else:
                    self.is_leaf = True

    def is_leaf(self):
        return self.is_leaf

    def set_attribute(self, f):
        self.splitAttribute = f

    def set_attribute_value(self, val):
        self.split_value = val

    def get_instances(self):
        return self.instance_list

    def get_split_value(self):
        return self.split_value

    def get_majority_classification(self):
        size = len(self.outputValues)
        category = []

        count_neg = 0
        count_pos = 0
        i = 0
        while i < size:
            if self.outputValues[i] == 1:
                count_pos = count_pos + 1
            elif self.outputValues[i] == 0:
                count_neg = count_neg + 1
            i = i + 1

        if count_pos > count_neg:
            self.classification = 1
        else:
            self.classification = 0

        return self.classification

    def get_id(self):
        return self.id

