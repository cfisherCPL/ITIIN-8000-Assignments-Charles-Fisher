"""
# import the iris dataset from sklearn to do data stuff to it
# import train_test_split from sklearn to split our dataset
# import the MLP model from sklearn
# import metrics from sklearn to test accuracy
# import random to make random numbers for testing
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import random

# load the iris dataset
iris = load_iris()
# put the features in an object called X
X = iris.data
# put the responses in an object called y
y = iris.target
# instantiate the classifier
mlp = MLPClassifier(solver='lbfgs',
                    alpha=1e-5,
                    hidden_layer_sizes=(6,),
                    random_state=1)
# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify='yes', random_state=1)
# fit the model using the split training data
mlp.fit(X_train,y_train)
# feed the testing set into the MLP object
y_pred = mlp.predict(X_test)
# test the accuracy of the output of the test set vs the training set
print('Standard run at 20% test: ' + str(metrics.accuracy_score(y_test, y_pred)))


# create a loop to randomly split the data differently each time it passes, 5 times total

"""
# using the previously defined 4 step model didnt work with MLP
# let's try something else
# https://python-course.eu/neural_networks_with_scikit.php

from sklearn.datasets import load_iris
iris = load_iris()

import random
for i in range (5):
    rnd_test = round(random.uniform(0.1, 0.9), 1)
    # splitting into train and test datasets
    from sklearn.model_selection import train_test_split
    datasets = train_test_split(iris.data, iris.target, test_size=rnd_test)
    train_data, test_data, train_labels, test_labels = datasets

    # scaling the data
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()

    # we fit the train data
    scaler.fit(train_data)

    # scaling the train data
    train_data = scaler.transform(train_data)
    test_data = scaler.transform(test_data)

    # Training the Model
    from sklearn.neural_network import MLPClassifier
    # creating an classifier from the model:
    mlp = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=1000)

    # let's fit the training data to our model
    mlp.fit(train_data, train_labels)

    # testing accuracy
    from sklearn.metrics import accuracy_score

    predictions_train = mlp.predict(train_data)
    print('Results for '+ str(rnd_test) + ' sample size:')
    print('Train accuracy: ' + str(accuracy_score(predictions_train, train_labels)))
    predictions_test = mlp.predict(test_data)
    print('Test accuracy:  ' + str(accuracy_score(predictions_test, test_labels)))

"""
# past here it tests accuracy, but not sure of what the specs mean per se
# so, let's just hide it for the assignment, even if it's useful
from sklearn.metrics import confusion_matrix

confusion_matrix(predictions_train, train_labels)
confusion_matrix(predictions_test, test_labels)

from sklearn.metrics import classification_report

print(classification_report(predictions_test, test_labels))
"""