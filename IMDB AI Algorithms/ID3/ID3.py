from tensorflow import keras
from keras.datasets import imdb
import matplotlib.pyplot as plt

from Node import *
from DecisionTree import *
from Utility import *


class ID3:
    Attributes = []
    x_train = []
    testInstances = []
    instances1 = []
    instances2 = []
    instances3 = []
    instances4 = []
    numbering = 0
    outputIndex = 0
    outputValues = []

    def __init__(self):
        pass

    def run_id3(self):
        (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=4000)

        # Retrieve the word index file mapping words to indices
        word_index = keras.datasets.imdb.get_word_index()
        #Create set with 20% of the training set
        i = 0
        while i < math.floor(len(y_train) * 0.2):
            self.instances1.append(y_train[i])
            i = i + 1

        # Create set with 40% of the training
        i = 0
        while i < math.floor(len(y_train) * 0.4):
            self.instances2.append(y_train[i])
            i = i + 1

        # Create set with 60% of the training set
        i = 0
        while i < math.floor(len(y_train) * 0.6):
            self.instances3.append(y_train[i])
            i = i + 1

        # Create set with 80% of the training set
        i = 0
        while i < math.floor(len(y_train) * 0.8):
            self.instances4.append(y_train[i])
            i = i + 1

        # Create tree that fits the 20% of training' sets
        train_size=math.floor(len(y_train) * 0.2)
        tree = self.id3(self.instances1, x_train[:train_size])

        sum = 0.0
        # Calculate score of tree
        for e in self.instances1:
            sum = sum + tree.classify(e, word_index.keys())

        # Set initial best score and best tree
        print("Size of 20% of train sets: ", str(len(self.instances1)))
        score_of_best_tree = (sum / len(self.instances1)) * 100.0
        error = 100.0 - score_of_best_tree
        print("score of train of 20% of Instances: ", str(score_of_best_tree))
        print("error of train of 20% of Instances: ", str(error))
        print("-----------------------------------------------------------\n")

        # Create tree that fits the 40% of training' sets
        train_size=math.floor(len(y_train) * 0.4)
        tree2 = self.id3(self.instances2, x_train[:i])

        # Calculate score of tree
        sum = 0.0
        for e in self.instances2:
            sum = sum + tree2.classify(e, word_index.keys())

        # Set initial best score and best tree
        print("Size of 40% of train sets: ", len(self.instances2))
        score_of_best_tree2 = (sum / len(self.instances2)) * 100.0
        error2 = 100.0 - score_of_best_tree2
        print("score of train of 40% of Instances: ", score_of_best_tree2)
        print("error of train of 40% of Instances: ", error2)
        print("-----------------------------------------------------------~\n")

        # Create tree that fits the 60% of training' sets
        train_size=math.floor(len(y_train) * 0.6)
        tree3 = self.id3(self.instances3, x_train[:train_size])

        sum = 0.0
        # Calculate score of tree
        for e in self.instances3:
            sum = sum + tree3.classify(e, word_index.keys())

        # Set initial best score and best tree
        print("Size of 60% of train sets: ", len(self.instances3))
        score_of_best_tree3 = (sum / len(self.instances3)) * 100.0
        error3 = 100.0 - score_of_best_tree3
        print("score of train of 60% of Instances: ", score_of_best_tree3)
        print("error of train of 60% of Instances: ", error3)
        print("-----------------------------------------------------------~\n")

        # Create tree that fits the 80% of training' sets
        train_size=math.floor(len(y_train) * 0.8)
        tree4 = self.id3(self.instances4, x_train[:train_size])

        sum = 0
        # Calculate score of tree on the tuning set
        for e in self.instances4:
            sum += tree4.classify(e, word_index.keys())

        # Set initial best score and best tree
        print("Size of 80% of train sets: ", len(self.instances4))
        score_of_best_tree4 = (sum / len(self.instances4)) * 100.0
        error4 = 100 - score_of_best_tree4
        print("score of train of 80% of Instances: ", score_of_best_tree4)
        print("error of train of 80% of Instances: ", error4)
        print("-----------------------------------------------------------~\n")

        #Create tree that fits 100% of training sets
        tree5 = self.id3(y_train, x_train)

        # calculate score of tree in the tuning set
        sum = 0
        for e in y_train:
            sum = sum + tree5.classify(e, word_index.keys())
        print("total_mismatch:",sum)
        # set initial best score and best tree
        print("Size of 100% of train sets: ", len(y_train))
        score_of_best_tree5 = (sum / len(y_train)) * 100.0
        error5 = 100 - score_of_best_tree5
        print("score of train of 100% of Instances: ", score_of_best_tree5)
        print("error of train of 100% of Instances: ", error5)
        print("****************************************************\n")


        data = [len(self.instances1), len(self.instances2), len(self.instances3), len(self.instances4),
                len(x_train)]
        score = [score_of_best_tree, score_of_best_tree2, score_of_best_tree3, score_of_best_tree4, score_of_best_tree5]

        plt.plot(data, score)
        plt.show()

        total = 0.0
        for e in self.testInstances:
            total = total + tree5.classify(e, word_index.keys())

        accuracy_of_test = (total / len(y_test)) * 100.0
        error_of_test = 100.0 - accuracy_of_test
        print("-----------------------------------------------------------~\n")
        print("Accuracy of DT learner: ", accuracy_of_test, "%")
        print("Error of DT learner: ", error_of_test, "%")
        print("-----------------------------------------------------------~\n")

        res = Utility().recall(tree5, y_test, word_index.keys())
        cla = Utility().take_classification(y_test)

        i = 0
        while i < len(res):
            if not cla[i] == 0:
                precision = float(res[i][i]) / float(cla[i])

            recall = 0.0
            column = 0
            j = 0
            while j < len(res):
                column = column + res[j][i]
                j = j + 1
            if not column == 0:
                recall = res[i][j] / column
            else:
                recall = 0.0
            print("Recall of ", word_index[i].keys(), " : ", recall)
            i = i + 1

    def id3(self, instances, attributes):
        word_index = keras.datasets.imdb.get_word_index()

        self.numbering = self.numbering + 1
        new_attribute_list = []

        root = Node(attributes, instances, self.numbering)

        tree = DecisionTree(root)

        # If the root node contains all the same classifications,
        # return the single tree node with the corresponding classification
        if root.is_leaf:
            return tree
        elif not len(instances) == 0:
            tree.root.set_classification()
            print(tree.root.get_classification())
            return tree
        else:  # Otherwise begin the algorithm to search for a DecisionTree
            total_entropy = Utility().get_total_entropy(attributes)
            best_attribute = Utility().get_best_attribute(total_entropy, instances, attributes, word_index.keys())
            root.set_attribute(best_attribute)

        k = best_attribute.getIndex()

        for val in best_attribute.get_possible_values():
            new_instance_list = []
            for e in instances:
                if e.get_values[k].equalsIgnoreCase(val):
                    new_instance_list.append(e)

            child = DecisionTree(Node(new_instance_list, word_index.keys(), self.numbering))

            child.get_root_node().set_attribute_value(val)

            if not child.get_root_node().is_leaf():
                new_attribute_list.remove(best_attribute)
                child.add_tree(self.id3(new_instance_list, new_instance_list))
            else:
                child.get_root_node().self_classification(child.get_root_node().get_majority_classification())
                tree.add_tree(child)

        return tree