from keras.datasets import imdb
from keras import models
from keras import layers
import numpy as np
from sklearn.metrics import recall_score, precision_score, f1_score
import matplotlib.pyplot as plt

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=1000)

def vectorize_sequences(sequences, dimension=1000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(1000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# Create a list to store the accuracy for each test set size
accuracies = []
precissions = []
recalls = []
f1_scores = []
step = int((len(x_test)*20)/100) # step 20%
test_range=range(1, len(x_test),step)
# Loop through different test set sizes
for i in test_range:
    model.fit(x_train, y_train, epochs=4, batch_size=512)

    results = model.evaluate(x_test[:i], y_test[:i])
    print("Accuracy:", results[1])

    y_pred = model.predict(x_test[:i])
    y_pred = (y_pred > 0.5).astype(int)

    recall = recall_score(y_test[:i], y_pred)
    precision = precision_score(y_test[:i], y_pred)
    f1 = f1_score(y_test[:i], y_pred)
    # Append the metrics to the list
    accuracies.append(results[1])
    precissions.append(precision)
    recalls.append(recall)
    f1_scores.append(f1)

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