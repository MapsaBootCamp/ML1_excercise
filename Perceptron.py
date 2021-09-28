import numpy as np
from numpy import errstate, random
from numpy.random import seed
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import rcParams

# set the plot figure size
rcParams["figure.figsize"] = 10, 5

class Perceptron:

    def __init__(self, learning_rate=0.1, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func =self._unit_step_func
        self.weights = None
        self.bias = None
    
    def fit(self, x, y):
        n_samples, n_features = x.shape

        # init parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.n_iters):

            for idx, x_i in enumerate(x):

                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)

                # Perceptron update rule
                update = self.lr * (y_[idx] - y_predicted)

                self.weights += update * x_i
                self.bias += update

    def predict(self, x):
        linear_output = np.dot(x, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted
    
    def _unit_step_func(self,x):
        return np.where(x>0,1,0)