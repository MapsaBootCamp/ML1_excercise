import numpy as np
import pandas as pd
# from sklearn.decomposition import PCA
from sklearn.naive_bayes import ComplementNB,GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import   classification_report



df = pd.read_csv(r"C:\Users\mehdi\Downloads\Iris.csv")
df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
df.dropna(how="all", inplace=True)

X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

X_std = StandardScaler().fit_transform(X)


class PCA_khodam:
    def __init__(self, n_comp):
        self.n_comp = n_comp

    def fit(self, X_std):
        self.X_std = X_std
        cov_mat = np.cov(X_std.T)

        eig_vals, eig_vecs = np.linalg.eig(cov_mat)
        eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]

        eig_pairs.sort()
        eig_pairs.reverse()
        n_c = self.n_comp
        n_f = X_std.shape[1]
        xx = []
        for i in range(n_c):
            matrix = np.hstack(eig_pairs[i][1].reshape(n_f, 1))
            xx.append(matrix)

        matrix_w = np.array(xx).T

        nex_x = X_std.dot(matrix_w)
        return nex_x



x_pca=PCA_khodam(2)

xx=x_pca.fit(X_std)
X_train, X_test, y_train, y_test = train_test_split(xx, y, test_size=0.3, random_state=42)

nb_classifier = GaussianNB()

nb_classifier.fit(X_train,y_train)

y_prediction = nb_classifier.predict(X_test)
print(classification_report(y_test,y_prediction))