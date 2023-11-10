import math

class Utility:

    def __init__(self):
        pass

    def get_best_attribute(self, total_entropy, instancesarr, attribute_list, output_values):
        best_attribute = attribute_list[0]
        max_gain = self.get_information_gain(total_entropy, attribute_list, instancesarr, output_values)
        size = len(attribute_list) - 1
        i = 0
        while i < size:
            f = attribute_list[i]
            gain = self.get_information_gain(total_entropy, f, instancesarr, output_values)
            if gain > max_gain:
                max_gain = gain
                best_attribute = f
            i = i + 1

        return best_attribute

    def get_total_entropy(self, instancesarr):
        category_nums = []
        total_entropy = 0.0

        i = 0
        while i < len(instancesarr):
            category = 0.0
            for e in instancesarr:
                print(e.get_classification())
                print(e.instancearr[i])
                if e.classification == e.instancearr[i]:
                    category = category + 1
            term = category / len(instancesarr)
            category_nums.append(term)
            i = i + 1

        i = 0
        while i < len(category_nums):
            clas = category_nums[i]
            if clas == 0:
                total_entropy = total_entropy + 0
            else:
                total_entropy = total_entropy - clas * (math.log(clas) / math.log(2))
            i = i + 1

        return total_entropy

    # Returns Information Gain of an attribute
    def get_information_gain(self, total_entropy, attr_f, instancesarr, words):
        entropy = 0.0
        for val in attr_f.get_possible_values():
            # if the instance has this attribute value, count the number of each classification
            i = 0
            while i < len(words):
                a = 0
                num_of_instances = 0
                for e in instancesarr:
                    if e.valuesList[attr_f.get_index()] == val:
                        num_of_instances = num_of_instances + 1
                        if e.get_classification().lower() == words[i]:
                            a = a + 1

                aFraction = a / num_of_instances
                if aFraction == 0.0:
                    entropy = entropy + 0.0
                else:
                    entropy = entropy - aFraction * (math.log(aFraction) / math.log(2))

                i = i + 1   # end while loop

        return total_entropy - entropy

    def recall(self, tree, test, words):
        s = len(words)
        index1 = 0
        index2 = 0

        # generate a 2 dimensional matrix of size s x s filled with 0
        resolution = [[0 for i in range(s)] for i in range(s)]

        for e in test:
            result = tree.classify(e, words)
            if result == 1.0:
                c = tree.get_classifier_class_correct()
                i = 0
                while i < s:
                    if words[i] == c:
                        index1 = i
                        break
                    i = i + 1
                resolution[index1][index2] = resolution[index1][index2]+1
            elif result == 0.0:
                c = tree.get_classifier_class_correct()
                w = tree.get_classifier_class_wrong()
                i = 0
                while i < s:
                    if words[i] == c:
                        index1 = i
                    if words[i] == w:
                        index2 = i
                    i = i+1
                resolution[index1][index2] = resolution[index1][index2]+1
        return resolution

    def take_classification(instance_list, outpt):
        s = len(outpt)
        classification = []
        for i in range(s):
            classification.append(0)

        j = 0
        while j < s:
            for ex in instance_list:
                if ex.classification.lower() == outpt[j].lower():
                    classification[j] = classification[j] + 1
            j = j + 1
        return classification

