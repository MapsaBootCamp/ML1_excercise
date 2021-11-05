from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pca
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import decomposition
import numpy as np


data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

# reduced data by my pca
my_pca = pca.PCA(n_components=2)
my_pca.fit(X_train)
X_train_my_pca = my_pca.transform(X_train)
X_test_my_pca = my_pca.transform(X_test)
print('my explained_variance_: \n', my_pca.explained_variance_)
print('sum of my explained_variance_ratio_: \n', np.sum(my_pca.explained_variance_ratio_[:2]))

svc_clf_1 = SVC()
svc_clf_1.fit(X_train_my_pca, y_train)
y_pred_1 = svc_clf_1.predict(X_test_my_pca)
print(' My PCA: ')
print(classification_report(y_test, y_pred_1))

# reduced data by pca sklearn
sk_pca = decomposition.PCA(n_components=2)
sk_pca.fit(X_train)
X_train_sk_pca = sk_pca.transform(X_train)
X_test_sk_pca = sk_pca.transform(X_test)
print('scikit learn explained_variance_: \n', sk_pca.explained_variance_)
print('sum of scikit learn explained_variance_ratio_: \n', np.sum(sk_pca.explained_variance_ratio_))

svc_clf_2 = SVC()
svc_clf_2.fit(X_train_sk_pca, y_train)
y_pred_2 = svc_clf_2.predict(X_test_sk_pca)
print(' scikit learn PCA: ')
print(classification_report(y_test, y_pred_2))

# plot reduced data by my pca
X_train_reduced = pd.DataFrame(X_train_my_pca , columns = ['PC1','PC2'])
data_train = pd.concat([X_train_reduced ,pd.DataFrame(y_train, columns = ['target'])] , axis = 1)

plt.figure(figsize=(8,8))
plt.title('My PCA')
sns.scatterplot(data = data_train , x = 'PC1',y = 'PC2' , hue = 'target')
plt.show()
