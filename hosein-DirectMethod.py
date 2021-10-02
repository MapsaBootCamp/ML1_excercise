import numpy as np


class LinearRegression:
    def _scale_train(self, mat_x: np.ndarray):
        self.min_array_ = np.min(mat_x, axis=0)
        self.range_array_ = np.max(mat_x, axis=0) - self.min_array_

    def _make_scale(self, mat_x: np.ndarray) -> np.ndarray:
        if mat_x.shape[-1] == self.min_array_.shape[0]:
            return (mat_x - self.min_array_) / self.range_array_
        else:
            raise Exception('فرمت ماتریس ورودی با ماتریس تعلیم ابتدایی یکسان نیست')

    def fit(self, mat_x: np.ndarray, vec_y: np.ndarray, regularization=False, laanda=0.001):
        if mat_x.shape[0] != vec_y.shape[0]:
            raise Exception("X , Y tafahom nadaran")
        vec_1 = np.ones(mat_x.shape[0], dtype='int8').reshape((-1, 1))
        self._scale_train(mat_x)
        mat_train_temp = np.hstack([vec_1, self._make_scale(mat_x)])
        try:
            matmul = np.matmul(mat_train_temp.T, mat_train_temp)
            if regularization:
                matmul += np.eye(matmul.shape[0]) * laanda
            vec_w = np.matmul(np.linalg.inv(matmul), np.matmul(mat_train_temp.T, vec_y))
        except np.linalg.LinAlgError as err:
            print(err)
            print('fit IMPOSSIBLE')
            return None
        self.coef_ = vec_w[1:]
        self.intercept_ = vec_w[0]
        return self

    def _predict(self, vec_test: np.ndarray) -> np.ndarray:
        if vec_test.shape[0] != self.coef_.shape[0]:
            raise Exception("tedad feature ha ro kamel nadadi")
        return np.dot(self._make_scale(vec_test), self.coef_) + self.intercept_

    def predict(self, mat_test):
        return np.array([self._predict(x_sample) for x_sample in mat_test])

    @staticmethod
    def evaluate(vec_test: np.ndarray, vec_predict: np.ndarray):
        error = 0
        non_zeros: np.ndarray = vec_test != 0
        if any(non_zeros):
            error += np.average(abs(vec_predict[non_zeros] / vec_test[non_zeros] - 1))
        if any(~non_zeros):
            error += np.average(vec_predict[~non_zeros])
        return error


if __name__ == '__main__':
    x_train = np.random.randint(-100, 100, 10).reshape([-1, 1])
    y_train = x_train[:, 0] * 3 + 1
    model = LinearRegression()
    model.fit(x_train, y_train)
    print(model.predict(x_train))
    print(y_train)
