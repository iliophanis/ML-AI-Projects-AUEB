from IMDB import *
from NaiveBayes import *

imdb_dir="IMDB_DataSet"

print("Reading Training Data")
trainFilePath = os.path.join(imdb_dir, "train")
train_data = IMDB(trainFilePath)

print("Reading Test Data")
testFilePath=os.path.join(imdb_dir, "test")
test_data = IMDB(testFilePath, vocabulary=train_data.vocabulary)

print("Calculating for 0.01")
nb = NaiveBayes(train_data, 0.01)
print("Evaluating")
nb.Assess(test_data)
nb.predict_probability(test_data, range(10))
nb.Attibutes()