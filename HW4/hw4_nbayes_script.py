# import the iris dataset from sklearn to do data stuff to it
# import train_test_split from sklearn to split our dataset
# import the naive bayes model from sklearn
# import metrics from sklearn to test accuracy
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

# load the iris dataset
iris = load_iris()
# put the features in an object called X
X = iris.data
# put the responses in an object called y
y = iris.target
# instantiate the classifier
gnb = GaussianNB()
# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# fit the model using the split training data
gnb.fit(X_train, y_train)
# feed the testing set into the GNB object
y_pred = gnb.predict(X_test)
# test the accuracy of the output of the test set vs the training set
print('Standard run at 20% test: ' + str(metrics.accuracy_score(y_test, y_pred)))
# use example as well
print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
print('Score function: ' + str(gnb.score(X_test,y_test)))


import random
print('Randomized Runs...')
for i in range(5):
    rnd_test = round(random.uniform(0.1,0.9),1)
    gnb2 = GaussianNB()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=rnd_test)
    gnb2.fit(X_train, y_train)
    y_pred = gnb2.predict(X_test)
    print(' TestSize: ' + str(rnd_test) + ' Accuracy: '
          + str(gnb.score(X_test,y_test)))