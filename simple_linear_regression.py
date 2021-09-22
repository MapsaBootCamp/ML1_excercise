''' simple linear regression
    y = mx + b
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class SimpleLinearRegression(object):

    def __init__(self):
        self.m = 0
        self.c = 0
        self.df_out = pd.DataFrame() 

    def _gradient_descent(self,learning_rate,epochs,x,y):
        m=0
        c = 0
        print(epochs)
        n = float(len(x))
        for i in range(epochs): 
            y_pred = m*x + c  
            # derivative wrt m and c
            D_m = (-2/n) * sum(x * (y - y_pred))  
            D_c = (-2/n) * sum(y - y_pred) 
            # update m and m
            m = m - learning_rate * D_m  
            c = c - learning_rate * D_c 
        data_out={'y':y,'y_predicted':y_pred}
        df_out = pd.DataFrame(data_out)  

        return m, c, df_out

    def fit(self,x,y,learning_rate,epochs):
        m,c,df_out=self._gradient_descent(learning_rate,epochs,x,y)
        self.m=m
        self.c=c
        self.df_out=df_out

    def predict(self, x_test):
        y_pred=self.m*x_test+self.c
        return y_pred

    def plot(self,x_train, y_train):
        plt.scatter(x_train, y_train) 
        plt.title("Simple Linear Regression")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.plot(x_train,self.m*x_train+self.c, color='red',label="y = "+str(self.m)+" x + "+ str(self.c))
        plt.legend()
        plt.show()

if __name__ == '__main__':
    tips = sns.load_dataset("tips")
    print(tips.head())
    learning_rate=0.0001
    epochs = 1000 
    x_train = tips.loc[:, "total_bill"]
    y_train = tips.loc[:, "tip"]
    lr_model=SimpleLinearRegression()
    lr_model.fit(x_train, y_train,learning_rate,epochs)
    print("y = "+str(lr_model.m)+" x + "+ str(lr_model.c))
    print(lr_model.df_out.head())
    x_test=input("enter your total bill: ")
    while x_test!='end':
        print("y_pred = ", lr_model.predict(float(x_test)))
        x_test=input("enter your total bill or end: ")
    do_plot=input("show simple linear regression (Y/N):")
    if do_plot=="Y":
        lr_model.plot(x_train, y_train)
    else:
        print("end")
