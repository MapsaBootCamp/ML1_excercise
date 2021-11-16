import cv2
import glob
import matplotlib.pyplot as plt
import imutils
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.decomposition import PCA, KernelPCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.svm import SVC

from bayes_opt import BayesianOptimization
from bayes_opt.util import Colours


model =  SVC(kernel='linear')
ext = ['jpg', 'JPG', 'pnp', 'jpeg']


# def get_files(path_, ext):
#     temp_paths = []
#     [temp_paths.extend(glob.glob(path_ + '*.' + e)) for e in ext]
#     return temp_paths


files_yes = []
files_no =[]
for e in ext:
    files_yes.extend(glob.glob('/media/sda3/ML/ML1_excercise/data/yes/' + '*.' + e))
    files_no.extend(glob.glob('/media/sda3/ML/ML1_excercise/data/no/' + '*.' + e))


def read_files(files):
    temp_images = []
    for file in files:
        temp_img = cv2.imread(file)
        if temp_img is not None:
            temp_images.append(cv2.imread(file))
    return temp_images

tumor_imgs_yes = read_files(files_yes)
tumor_imgs_no = read_files(files_no)


def crop_brain(image):
    
    # Convert the image to grayscale, and blur it slightly
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours in thresholded image, then grab the largest one
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    # extreme points
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    
    # crop new image out of the original image using the four extreme points (left, right, top, bottom)
    new_image = image[extTop[1]:extBot[1], extLeft[0]:extRight[0]]   
         
    
    return new_image


tumor_imgs_croped_yes = []
tumor_imgs_croped_no = []



for image in tumor_imgs_yes:
    x = crop_brain(image)
    x_resize = cv2.resize(x, (128, 128))
    gray = cv2.cvtColor(x_resize, cv2.COLOR_BGR2GRAY)
    tumor_imgs_croped_yes.append(gray)


for image in tumor_imgs_no:
    x = crop_brain(image)
    x_resize = cv2.resize(x, (128, 128))
    gray = cv2.cvtColor(x_resize, cv2.COLOR_BGR2GRAY)
    tumor_imgs_croped_no.append(gray)


y_yes = np.ones(len(tumor_imgs_croped_yes), dtype="int8")
y_no = np.zeros(len(tumor_imgs_croped_no), dtype="int8")



X = np.concatenate((tumor_imgs_croped_yes, tumor_imgs_croped_no), axis=0)
y = np.concatenate((y_yes, y_no), axis=0)

d1, d2, d3 = X.shape

X = X.reshape((d1, d2 * d3))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)


# scale data before train model
scaler_ = StandardScaler()
X_train_sc = scaler_.fit_transform(X_train)
X_test_sc = scaler_.transform(X_test)

def rfc_cv(n_estimators, min_samples_split, max_features, data, targets):
    estimator = RFC(
        n_estimators=n_estimators,
        min_samples_split=min_samples_split,
        max_features=max_features,
        random_state=2
    )
    cval = cross_val_score(estimator, data, targets,
                           scoring='neg_log_loss', cv=4)
    return cval.mean()

def svc_cv(C, gamma, data, targets):
    estimator = SVC(C=C, gamma=gamma, random_state=2)
    cval = cross_val_score(estimator, data, targets, scoring='roc_auc', cv=4)
    return cval.mean()

def optimize_svc(data, targets):
    """Apply Bayesian Optimization to SVC parameters."""
    def svc_crossval(expC, expGamma):
        C = 10 ** expC
        gamma = 10 ** expGamma
        return svc_cv(C=C, gamma=gamma, data=data, targets=targets)

    optimizer = BayesianOptimization(
        f=svc_crossval,
        pbounds={"expC": (-3, 2), "expGamma": (-4, -1)},
        random_state=1234,
        verbose=2
    )
    optimizer.maximize(n_iter=10)

    print("Final result:", optimizer.max)


def optimize_rfc(data, targets):
    """Apply Bayesian Optimization to Random Forest parameters."""
    def rfc_crossval(n_estimators, min_samples_split, max_features):

        return rfc_cv(
            n_estimators=int(n_estimators),
            min_samples_split=int(min_samples_split),
            max_features=max(min(max_features, 0.999), 1e-3),
            data=data,
            targets=targets,
        )

    optimizer = BayesianOptimization(
        f=rfc_crossval,
        pbounds={
            "n_estimators": (10, 250),
            "min_samples_split": (2, 25),
            "max_features": (0.1, 0.999),
        },
        random_state=1234,
        verbose=2
    )
    optimizer.maximize(n_iter=10)

    print("Final result:", optimizer.max)

print(Colours.yellow("--- Optimizing SVM ---"))
optimize_svc(X_train_sc, y_train)

print(Colours.green("--- Optimizing Random Forest ---"))
optimize_rfc(X_train_sc, y_train)