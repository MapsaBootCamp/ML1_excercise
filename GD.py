import numpy as np

from DirectMethod import LinearRegression


class LinearRegressionGradiantDescent(LinearRegression):
    def _cost_function(self, mat_x: np.ndarray, vec_y: np.ndarray, regularization: bool):
        hypothesis = mat_x @ self.coef_ + self.intercept_
        return np.linalg.norm(np.subtract(hypothesis, vec_y)) / 2 + (
            np.linalg.norm(self.coef_) if regularization else 0)

    def _gradient_descent(
            self, mat_x: np.ndarray, vec_y: np.ndarray, linear_rate=0.001, regularization=False, laanda=0.001
            ):
        hypothesis = mat_x @ self.coef_ + self.intercept_
        loss = np.subtract(hypothesis, vec_y)
        self.intercept_ -= linear_rate * np.average(loss)
        self.coef_ -= linear_rate * (loss @ mat_x) / loss.shape[-1]
        if regularization:
            self.coef_ += laanda * self.coef_
        return self._cost_function(mat_x, vec_y, regularization)

    def fit(
            self, mat_x: np.ndarray, vec_y: np.ndarray, linear_rate=0.05, max_iteration=1000, stop_criteria=1e-3,
            regularization=False, laanda=0.0001, error_record=False
            ):
        if error_record:
            self.err_ls_ = []
        self.intercept_ = 0
        self.coef_ = np.zeros(mat_x.shape[-1])
        self._scale_train(mat_x)
        mat_x_scale = self._make_scale(mat_x)
        error = np.nan
        for _ in range(max_iteration):
            error = self._gradient_descent(mat_x_scale, vec_y, linear_rate, regularization, laanda)
            if error_record:
                self.err_ls_.append(error)
            if error < stop_criteria:
                break
        else:
            print(f"train process doesn't converge and error is {error}")
        return self


if __name__ == '__main__':
    x_train = np.random.randint(-100, 100, 100).reshape([-1, 1])
    y_train = x_train[:, 0] * 3 + 1
    model = LinearRegressionGradiantDescent()
    model.fit(x_train, y_train, regularization=True)
    print(model.predict(x_train[[3, 5, 7]]).round())
    print(y_train[[3, 5, 7]])
    print(y_train[[3, 5, 7]])
