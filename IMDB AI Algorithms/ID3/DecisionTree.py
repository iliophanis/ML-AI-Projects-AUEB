
class DecisionTree:
    children = []
    class_correct = ""
    class_wrong = ""

    def __init__(self, root=None):
        self.root = root

    def add_tree(self, dt):
        self.children.append(dt)

    def get_number_of_nodes(self):
        total = 0

        for dt in self.children:
            i = 0
            while i < len(self.children):
                if not dt.children[i].root.is_leaf:
                    total = total + 1
                i = i + 1
        return total

    # Decides if this tree correctly classifies the given instance
    def classify(self, instance, words):
        result = 0.0
        # if node is leaf only compare the classifications
        if self.root.is_leaf:
            if self.root.classification == instance:
                result = 1.0
                self.class_correct = instance
            else:
                result = 0.0
                self.class_correct = instance
                self.class_wrong = self.root.classification
        # If the node is a leaf node but doesn't have a split value declared
        # use the majority classification to compare
        elif self.root.get_split_value() == '':
            if self.root.get_majority_classification() == instance:
                result = 1.0
                self.class_correct = instance
            else:
                result = 0.0
                self.class_correct = instance
                self.class_wrong = self.root.classification

        else:
            if self.root.split_value == words:
                for x in self.children:
                    i = 0
                    thesize = x.root.instance_list
                    while i < len(thesize):
                        if x.root.instance_list[i] == instance:
                            result = self.classify(x.root.instance_list[i])
                        i = i + 1
            else:
                result = 0.0

        return result

    def get_root_node(self):
        return self.root

    def get_children(self):
        return self.children

    def set_classifier_class_correct(self, c):
        self.class_correct = c

    def set_classifier_class_wrong(self, c):
        self.class_wrong = c

    def get_classifier_class_correct(self):
        return self.class_correct

    def get_classifier_class_wrong(self):
        return self.class_wrong