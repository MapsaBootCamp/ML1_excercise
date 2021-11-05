# Principal Component Analysis (PCA)
import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None
        self.explained_variance_=None
        self.explained_variance_ratio_=None

    def fit(self, X):
        # calculate mean
        self.mean = np.mean(X, axis=0)
        X = X - self.mean

        # calculate covariance matrix
        cov = np.cov(X.T)

        # calculate eigenvectors and eigenvalues
        eigenvalues, eigenvectors = np.linalg.eig(cov)
        print('*'*10+' eigenvalues '+'*'*10)
        print(eigenvalues)
        print('*'*10+' eigenvectors '+'*'*10)
        print(eigenvectors)

        # sort eigenvectors
        idxs = np.argsort(eigenvalues)[::-1]
        sorted_eigenvalues = eigenvalues[idxs]
        sorted_eigenvectors = eigenvectors[:, idxs]

        # store first n eigenvectors
        self.components = sorted_eigenvectors[:, 0:self.n_components]
        print('-'*10+' components '+'-'*10)
        print(self.components)
        self.explained_variance_ = sorted_eigenvalues[:self.n_components]
        self.explained_variance_ratio_=[(num/np.sum(sorted_eigenvalues)) for num in sorted_eigenvalues[:self.n_components]]

    def transform(self, X):
        X_mean = X - self.mean
        X_reduced = np.dot(self.components.T, X_mean.T).T
        return X_reduced
