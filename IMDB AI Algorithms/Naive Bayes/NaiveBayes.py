import sys
from scipy.sparse import csr_matrix
import numpy as np
from Evaluate import Evaluate
from math import log, exp
import matplotlib.pyplot as plt

class NaiveBayes:
    def __init__(self, data, ALPHA=0.1):
        self.ALPHA = ALPHA
        self.data = data  # training data
        # TODO: Initalize parameters - Random initialization
        self.P_pos = 1.0
        self.P_neg = 1.0
        self.count_pos = np.array([])
        self.count_neg = np.array([])
        self.deno_pos = 1
        self.deno_neg = 1
        self.num_pos_reviews = 1
        self.num_neg_reviews = 1
        self.total_pos_words = 1
        self.total_neg_words = 1
        self.pos_words = []
        self.neg_words = []
        self.vocab_len = 1
        self.Train(data.X, data.Y)

    # Train model - X are instances, Y are labels (+1 or -1)
    # X and Y are sparse matrices
    def Train(self, X, Y):
        # TODO: Estimate Naive Bayes model parameters
        # calculate frequency parameters to be used in PredictLabel to calculate probabilities
        pos_arr = np.argwhere(Y == 1.0).flatten()
        neg_arr = np.argwhere(Y == -1.0).flatten()
        self.count_pos = np.zeros(X.shape[1])
        self.count_neg = np.zeros(X.shape[1])
        self.num_pos_reviews = sum([1 if i == 1 else 0 for i in Y])
        self.num_neg_reviews = sum([1 if i == -1 else 0 for i in Y])
        self.total_pos_words = np.sum(X[pos_arr, :])
        self.total_neg_words = np.sum(X[neg_arr, :])
        self.deno_pos = self.total_pos_words + self.ALPHA * X.shape[1]
        self.deno_neg = self.total_neg_words + self.ALPHA * X.shape[1]

        rows, columns = X.nonzero()
        for i, j in zip(rows, columns):
            if self.data.Y[i] == 1:
                self.count_pos[j] += X[i, j]
            else:
                self.count_neg[j] += X[i, j]
        self.count_pos = (self.count_pos + self.ALPHA)
        self.count_neg = (self.count_neg + self.ALPHA)
        # above 2 arrays give total frequencies for each word in each class
        return

    # predict the labels, return sparse matrix Y with predicted labels (+1 or -1)
    def PredictLabel(self, X, threshold=0.5):
        # TODO: Implement Naive Bayes Classification
        # Calculate P(W|C) and P(C) to get P(C|W) using a logsum
        self.P_pos = log(self.num_pos_reviews) - (log(self.num_pos_reviews) + log(self.num_neg_reviews))
        self.P_neg = log(self.num_neg_reviews) - (log(self.num_pos_reviews) + log(self.num_neg_reviews))
        pred_labels = []
        w = X.shape[1]
        sh = X.shape[0]
        for i in range(sh):
            # checks if the value of the data is zero or not if not then proceed
            z = X[i].nonzero()
            positive_sum = self.P_pos
            negative_sum = self.P_neg
            for j in range(len(z[0])):
                row_idx = i
                col_idx = z[1][j]
                occurrence = X[row_idx, col_idx]
                P_pos = log(self.count_pos[col_idx]) - log(self.deno_pos)
                positive_sum = positive_sum + occurrence * P_pos
                P_neg = log(self.count_neg[col_idx]) - log(self.deno_neg)
                negative_sum = negative_sum + occurrence * P_neg
            probValue = exp(positive_sum - self.log_sum(positive_sum, negative_sum))
            if probValue > threshold:  # Predict positive
                pred_labels.append(1.0)
            else:  # Predict negative
                pred_labels.append(-1.0)

        return pred_labels

    # avoid numerical underflow/overflow, return log(x+y)
    def log_sum(self, logx, logy):
        m = max(logx, logy)
        return m + log(exp(logx - m) + exp(logy - m))

    # predict probability of each review being positive
    def predict_probability(self, test, indexes):
        for i in indexes:
            # using logsum
            predicted_label = 0
            z = test.X[i].nonzero()
            positive_sum = self.P_pos
            negative_sum = self.P_neg

            for j in range(len(z[0])):
                row_idx = i
                col_idx = z[1][j]
                occurrence = test.X[row_idx, col_idx]
                P_pos = log(self.count_pos[col_idx])
                positive_sum = positive_sum + occurrence * P_pos
                P_neg = log(self.count_neg[col_idx])
                negative_sum = negative_sum + occurrence * P_neg

            if positive_sum > negative_sum:
                predicted_label = 1.0
            else:
                predicted_label = -1.0
            print(test.Y[i], test.X_reviews[i], predicted_label)

    # calculates precision, recall and accuracy for the different values of a threshold
    # assess performance on test data
    # give top 20 positive and negative words based on their log odds
    def Attibutes(self):
        neg_pos_sub = np.zeros(self.data.X.shape[1])
        neg_diff = np.zeros(self.data.X.shape[1])
        for j in range(len(self.count_pos)):
            P_neg = log(self.count_neg[j]) - log(self.deno_neg)
            P_pos = log(self.count_pos[j]) - log(self.deno_pos)
            neg_pos_sub[j] = (P_pos - P_neg)
            # neg_diff[j]=(P_neg-P_pos)*(self.count_neg[j]-self.count_pos[j])

        print("The top 20 negative words along with their weights:")
        neg_index = neg_pos_sub.argsort()[:20]
        for j in neg_index:
            print("j:", self.data.vocabulary.get_word(j), " ", neg_pos_sub[j])

        print("The top 20 positive words along with their weights:")
        pos_index = neg_pos_sub.argsort()[-20:][::-1]
        for j in pos_index:
            print("j:", self.data.vocabulary.get_word(j), " ", neg_pos_sub[j])

    def Assess(self, test):
        # Create a list to store the accuracy for each test set size
        accuracies_pos = []
        precissions_pos = []
        recalls_pos = []
        f1_scores_pos = []
        accuracies_neg = []
        precissions_neg = []
        recalls_neg = []
        f1_scores_neg = []
        step = int((test.X.shape[0]*20)/100) # step 20%
        test_range=range(1, test.X.shape[0],step)
        # Loop through different test set sizes
        for z in test_range:
            Y_predict = self.PredictLabel(test.X[:z])
            eval = Evaluate(Y_predict, test.Y[:z])
            ev_neg = Evaluate([1 if i == -1 else -1 for i in Y_predict], [1 if i == -1 else -1 for i in test.Y[:z]])

            # Append the metrics to the list
            accuracies_pos.append(eval.Accuracy())
            precissions_pos.append(eval.Precision())
            recalls_pos.append(eval.Recall())
            f1_scores_pos.append(eval.F1())
            
            # Append the metrics to the list
            accuracies_neg.append(ev_neg.Accuracy())
            precissions_neg.append(ev_neg.Precision())
            recalls_neg.append(ev_neg.Recall())
            f1_scores_neg.append(ev_neg.F1())

        # Plot the metrics vs test set size
        plt.plot(test_range, accuracies_pos)
        plt.xlabel('Test Set Size')
        plt.ylabel('Accuracy')
        plt.show()

        plt.plot(test_range, precissions_pos)
        plt.xlabel('Test Set Size')
        plt.ylabel('Precission')
        plt.show()

        plt.plot(test_range, recalls_pos)
        plt.xlabel('Test Set Size')
        plt.ylabel('Recall')
        plt.show()

        plt.plot(test_range, f1_scores_pos)
        plt.xlabel('Test Set Size')
        plt.ylabel('F1 Scores')
        plt.show()

        # Plot the metrics vs test set size
        plt.plot(test_range, accuracies_neg)
        plt.xlabel('Test Set Size')
        plt.ylabel('Accuracy')
        plt.show()

        plt.plot(test_range, precissions_neg)
        plt.xlabel('Test Set Size')
        plt.ylabel('Precission')
        plt.show()

        plt.plot(test_range, recalls_neg)
        plt.xlabel('Test Set Size')
        plt.ylabel('Recall')
        plt.show()

        plt.plot(test_range, f1_scores_neg)
        plt.xlabel('Test Set Size')
        plt.ylabel('F1 Scores')
        plt.show()
