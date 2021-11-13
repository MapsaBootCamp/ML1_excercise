import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.utils import shuffle


class linearRegression:

    def trian_test_split(self):
        pass

    def scale(self, Z):
        data_max = max(Z)
        normal_z = Z/data_max
        return normal_z

    def get_train_data(self, X_train, Y_train):
        self.n = X_train.shape[0]
        self.m = X_train.shape[1]
        self.W = np.zeros((self.m,1))
        self.W0 = 0
        # self.X = np.append(x0, np.array(X_train))
        # self.X = self.X.reshape(n, -1)
        self.X = np.array(X_train)
        self.Y = np.array(Y_train)
        self.Y = self.Y.reshape(-1, 1)
        # self.W0 = np.zeros((n,1))

    def sigmoid(self, x, w, w0):
        z = np.dot(x, w)
        z += w0
        sigmo = 1/(1+np.exp(-z))
        return sigmo

    def softmax(self, x, w, w0, k):
        numerator = np.exp(-(np.dot(w,x)+w0))
        denominator = np.sum(np.exp(-(np.dot(w,x)+w0)))
        pass

    def Cost_function(self):
        C1 = self.Y*np.log(self.sigmoid(self.X, self.W, self.W0))
        C2 = (1-self.Y)*np.log(1-self.sigmoid(self.X, self.W, self.W0))
        J = np.mean(-C1-C2)
        return J

    def Gradient_Descent(self):
        dif = self.sigmoid(self.X, self.W, self.W0) - self.Y
        # dif = np.reshape(dif, self.n)
        dw = np.dot(self.X.T, dif)/self.n
        # dw.reshape(1, self.n)

        dw0 = np.sum(dif)/self.n
        return [dw, dw0]

    def Train_model(self, iter_rate, iter_nums):
        cost = []
        # self.W = np.array([self.W])
        for _ in range(iter_nums):
            difs = self.Gradient_Descent()
            self.W = self.W - iter_rate*difs[0]
            self.W0 = self.W0 - iter_rate * difs[1]
            cost.append(self.Cost_function())
        return cost   

    def predict(self, x_test):
        # y_predict = np.dot(self.W.T, x_test) + self.W0
        y_predict = self.sigmoid(x_test.T, self.W, self.W0)
        return y_predict

    def evaluate(self, X_test, Y_test):
        Y_pridict = self.W.T * X_test + self.W0
        accuracy = (np.sum(Y_test) - np.sum(Y_pridict))/np.sum(self.Y)
        return print('Accuracy: ', accuracy*100, '%')


# if __name__ == '_main_':
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['lable'] = data.target
df = shuffle(df)

a = np.array([[1,2],[3,4],[5,6],[7,8],[9,3],[4,5],[6,7],[8,9],[10,11]])
# b = np.array([1,2,3,4,5,6,7,8,9])
c = np.array([0, 0, 0, 1, 0, 1, 1, 1, 1])

model = linearRegression()
model.get_train_data(a, c)
# model.Train_model(0.1, 10)
# model.get_train_data(a,b)
print(model.Train_model(0.1, 100))
x_t = np.array([1.5, 2.6]).reshape(-1,1)
print(model.predict(x_t))


