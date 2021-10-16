from math import ceil

import numpy as np


class Tree:
    def __init__(self, *, cls_inx=None, mod='tree', leaf=None):
        self.mod = mod
        if mod == 'tree':
            if cls_inx is None:
                raise ValueError(
                        'for tree mod must define cls_inx'
                        )
            self.cls_inx = cls_inx
            self.branches = {}
        self.leaf = leaf

    def __call__(self, x):
        if self.mod == 'leaf':
            return self.leaf
        try:
            return self.branches[x[self.cls_inx]](x)
        except KeyError:
            return self.leaf

    def __repr__(self):
        return self.mod


class CategoricalDecisionTree:
    def __init__(
            self,
            max_depth=None,
            min_samples_split=2,
            min_samples_leaf=1,
            ):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf

    def _prepare(self, X: np.ndarray, y_in: np.ndarray):
        self._n_samples, self.n_features = X.shape
        y = np.atleast_1d(y_in)
        if y.ndim == 1:
            y = np.reshape(y, (-1, 1))
        self.classes_, y_encoded = np.unique(y[:, 0], return_inverse=True)
        self.n_classes_ = self.classes_.shape[0]
        y = np.reshape(y_encoded, (-1, 1))

        # Check parameters
        if not 1 <= self.min_samples_leaf:
            raise ValueError(
                    "min_samples_leaf must be at least 1 or in (0, 0.5], got %s"
                    % self.min_samples_leaf
                    )
        self.min_samples_leaf = ceil(self.min_samples_leaf)

        if not 2 <= self.min_samples_split:
            raise ValueError(
                    "min_samples_split must be an integer "
                    "greater than 1 or a float in (0.0, 1.0]; "
                    "got the integer %s"
                    % self.min_samples_split
                    )
        self.min_samples_split = ceil(self.min_samples_split)
        self.min_samples_leaf = ceil(self.min_samples_leaf)
        self.max_depth = ceil(self.max_depth) if self.max_depth else np.iinfo(np.int32).max
        if len(y) != self._n_samples:
            raise ValueError(
                    "Number of labels=%d does not match number of samples=%d"
                    % (len(y), self._n_samples)
                    )
        if self.max_depth <= 0:
            raise ValueError("max_depth must be greater than zero. ")
        return y

    def fit(
            self, X: np.ndarray, y_in: np.ndarray,
            ):
        y = self._prepare(X, y_in)
        self._build(X, y)
        return self

    def _build(self, X: np.ndarray, y: np.ndarray):
        def entropy(labels: np.ndarray):
            counts = np.unique(labels, return_counts=True)[1]
            p = counts / counts.sum()
            return -p @ np.log2(p)

        def calc_ig(i: int, samples: np.ndarray, labels: np.ndarray):
            H0 = entropy(labels)
            cates = np.unique(samples[:, i])
            Hr = 0
            for cate in cates:
                Hr += entropy(labels[samples[:, i] == cate])
            return H0 - Hr, list(cates)

        def best_feature(samples: np.ndarray, labels: np.ndarray, features: set):
            feature_effect = [(*calc_ig(i, samples, labels), i) for i in features]
            return max(feature_effect)[1:]

        def find_tree(
                samples: np.ndarray, labels: np.ndarray, features: set, lvl=0,
                min_samples_split=self.min_samples_split, max_depth=self.max_depth,
                min_samples_leaf=self.min_samples_leaf
                ):
            categories, counts = np.unique(labels, return_counts=True)
            if categories.shape[0] == 1:
                return Tree(mod='leaf', leaf=categories[0])
            elif len(features) == 0 or len(labels) < min_samples_split or lvl >= max_depth:
                return Tree(mod='leaf', leaf=categories[counts.argmax()])
            cats, inx = best_feature(samples, labels, features)
            tree_ = Tree(cls_inx=inx, leaf=categories[counts.argmax()])
            for cat in cats:
                mask = samples[:, inx] == cat
                if mask.shape[0] > min_samples_leaf:
                    new_samples = samples[mask]
                    new_labels = labels[mask]
                    tree_.branches[cat] = find_tree(new_samples, new_labels, features - {inx}, lvl + 1)
            return tree_

        unused_feature = set(range(X.shape[1]))
        self.tree_ = find_tree(X, y, unused_feature)

    def predict(self, X: np.ndarray):
        rows, size = X.shape
        if size != self.n_features:
            raise ValueError(
                    "Number of input features=%d does not match number of trained features=%d"
                    % (X.shape[1], self.n_features)
                    )
        ans = np.zeros((rows, 1))
        for i in range(rows):
            ans[i] = self.classes_[self.tree_(X[i])]
        return ans


if __name__ == '__main__':
    X_mat = np.random.randint(0, 3, (400, 3))
    y_vec = X_mat.sum(axis=1)
    model = CategoricalDecisionTree(max_depth=3, min_samples_split=10, min_samples_leaf=4).fit(X_mat, y_vec)
    predict = model.predict(X_mat)
    print('train error', sum(a != b for a, b in zip(y_vec[:], predict[:])))
    X_mat = np.random.randint(0, 3, (40, 3))
    y_vec = X_mat.sum(axis=1)
    predict = model.predict(X_mat)
    print('test error', sum(a != b for a, b in zip(y_vec[:], predict[:])))
