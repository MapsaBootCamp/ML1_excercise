''' multiple linear regression
    y = m1 * x1 + m2 * x2 + ... + mn * xn + c
'''
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class MultipleLinearRegression(object):

    def __init__(self):
        self.m=[]
        self.c = 0
        self.sc=StandardScaler()
        self.df_out = pd.DataFrame() 
    
    # standardize data
    def standardize(self,x):
        X_transform=self.sc.fit_transform(x)
        return X_transform

    # loss function
    def loss(self,y,y_pred):
        n=len(y)
        s=0
        for i in range(n):
            s+=(y[i]-y_pred[i])**2
        return (1/n)*s
    
    # multiple linear regression equation "wx + c"
    def cal_y(self,weight,x,intercept):
        y_lst=[]
        multiply_temp=0
        for i in range(len(x)):
            multiply_temp=np.multiply(weight,x[i])
            y_lst.append(np.sum(multiply_temp)+intercept) 
        return np.array(y_lst)

    #derivative of loss function based on weight
    def dldw(self,x,y,y_pred):
        s=0
        n=len(y)
        for i in range(n):
            s+=-x[i]*(y[i]-y_pred[i])
        return (2/n)*s
    
    #derivative of loss function based on c
    def dldc(self,y,y_pred):
        n=len(y)
        s=0
        for i in range(len(y)):
            s+=-(y[i]-y_pred[i])
        return (2/n) * s
    

    def _gradient_descent(self,learning_rate,epochs,x,y):
        weight_vector=np.random.randn(x.shape[1])
        intercept=0
        for i in range(epochs):
            y_pred = self.cal_y(weight_vector,x,intercept)
            #update weight
            weight_vector = weight_vector - learning_rate *self.dldw(x,y,y_pred) 
            #update c
            intercept = intercept - learning_rate * self.dldc(y,y_pred)
        
        data_out={'y':y,'y_predicted':y_pred}
        df_out = pd.DataFrame(data_out)  

        return weight_vector,intercept,df_out

    # train model
    def fit(self,x,y,learning_rate,epochs):
        x=self.standardize(x)
        m,c,df_out=self._gradient_descent(learning_rate,epochs,x,y)
        self.m=m
        self.c=c
        self.df_out=df_out

    def predict(self, x_test):
        x_test=np.array(x_test)
        x_test=self.sc.transform(x_test.reshape(1, -1))
        multiply_temp=np.multiply(self.m,x_test)
        y_pred=np.sum(multiply_temp)+self.c
        return y_pred


if __name__ == '__main__':
    boston_data=load_boston()
    boston_df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    boston_df['target']=boston_data.target
    print(boston_df.head())
    x_train=boston_data.data
    y_train=boston_data.target
    learning_rate=0.001
    epochs = 1000 
    mlr_model=MultipleLinearRegression()
    mlr_model.fit(x_train, y_train,learning_rate,epochs)
    print("weight_vector: ")
    print(mlr_model.m)
    print("bias: ")
    print(mlr_model.c)
    print(mlr_model.df_out.head())
    user_input=input("enter your x_test: ").split()
    while user_input!='end':
        x_test=[]
        for elm in user_input:
            x_test.append(float(elm))
        print(x_test)
        print("y_pred = ", mlr_model.predict(x_test))
        user_input=input("enter your x_test or end: ").split()


