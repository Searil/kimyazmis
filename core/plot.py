import numpy as np
import pylab as pl
import pickle

from matplotlib.colors import ListedColormap
from sklearn import neighbors, svm, datasets, tree, ensemble
from sklearn import linear_model, ensemble, naive_bayes

n_neighbors = 3

# import some data to play with
iris = datasets.load_iris()
# X = iris.data[:, :2]  # we only take the first two features. We could
#                       # avoid this ugly slicing by using a two-dim da

file_path_data = open("../trainer/PickledDataArrays/data.pkl")
x_arr = pickle.load(file_path_data)
file_path_data.close()

X = np.array(x_arr)
print len(X)

# y = iris.target
file_path_target = open("../trainer/PickledDataArrays/target.pkl")
y_arr = pickle.load(file_path_target)
file_path_target.close()

print y_arr

y = np.array(y_arr)

h = 1  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF',
                             '#CCCCFF', "#FFE261"])

cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF',
                            '#EEEEFF', "#DDA000"])

# we create an instance of Neighbours Classifier and fit the data.
# algo = neighbors.KNeighborsClassifier(n_neighbors, weights="uniform")
# algo = svm.SVC(kernel='linear').fit(X, y)
# algo = linear_model.LogisticRegression()
# algo = naive_bayes.GaussianNB()
# algo = tree.DecisionTreeClassifier()
algo = ensemble.GradientBoostingClassifier()

algo.fit(X, y)

# Plot the decision boundary. For that, we will asign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - 20, X[:, 0].max() + 20
y_min, y_max = X[:, 1].min() - 20, X[:, 1].max() + 20
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = algo.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
pl.figure()
pl.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
pl.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
pl.title("5-Class Classification with Gradient Boosting Classifier")
pl.axis('tight')

pl.show()
