from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

class PerceptronClassifier(object):

    def fit(self,X,y,learning_rate=0.001,epochs=1000):
        X=self.__normalize(X)
        coef,df_out=self.__gradient_descent(X,y,learning_rate,epochs)
        self.bias=coef[0]
        self.weight=coef[1:]
        self.df_out=df_out

    def __perceptron(self,X,weight,bias):
        y_pred=[]
        activation=0
        for i in range(len(X)):
            activation=np.dot(weight,X[i])+bias
            if activation>0.0:
                y_pred.append(1) 
            else:
                y_pred.append(0)
        return np.array(y_pred)
    
    def __loss_function(self,y_pred,y):
        n=len(y)
        s=0
        for i in range(n):
            s+=(y[i]-y_pred[i])**2
        return (1/n)*s

    def normalize(self,data):
        data = (data) / self.data_max
        return data
   
    def __normalize(self,data):
        self.data_max=data.max()
        data = (data) / self.data_max
        return data
    
    #derivative of loss function based on weight
    def __dldw(self,X,y,y_pred):
        s=0
        n=len(y)
        for i in range(n):
            s+=-X[i]*(y[i]-y_pred[i])
        return (2/n)*s

    #derivative of loss function based on bias
    def __dldb(self,y,y_pred):
        n=len(y)
        s=0
        for i in range(len(y)):
            s+=-(y[i]-y_pred[i])
        return (2/n) * s

    def __gradient_descent(self,X,y, learning_rate,epochs):
        self.loss_log=[]
        weight_vector=np.random.randn(X.shape[1])
        bias=0
        for i in range(epochs):
            y_pred = self.__perceptron(X,weight_vector,bias)
            loss = self.__loss_function(y_pred,y)
            self.loss_log.append(loss)
            #update weight
            weight_vector = weight_vector - learning_rate *self.__dldw(X,y,y_pred)
            #update bias
            bias = bias - learning_rate * self.__dldb(y,y_pred)
        
        data_out={'y':y,'y_predicted':np.round(y_pred)}
        df_out = pd.DataFrame(data_out)  
        coef=np.hstack([bias, weight_vector])

        return coef,df_out

    def predict(self,X):
        X=self.normalize(X)
        y_pred=self.__perceptron(X,self.weight,self.bias)
        return y_pred

    def accuracy_metric(self,y_test, y_pred):
        correct = 0
        for i in range(len(y_test)):
            if y_test[i] == y_pred[i]:
                correct += 1
        accuracy=correct / float(len(y_test)) * 100.0
        return accuracy

if __name__ == '__main__':
    X,y= load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    perceptron_model = PerceptronClassifier() 
    perceptron_model.fit(X_train, y_train)
    y_pred=perceptron_model.predict(X_test)
    accuracy=perceptron_model.accuracy_metric(y_test, y_pred)
    print('\n')
    print(perceptron_model.df_out.head())
    print('\n')
    print('-----  weight  -----')
    print(perceptron_model.weight)
    print('\n')
    print('-----  bais  -----')
    print(perceptron_model.bias)
    print('\n')
    print('accuracy: %.2f'  %accuracy +' %')
