import numpy as np
from sklearn.datasets import load_iris
from sklearn.utils import shuffle
from scipy.special import softmax


class LogesticRegression:

    def __init__(self, X_train, Y_train):
        self.X = X_train.T
        self.m = X_train.shape[1]  # features
        self.n = X_train.shape[0]  # sample size
        self.Y = np.array(Y_train)  # train lable
        self.Y = self.Y.reshape(-1, 1)
        self.classes = np.unique(self.Y)
        self.Y_onehot = np.zeros((self.n, len(self.classes)))
        for i in range(self.n):
            self.Y_onehot[i, Y_train[i]] = 1
        try:
            self.W = np.zeros((self.m, len(self.classes)))
            # self.W0 = 0
        except:
            self.W = np.zeros((self.m + 1, 1))
            # self.W0 = 0

    @staticmethod
    def trian_test_split(x, y, test_size=0.2):
        if len(x) == len(y):
            train_sample = int(len(x) * (1 - test_size))
            x = np.array(x)
            y = np.array(y)
        else:
            raise Exception('samples and lables are not in same size!!!')
        Xtrain = x[0:train_sample, :]
        Ytrain = y[0:train_sample]
        Xtest = x[train_sample:, :]
        Ytest = y[train_sample:]
        return Xtrain, Ytrain, Xtest, Ytest

    @staticmethod
    def scale(Z):
        data_max = max(Z)
        normal_z = Z / data_max
        return normal_z

    def get_train_data(self, X_train, Y_train):
        # x0 = np.ones((1, self.n))
        # self.X = np.append(x0, np.array(X_train).T, axis=0)      # train data
        pass

    def sigmoid(self, x, w, w0):
        z = np.dot(x, w)
        z += w0
        sigmo = 1 / (1 + np.exp(-z))
        return sigmo

    def softmax(self, x, w, k):
        # res = []
        # for class_type in range(k):
        #     numerator = np.exp(-(np.dot(w[:, class_type].T, x)))
        #     denominator = np.sum(np.exp(-(np.dot(w[:, class_type].T, x))))
        # Z = - self.W.T @ self.X
        # P = softmax(Z, axis=0)
        # res.append(numerator/denominator)
        numerator = np.exp(-(np.dot(w.T, x)))
        denominator = 1 / np.sum(numerator, axis=0)
        res = numerator * denominator
        return np.array(res)

    def Cost_function(self):
        C1 = np.dot(np.log(self.softmax(self.X, self.W, len(self.classes))), self.Y_onehot)
        C2 = np.dot(np.log(1 - self.softmax(self.X, self.W, len(self.classes))), (1 - self.Y_onehot))
        J = np.mean(-C1 - C2)
        return J

    def loss(self, X, Y, W):
        Z = - W.T @ X
        N = X.shape[1]
        loss = 1 / N * (np.trace(W.T @ X @ Y) + np.sum(np.log(np.sum(np.exp(Z), axis=1))))
        return loss

    def Gradient_Descent(self):
        dif = self.Y_onehot - self.softmax(self.X, self.W, len(self.classes)).T

        # dw = np.dot(self.X[1:, :], dif)/self.n
        dw0 = np.sum(dif) / self.n

        dw = 1 / self.n * (self.X @ (dif)) + 2 * 0.01 * self.W
        return dw
        # return [dw, dw0]

    def fit(self, iter_rate, iter_nums):
        cost = []
        for _ in range(iter_nums):
            difs = self.Gradient_Descent()
            self.W -= iter_rate * difs
            # self.W[1:,:] = self.W[1:,:] - iter_rate*difs[0]
            # self.W[0,:] = self.W[0,:] - iter_rate*difs[1]
            # cost.append(self.Cost_function())
            cost.append(self.loss(self.X, self.Y, self.W))
        return cost

        # def predict(self, x_test):

    #     y_predict = self.softmax(x_test.T, self.W, len(self.classes))
    #     return y_predict
    def predict(self, H):
        Z = - H @ self.W
        P = softmax(Z, axis=1)
        return np.argmax(P, axis=1)

    def evaluate(self, X_test, Y_test):
        j = 0
        # x0 = np.ones((1, X_test.shape[0]))
        # X_test = np.append(x0.T, X_test, axis=1)
        # X_test =
        Y_prime = np.zeros(len(X_test))
        Y_predict = self.predict(X_test).T
        for probability in Y_predict:
            Y_prime[j] = np.argmax(probability)
            j += 1
        # accuracy = (np.sum(Y_test) - np.sum(Y_prime))/np.sum(self.Y)
        # return print('Accuracy: ', accuracy*100, '%')
        accuracy = (np.sum(Y_test) - np.sum(Y_predict)) / np.sum(Y_test)
        return print('Accuracy: ', (1 - accuracy) * 100, '%')


# if __name__ == '_main_':


model = linearRegression()
# model.get_train_data(a, c)
# model.Train_model(0.1, 10)
# model.get_train_data(a,b)
# print(model.Train_model(0.1, 100))
# x_t = np.array([1.5, 2.6]).reshape(-1,1)
# print(model.predict(x_t))

X = load_iris().data
Y = load_iris().target
X, Y = shuffle(X, Y, random_state=10)

x_train_splited, y_train_splited, x_test_splited, y_test_splited = model.trian_test_split(X, Y)
# fit model
model.get_train_data(x_train_splited, y_train_splited)
model.fit(0.1, 300)

model.evaluate(x_test_splited, y_test_splited)

# predict
# print(model.predict(np.array([6.6, 3.2, 4.6, 1.45])))
# print(np.sum(model.predict(np.array([6.6, 3.2, 4.6, 1.45]))))
