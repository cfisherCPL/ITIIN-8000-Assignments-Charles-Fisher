import matplotlib.pyplot as plt
from sklearn import datasets

# import some data to play with
iris = datasets.load_iris()
X = iris.data # [:, :2]  # this as something to do with what columns we want? Maybe?
# changing the above number does nothing to change WHAT column we use to plot
# can literally comment out the [] area and it doesnt change anything
y = iris.target

x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
# is this what we change to get different columns?
# nope. out of bounds error
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

plt.show()