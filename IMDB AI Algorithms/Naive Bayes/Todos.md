* Change prediction and accuracy based per test data to show the accuracy changes [] 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# load the dataset
X, y = #...

# split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the classifier
clf = DecisionTreeClassifier()

# Create a list to store the accuracy for each test set size
accuracies = []

# Loop through different test set sizes
for i in range(1, len(X_test)):

    # Fit the classifier on the training set
    clf.fit(X_train[:i], y_train[:i])

    # Make predictions on the test set
    y_pred = clf.predict(X_test[:i])

    # Calculate the accuracy
    accuracy = accuracy_score(y_test[:i], y_pred)

    # Append the accuracy to the list
    accuracies.append(accuracy)

# Plot the accuracy vs test set size
plt.plot(range(1, len(X_test)), accuracies)
plt.xlabel('Test Set Size')
plt.ylabel('Accuracy')
plt.show()

