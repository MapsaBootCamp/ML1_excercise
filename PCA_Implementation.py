import numpy as np


class PCA:

    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        # mean
        self.mean = np.mean(X, axis=0)
        X = X - self.mean
        
        # covariance
        cov = np.cov(X.T)
        
        # eignenvectors, eigenvalues
        eigenvalues, eigenvecotrs = np.linalg.eig(cov)
        # v[:, i]

        # sort eigenvectors
        eigenvalues = eigenvalues.T
        idxs = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idxs]
        eigenvecotrs = eigenvecotrs[idxs]
        
        # sort first n eigenvectors
        self.components = eigenvecotrs[0:self.n_components] 

    def transform(self, X):
        # project data
        X = X - self.mean
        return np.dot(X, self.components.T)  