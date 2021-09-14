import numpy as np


class Perceptron:
    @staticmethod
    def __checker(mat_x, vec_y):
        if len(mat_x.shape) != 2:
            raise Exception(
                    'ماتریس ضرایب به درستی وارد نشده است. این ماتریس باید به صورت دو بعدی با سطرهایی به تعداد نمونه ها '
                    'باشد')
        if len(vec_y.shape) != 1 or mat_x.shape[0] != vec_y.shape[0]:
            raise Exception(
                    'بردار نتایج به درستی وارد نشده است. این بردار باید تک سطری و به تعداد نمونه ها (سطرهای ماتریس '
                    'ضرایب) '
                    'باشد')
        if not set(vec_y) <= {1, -1}:
            raise Exception('بردار نتایج تنها باید شامل 1 و -1 باشد')

    def fit(self, mat_x: np.ndarray, vec_y: np.ndarray, sample_retest=100, voted=False, recording=False):
        self.__checker(mat_x, vec_y)
        self.voted = int(voted)
        temp_x: np.ndarray = np.hstack([np.ones((mat_x.shape[0], 1)), mat_x]).T
        self.coef_: np.ndarray = vec_y[0] * temp_x[:, 0]
        self.weight_: np.ndarray = np.ones(1)
        for _ in range(sample_retest):
            predicts = self.__predict(temp_x)
            comparison = predicts != vec_y
            if not any(comparison):
                break
            if voted:
                pass
            else:
                self.coef_ += np.sum(vec_y[comparison] * temp_x[:, comparison], axis=1)
        else:
            print(f'مدل در تعداد تست تعریف شده نتوانست ابر صفحه را پیدا کند')
        return self

    def __predict(self, temp_x: np.ndarray):
        return np.sign(self.weight_ * (self.coef_ @ temp_x))

    def predict(self, mat_x: np.ndarray):
        if len(mat_x.shape) != 2:
            raise Exception(
                    'ماتریس ضرایب به درستی وارد نشده است. این ماتریس باید به صورت دو بعدی با سطرهایی به تعداد نمونه ها '
                    'باشد')
        if mat_x.shape[1] != self.coef_.shape[-1] - 1:
            raise Exception('تعداد پارامترها (ستون ها)ی ماتریس با تعداد پارامترهای مدل برابر نیست')
        temp_x: np.ndarray = np.hstack([np.ones((mat_x.shape[0], 1)), mat_x]).T
        return self.__predict(temp_x)


if __name__ == '__main__':
    mat_x = np.array([[1, 1, 1],
                      [2, 2, 2],
                      [3, 3, 3]])
    vec_y = np.array([-1, 1, 1])
    model = Perceptron().fit(mat_x, vec_y)
    mat_test = np.array([[-1, -1, -1],
                         [5, 5, 5]])
    print(model.predict(mat_test))
