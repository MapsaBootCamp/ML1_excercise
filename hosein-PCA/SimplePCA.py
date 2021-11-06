import numpy as np

class SimplePCA():
    def __init__(self, n_components=None, mode='eig'):
        self.n_components = n_components
        if mode in ('eig', 'svd'):
            self.mode = mode  # eig or svd
        else:
            raise Exception('دو حالت eig و svd قابل قبول است')
    def fit(self, X, y=None):
        self.means = X.mean(axis=0)
        x2 = X - self.means
        if self.mode == 'eig':
            sigma = x2.T @ x2
            eigs, eigs_vecs = np.linalg.eig(sigma)
            orders = np.argsort(eigs)[::-1]
            self.components_ = eigs_vecs[:,:self.n_components]
        else:
            *_, self.mags, vecs = np.linalg.svd(x2)
            self.components_ = vecs[:self.n_components, :].T if self.n_components else vecs.T
        return self
    
    def trasform(self, X, y=None):
        return X @ self.components_
    
    def reverse_transform(self,X,y=None):
        return X @ self.components_.T
