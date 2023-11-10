from collections import Counter
from scipy.sparse import csr_matrix
import os
import numpy as np
from Vocabulary import *

np.random.seed(1)

class IMDB:
    def __init__(self, directory, vocabulary=None):
        neg_files = os.listdir("%s/neg" % directory)
        pos_files = os.listdir("%s/pos" % directory)
        if not vocabulary:
            self.vocabulary = Vocabulary()
        else:
            self.vocabulary = vocabulary
        X_values = []
        self.X_reviews = []
        Y = []
        X_col_list = []
        X_row_list = []

        for j in range(len(neg_files)):     # process neg files
            file = neg_files[j]
            lines = ""
            for line in open("%s/neg/%s" % (directory, file), encoding="utf8"):
                lines = lines + line
                word_counter = Counter([self.vocabulary.get_id(word.lower()) for word in line.split(" ")])
                for (word_id, count) in word_counter.items():
                    if word_id >= 0:
                        X_values.append(count)
                        X_row_list.append(len(pos_files) + j)
                        X_col_list.append(word_id)
            Y.append(-1.0)
            self.X_reviews.append(lines)

        for i in range(len(pos_files)):     # process positive files
            lines = ""
            file = pos_files[i]
            for line in open("%s/pos/%s" % (directory, file), encoding="utf8"):
                lines = lines + line
                word_counter = Counter([self.vocabulary.get_id(w.lower()) for w in line.split(" ")])
                for (word_id, count) in word_counter.items():
                    if word_id >= 0:
                        X_values.append(count)
                        X_row_list.append(i)
                        X_col_list.append(word_id)
            Y.append(+1.0)
            self.X_reviews.append(lines)

        self.vocabulary.lock()
        self.X = csr_matrix((X_values, (X_row_list, X_col_list)), shape=(max(X_row_list)+1, self.vocabulary.get_size_vocabulary()))
        self.Y = np.asarray(Y)

        idx = np.arange(self.X.shape[0])
        np.random.shuffle(idx)
        self.X = self.X[idx, :]
        self.Y = self.Y[idx]


