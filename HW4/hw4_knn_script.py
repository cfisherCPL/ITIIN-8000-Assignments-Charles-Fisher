# import the iris dataset from sklearn to do data stuff to it
# import the knn classifier to be used for classification of data
# import train_test_split from sklearn to split our dataset
# import metrics from sklearn to test accuracy
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# load the iris dataset
iris = load_iris()
# put the features in an object called X
X = iris.data
# put the responses in an object called y
y = iris.target
# instantiate the classifier with a K value
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# fit the model using the split training data
knn.fit(X_train, y_train)
# feed the testing set into the knn object
y_pred = knn.predict(X_test)
# test the accuracy of the output of the test set vs the training set
print('Standard run K=5 and 20% test: ' + str(metrics.accuracy_score(y_test, y_pred)))

import random
print('Randomized Runs...')

for i in range(5):
    rnd_K = random.randint(1,9)
    rnd_test = round(random.uniform(0.1,0.9),1)
    knn2 = KNeighborsClassifier(n_neighbors=rnd_K, weights='distance')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=rnd_test)
    knn2.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print('K: '+ str(rnd_K) +' ' + ' TestSize: ' + str(rnd_test) + ' Accuracy: '
          + str(metrics.accuracy_score(y_test, y_pred)))


