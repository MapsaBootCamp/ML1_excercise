import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris



class Perceptron:
    def fit(self, X_train, Y_train, alpha, epochs):
        self.X = np.array(X_train)
        self.Y = np.array(Y_train).reshape(-1, 1)
        self.W = np.random.normal(0, 1, len(X_train.T)).reshape(-1, 1)
        err = np.zeros((len(X_train)))

        for i in range(epochs):
            for j, sample in enumerate(self.X):
                sample = sample.reshape(-1, 1)
                Y_p = self.predict(sample, self.W)
                err[j] = self.Y[j] - Y_p
                self.W = self.W + alpha*err[j]*sample

    def predict(self, x, w):
        Z = np.dot(w.T, x)
        A = self.sigmoid(Z)
        return A

    def sigmoid(self, z):
        return 1/(1+np.exp(-z))

    def evaluate(self, X_test, Y_test):
        j = 0
        X_test = np.array(X_test)
        Y_predict = self.predict(X_test.T, self.W).T
        Y_prime = np.where(Y_predict<0.5, 0, 1)
        temp = Y_test.reshape(-1, 1) == Y_prime.reshape(-1, 1)
        temp = np.array(temp, dtype=int)
        accuracy = (np.sum(temp) / len(Y_test))
        return print('Accuracy: ', (accuracy) * 100, '%')



# Load and Splite Dataset
X = load_iris().data[:100]
Y = load_iris().target[:100]
x_train_splited, x_test_splited, y_train_splited, y_test_splited = train_test_split(X, Y)

# Fit Model
model = Perceptron()
model.fit(x_train_splited, y_train_splited, 0.1, 300)

# Evaluate Model
model.evaluate(x_test_splited, y_test_splited)

