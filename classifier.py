from GD import LinearRegressionGradiantDescent
import numpy as np


class ClassifierRegression(LinearRegressionGradiantDescent):
    def _sigmoid(self, mat_x: np.ndarray):
        hypothesis = mat_x @ self.coef_ + self.intercept_
        return (1 + np.exp(-hypothesis)) ** -1.0

    def _cost_function(self, mat_x: np.ndarray, vec_y: np.ndarray, *args, **kwargs):
        sigmoid = self._sigmoid(mat_x)
        return -np.average(vec_y * np.log(sigmoid) + (1 - vec_y) * np.log(1. - sigmoid))

    def _gradient_descent(self, mat_x: np.ndarray, vec_y: np.ndarray, linear_rate=0.001, *args, **kwargs):
        sigmoid = self._sigmoid(mat_x)
        loss = np.subtract(sigmoid, vec_y)
        self.intercept_ -= linear_rate * np.average(loss)
        self.coef_ -= linear_rate * (loss @ mat_x) / loss.shape[-1]
        return self._cost_function(mat_x, vec_y, )

    def _predict(self, vec_test: np.ndarray) -> np.ndarray:
        if vec_test.shape[0] != self.coef_.shape[0]:
            raise Exception("tedad feature ha ro kamel nadadi")
        return np.floor(self._sigmoid(vec_test) + 0.5)

    def fit(self, *args, **kwargs):
        if not set(args[1]) <= {0, 1}:
            raise Exception('بردار خروجی تنها می تواند شامل 0 و 1 باشد')
        super().fit(*args, **kwargs)


if __name__ == '__main__':
    x_train = np.random.randint(-100, 100, 100).reshape([-1, 1])
    lik = np.sign(x_train[:, 0] * 3 + 1)
    y_train = (np.abs(lik) + lik) / 2
    model = ClassifierRegression()
    model.fit(x_train, y_train)
    print(model.predict(x_train[[3, 5, 7]]).round())
    print(y_train[[3, 5, 7]])
