import numpy as np

class SimplePCA():
    def __init__(self, n_components=None):
        self.n_components = n_components
        
    def fit(self, X, y=None):
        self.means = X.mean(axis=0)
        x2 = X - self.means
        sigma = x2.T @ x2
        vecs, self.mags, *_ = np.linalg.svd(sigma)
        self.components_ = vecs[:, :self.n_components] if self.n_components else vecs
        return self
    
    def trasform(self, X, y=None):
        return X @ self.components_
    
    def reverse_transform(self,X,y=None):
        return X @ self.components_.T