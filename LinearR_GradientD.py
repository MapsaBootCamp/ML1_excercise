import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.utils import shuffle


class LinearRegression_GD:

    def get_train_data(self, X_train, Y_train):
        n = X_train.shape[0]
        m = X_train.shape[1]
        self.X = np.array(X_train) 
        self.X = self.X.reshape(-1,m)
        self.Y = np.array(Y_train)
        self.Y = self.Y.reshape(-1,1)
        self.W = np.zeros((self.X.shape[1], 1))
        self.W0 = np.zeros((1,1))

    def Cost_function(self, Regularisation=None, landa=0):
        if Regularisation == None:
            Y_i = (self.W * self.X) + self.W0
            loss = (np.subtract(self.Y, Y_i))**2
            sample_size = self.Y.shape[0]
            MSE = np.sum(loss)/(2*sample_size)
            return MSE
        elif Regularisation == 'Ridge':
            Y_i = (self.W * self.X) + self.W0
            loss = (np.subtract(self.Y, Y_i))**2 + landa*(np.sum(self.W)**2)
            sample_size = self.Y.shape[0]
            MSE = np.sum(loss)/(2*sample_size)
            return MSE
        elif Regularisation == 'Lasso':
            Y_i = (self.W * self.X) + self.W0
            loss = (np.subtract(self.Y, Y_i))**2 + landa*(np.sum(abs(self.W)))
            sample_size = self.Y.shape[0]
            MSE = np.sum(loss)/(2*sample_size)
            return MSE


    def Gradient_Descent(self, intercept=False):
        Y_pridict = self.W * self.X + self.W0
        sample_size = self.Y.shape[0]
        if intercept:
            dw = np.sum((Y_pridict-self.Y))/sample_size
        else:
            dw = np.sum((Y_pridict-self.Y) * self.X)/sample_size 
        return dw

    def Train_model(self, iter_rate, iter_nums, regularise_parameter=None, landa=0):
        cost = []
        for _ in range(iter_nums):
            temp = self.W - iter_rate*self.Gradient_Descent()
            temp0 = self.W0 - iter_rate*self.Gradient_Descent(intercept=True)
            self.W = temp
            self.W0 = temp0
            cost.append(self.Cost_function(regularise_parameter, landa))
        return cost   

    def evaluate(self, X_test, Y_test):
        Y_pridict = self.W * X_test + self.W0
        accuracy = (np.sum(Y_test) - np.sum(Y_pridict))/np.sum(self.Y)
        return print(accuracy*100)

# if __name__ == '_main_':
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['lable'] = data.target
df = shuffle(df)

# a = np.array([1,2,3,4,5,6,7,8,9])
# b = np.array([1,2,3,4,5,6,7,8,9])

model = LinearRegression_GD()
model.get_train_data(df[['sepal length (cm)','petal length (cm)']][0:99], df['sepal width (cm)'][0:99])
model.Train_model(0.01, 100, regularise_parameter='Ridge', landa=0.1)
xtest = np.array(df[['sepal length (cm)','petal length (cm)']])[100:,:]
ytest = np.array(df['lable'][100:]).reshape(-1,1)
model.evaluate(xtest, ytest)
    # model.get_train_data(a,b)
    # print(model.Train_model(0.01, 100, regularise_parameter='Ridge', landa=0.1))

