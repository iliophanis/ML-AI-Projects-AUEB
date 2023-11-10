from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import numpy as np


class Evaluate:
    def __init__(self, predict, gold):
        self.predict = predict
        self.gold = gold

    def Precision(self):
        return precision_score(self.gold, self.predict)

    def Accuracy(self):
        return np.sum(np.equal(self.predict, self.gold)) / float(len(self.gold))

    def Recall(self):
        return recall_score(self.gold, self.predict)

    def F1(self):
        return 2 * (self.Precision() * self.Recall()) / (self.Precision() + self.Recall())
