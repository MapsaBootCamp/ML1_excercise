import numpy as np
from sklearn.datasets import load_iris
from sklearn.utils import shuffle
from scipy.special import softmax
from sklearn.model_selection import train_test_split


class LogesticRegression:

    def __init__(self, X_train, Y_train):
        X0 = np.ones((X_train.shape[0],1))
        self.X = np.append(X_train, X0, axis=1).T
        self.m = X_train.shape[1]  # features
        self.n = X_train.shape[0]  # sample size
        self.Y = np.array(Y_train)  # train lable
        self.Y = self.Y.reshape(-1, 1)
        self.classes = np.unique(self.Y)
        self.Y_onehot = np.zeros((self.n, len(self.classes)))
        for i in range(self.n):
            self.Y_onehot[i, Y_train[i]] = 1
        self.W = np.zeros((self.m+1, len(self.classes)))

    @staticmethod
    def scale(Z):
        data_max = max(Z)
        normal_z = Z / data_max
        return normal_z

    def sigmoid(self, x, w, w0):
        z = np.dot(x, w)
        z += w0
        sigmo = 1 / (1 + np.exp(-z))
        return sigmo

    def softmax(self, x, w, k):
        numerator = np.exp(-(np.dot(w.T, x)))
        denominator = 1 / np.sum(numerator, axis=0)
        res = numerator * denominator
        return np.array(res)

    def loss(self, X, Y, W):
        Z = - W.T @ X
        N = X.shape[1]
        loss = 1 / N * (np.trace(W.T @ X @ Y) + np.sum(np.log(np.sum(np.exp(Z), axis=1))))
        return loss

    def Gradient_Descent(self):
        dif = self.Y_onehot - self.softmax(self.X, self.W, len(self.classes)).T
        dw = 1 / self.n * (self.X @ (dif)) + 2 * 0.01 * self.W
        return dw

    def fit(self, iter_rate, iter_nums):
        cost = []
        for _ in range(iter_nums):
            difs = self.Gradient_Descent()
            self.W -= iter_rate * difs
            cost.append(self.loss(self.X, self.Y, self.W))
        return cost

    def predict(self, H):
        Z = - H @ self.W
        P = softmax(Z, axis=1)
        return np.argmax(P, axis=1)

    def evaluate(self, X_test, Y_test):
        j = 0
        x0 = np.ones((1, X_test.shape[0]))
        X_test = np.append(X_test, x0.T, axis=1)
        Y_prime = np.zeros(len(X_test))
        Y_predict = self.predict(X_test).T
        for probability in Y_predict:
            Y_prime[j] = np.argmax(probability)
            j += 1
        temp = Y_test == Y_predict
        temp = np.array(temp, dtype=int)
        accuracy = (np.sum(temp)/len(Y_test))
        return print('Accuracy: ', (accuracy) * 100, '%')


# Load and Splite Dataset
X = load_iris().data
Y = load_iris().target
X, Y = shuffle(X, Y, random_state=10)
x_train_splited, x_test_splited, y_train_splited, y_test_splited = train_test_split(X, Y)

# Fit Model
model = LogesticRegression(x_train_splited, y_train_splited)
model.fit(0.1, 300)

# Evaluate Model
model.evaluate(x_test_splited, y_test_splited)

