"""
https://www.youtube.com/watch?v=0pP4EwWJgIU
"""
from sklearn.datasets import load_iris

iris = load_iris()
# notes and testing block commented out below
"""
# iris here is a dataype called BUNCH from sklearn
# each row is a OBSERVATION
# each column is a FEATURE
print(iris.feature_names)

# integers representing the species.
# these are the RESPONSES
print(iris.target)
# target represent what we are going to predict
print(iris.target_names)

# we're using classification here bc the supervised learning is CATEGORICAL
# finite unordered set
# so: we'll use CLASSIFICATION TECHNIQUES vs regression techs for solving and identifying from the data

# step one for doing this jazz: learn the relationship between the features and response!
# features and responses must be passed as separate objects : target and data do this
# these objects must be NUMERIC
# need to put them in a form that sklearn expects: NumPy arrays (ND Array?)
# these arrays need specific "shapes" --> these are the X and Y on your graph?
# data uses rows and columns, so the shape is 150 entries, and 4 features
# response is just SINGLE dimension, match the 1st from above, so 150 entries  --> the Z on a 3d graph then? (no!)
"""

# feature matrix in X, capitalized bc matrix
X = iris.data
# response vector in y, lowercase bc vector
y = iris.target

# so we've loaded the data and turned it into objects. Time to learn!

# step 1: import the kind of learning you want via class import
from sklearn.neighbors import KNeighborsClassifier

# step 2: instantiate the estimator! (estimator = "model")
knn = KNeighborsClassifier(n_neighbors=5)
# here we're setting the number of neighbors that matter for estimation to 1
# n_neighbors is a tuning param, or hyperparameter

# step 3: fit the model with data...aka TRAINING
# use the fit() method on knn object
knn.fit(X,y)

# final step is to make predictions for new observations
# use the predict() method on the knn object, and pass features as a python list in the params
# print(knn.predict([[3,5,4,2]]))
# can't tell if that prediction is correct or not bc the data is bs
# so, we use the data set itself to test our model!
y_pred = knn.predict(X)

# with sklearn, same 4 step process is used for all model types

# LET'S TRAIN AND TEST ACCURACY!
# first, import the metrics module
from sklearn import metrics
# then, use the accuracy score function, with params of true first, predicted second
print(metrics.accuracy_score(y, y_pred))

# look dawg, the onlything we did above is train a dataset to itself for PERFECT accuracy
# this would fail on out-of-sample data: noise versus signal concept
# train, test, split time

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)  #, random_state=4)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))