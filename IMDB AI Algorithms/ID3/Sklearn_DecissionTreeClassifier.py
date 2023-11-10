
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score
import matplotlib.pyplot as plt
from keras.datasets import imdb
from sklearn.metrics import precision_score
import numpy as np
import tensorflow as tf

# load the dataset
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=1000)

word_index = tf.keras.datasets.imdb.get_word_index()
index2word = dict((i + 3, word) for (word, i) in word_index.items())
index2word[0] = '[pad]'
index2word[1] = '[bos]'
index2word[2] = '[oov]'
x_train = np.array([' '.join([index2word[idx] for idx in text]) for text in X_train])
x_test = np.array([' '.join([index2word[idx] for idx in text]) for text in X_test])

vocabulary = list()
for text in x_train:
  tokens = text.split()
  vocabulary.extend(tokens)

vocabulary = set(vocabulary)
print(len(vocabulary))

from tqdm import tqdm

x_train_binary = list()
x_test_binary = list()

for text in tqdm(x_train):
  tokens = text.split()
  binary_vector = list()
  for vocab_token in vocabulary:
    if vocab_token in tokens:
      binary_vector.append(1)
    else:
      binary_vector.append(0)
  x_train_binary.append(binary_vector)

x_train_binary = np.array(x_train_binary)

for text in tqdm(x_test):
  tokens = text.split()
  binary_vector = list()
  for vocab_token in vocabulary:
    if vocab_token in tokens:
      binary_vector.append(1)
    else:
      binary_vector.append(0)
  x_test_binary.append(binary_vector)

x_test_binary = np.array(x_test_binary)

dt = DecisionTreeClassifier(criterion='entropy')

# Create a list to store the accuracy for each test set size
accuracies = []
precissions = []
recalls = []
f1_scores = []
step = int((len(x_test_binary)*20)/100) # step 20%
test_range=range(1, len(x_test_binary),step)

# Loop through different test set sizes
for i in test_range:

    # Fit the classifier on the training set
    dt.fit(x_train_binary[:i], y_train[:i])

    # Make predictions on the test set
    y_pred = dt.predict(x_test_binary[:i])

    # Calculate metrics
    accuracy = accuracy_score(y_test[:i], y_pred)
    precission = precision_score(y_test[:i], y_pred)
    recall = recall_score(y_test[:i], y_pred)
    f1Score= f1_score(y_test[:i], y_pred)

    # Append the metrics to the list
    accuracies.append(accuracy)
    precissions.append(precission)
    recalls.append(recall)
    f1_scores.append(f1Score)

# Plot the metrics vs test set size
plt.plot(test_range, accuracies)
plt.xlabel('Test Set Size')
plt.ylabel('Accuracy')
plt.show()

plt.plot(test_range, precissions)
plt.xlabel('Test Set Size')
plt.ylabel('Precission')
plt.show()

plt.plot(test_range, recalls)
plt.xlabel('Test Set Size')
plt.ylabel('Recall')
plt.show()

plt.plot(test_range, f1_scores)
plt.xlabel('Test Set Size')
plt.ylabel('F1 Scores')
plt.show()


