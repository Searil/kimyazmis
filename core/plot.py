import numpy as np
import pylab as pl
from matplotlib.colors import ListedColormap
from sklearn import neighbors, svm, datasets

n_neighbors = 15

# import some data to play with
iris = datasets.load_iris()
# X = iris.data[:, :2]  # we only take the first two features. We could
#                       # avoid this ugly slicing by using a two-dim da


x_arr = [
    [19.677, 89.952],
    [30.000, 69.615],
    [25.391, 82.100],
    [22.806, 52.954],
    [25.942, 59.226],
    [21.723, 73.858],
    [25.739, 64.793],
    [28.478, 56.344],
    [25.514, 60.523],
    [28.350, 74.895],
    [25.557, 80.324],
    [20.744, 65.894],
    [28.670, 51.483],
    [23.694, 51.720],
    [22.546, 60.014],
    [7.1174, 81.576],
    [31.828, 60.010],
    [29.910, 69.558],
    [28.236, 59.147],
    [34.052, 92.870],
    [21.634, 63.043],
    [21.178, 55.478],
    [33.220, 84.690],
    [23.742, 62.978],
    [27.705, 63.021],
    [17.217, 47.580],
    [27.915, 61.298],
    [15.857, 37.000],
    [22.168, 58.554],
    [21.897, 139.87],
    [26.080, 84.315],
    [26.431, 56.757],
    [32.485, 76.651],
    [25.467, 68.543],
    [30.469, 65.626],
    [54.250, 139.50],
    [11.465, 21.451],
    [33.911, 96.083],
    [30.031, 118.87],
    [27.306, 81.117],
    [29.691, 80.277],
    [30.086, 62.321],
    [34.530, 110.23],
    [43.129, 145.56],
    [24.125, 57.900],
    [31.507, 67.937],
    [31.041, 111.51],
    [36.000, 110.40],
    [7.9523, 20.875],
    [20.780, 38.727],
    [23.859, 50.370],
    [31.103, 69.384],
    [37.571, 144.65],
    [18.040, 44.918],
    [10.788, 28.370],
    [20.988, 46.947],
    [17.242, 44.703],
    [30.181, 109.40],
    [12.303, 24.886],
    [36.904, 141.78],
    [32.081, 98.250],
    [15.266, 33.925],
    [18.402, 47.027],
    [17.772, 40.448],
    [29.921, 72.666],
    [25.067, 62.145],
    [21.123, 48.885],
    [28.523, 149.75],
    [14.810, 33.212],
    [14.222, 32.000],
    [60.621, 407.81],
    [54.677, 258.08],
    [48.304, 222.20],
    [44.397, 217.55],
    [47.907, 279.45],
    [43.293, 386.30],
    [58.215, 365.92],
    [59.863, 379.13],
    [48.333, 341.78],
    [65.000, 433.33],
    [57.921, 338.61],
    [52.061, 252.59],
    [54.537, 396.63],
    [47.821, 446.33],
    [46.676, 256.72],
    [49.752, 414.60],
    [44.443, 359.25],
    [40.491, 412.27],
    [58.337, 392.45],
    [51.095, 266.83],
    [40.603, 237.21],
    [56.892, 352.73],
    [49.416, 395.33],
    [60.606, 333.33],
    [55.983, 223.93],
    [48.148, 261.11],
    [56.645, 223.75],
    [52.094, 449.31],
    [50.254, 409.76],
    [74.394, 310.70],
    [49.676, 378.30],
    [59.445, 387.80],
    [65.544, 345.20],
    [44.563, 403.42],
    [60.810, 400.33]
]


X = np.array(x_arr)
print X
print len(X)

# y = iris.target
y_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2]

y = np.array(y_arr)

h = 1  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# we create an instance of Neighbours Classifier and fit the data.
# clf = neighbors.KNeighborsClassifier(n_neighbors, weights="uniform")
# clf.fit(X, y)
svc = svm.SVC(kernel='linear').fit(X, y)

# Plot the decision boundary. For that, we will asign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - 20, X[:, 0].max() + 20
y_min, y_max = X[:, 1].min() - 20, X[:, 1].max() + 20
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
pl.figure()
pl.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
pl.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
pl.title("3-Class classification (k = %i, weights = '%s')"
         % (n_neighbors, "uniform"))
pl.axis('tight')

pl.show()
