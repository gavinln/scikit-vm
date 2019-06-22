---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
import numpy as np
```

Q01. Scikit-learn data sets

```python
from sklearn import datasets
iris = datasets.load_iris()
iris.data.shape
iris_X = iris.data
iris_y = iris.target

diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data
diabetes_y = diabetes.target

np.random.seed(0)
indices = np.random.permutation(len(iris_X))
```

Q02. KNN classifier

```python
from sklearn.neighbors import KNeighborsClassifier
X_train = iris_X[indices[:-10]]
y_train = iris_y[indices[:-10]]
X_test = iris_X[indices[-10:]]
y_test = iris_y[indices[-10:]]
# low n_neighbors - low bias/high variance
# high n_neighbors - high bias/low variance
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn.predict(X_test)
knn.score(X_test, y_test)  # accuracy
```

Q03. Logistic regression - classification algorithm

```python
from sklearn.linear_model import LogisticRegression
# C - inverse of regularization strength
# small C - large regularization
clf = LogisticRegression(
    solver='lbfgs', C=1e5, multi_class='multinomial')
clf.fit(X_train, y_train)
clf.score(X_test, y_test)  # accuracy
```


Q04. Support vector machine - linear kernel

```python
from sklearn import svm
# requires features to be normalized
# for a good prediction
# C - inverse of regularization strength
# small C - large regularization
svc = svm.SVC(C=1.0, kernel='linear')
svc.fit(X_train, y_train)
svc.score(X_test, y_test)  # accuracy
```

Q05. Support vector machine - non-linear kernel

```python
from sklearn import svm
# Classes that are not linearly separable
# Choose rbf - radial bases function
svc = svm.SVC(C=1.0, kernel='rbf')
svc.fit(X_train, y_train)
svc.score(X_test, y_test)  # accuracy
```

Q06. Linear regression

```python
from sklearn.linear_model import LinearRegression
X_train = diabetes_X[indices[:-20]]
y_train = diabetes_y[indices[:-20]]
X_test = diabetes_X[indices[-20:]]
y_test = diabetes_y[indices[-20:]]
regr = LinearRegression()
regr.fit(X_train, y_train)
mse = np.mean((regr.predict(X_test) - y_test) ** 2)
# coefficient of determination - R^2
# best 1.0, can be negative
# R^2 = (1 - u/v) u = ((y_true - y_pred) ** 2).sum()
# v = ((y_true - y_true.mean()) ** 2).sum()
regr.score(X_test, y_test)  # R^2
regr.coef_  # all coefficients non-zero
```

Q07. Ridge regression

```python
from sklearn.linear_model import Ridge
# high alpha, high bias/low variance
regr = Ridge(alpha=.1)
regr.fit(X_train, y_train)
mse = np.mean((regr.predict(X_test) - y_test) ** 2)
regr.score(X_test, y_test)  # R^2
regr.coef_  # all coefficients non-zero
```

Q08. Lasso regression

```python
from sklearn.linear_model import Lasso
# high alpha, high bias/low variance
regr = Lasso(alpha=.1)
regr.fit(X_train, y_train)
mse = np.mean((regr.predict(X_test) - y_test) ** 2)
regr.score(X_test, y_test)  # R^2
regr.coef_  # some coefficients zero
```

Q09. Cross validation

```python
from sklearn.model_selection import cross_val_score
k_fold = 3
svc = svm.SVC(C=1.0, kernel='linear')
cross_val_score(svc, iris_X, iris_y, cv=k_fold,
    scoring='accuracy')
```

Q10. Grid search

```python
from sklearn.model_selection import GridSearchCV
# 1e-6 1e-5 1e-4 1e-3 1e-2 1e-1
Cs = np.logspace(-6, -1, 6)
svc = svm.SVC(C=1.0, kernel='linear')
clf = GridSearchCV(
    estimator=svc, param_grid=dict(C=Cs))
clf.fit(iris_X, iris_y)
clf.best_score_, clf.best_estimator_.C
```

Q11. K-means clustering

```python
from sklearn import cluster
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(iris_X)
k_means.score(iris_X)
```

Q12. Principal component analysis

```python
# Create a signal with only 2 useful dimensions
x1 = np.random.normal(size=100)
x2 = np.random.normal(size=100)
X = np.c_[x1, x2, x1 + x2]

from sklearn import decomposition
pca = decomposition.PCA()
pca.fit(X)
print(pca.explained_variance_)
# Only the 2 first components are useful
pca.n_components = 2
X_reduced = pca.fit_transform(X)
X_reduced.shape
```
