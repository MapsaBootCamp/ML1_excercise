from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import roc_curve as roc

# Load datasetd
X,y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33)
clf = LogisticRegression(random_state=0)

# Train model 
clf.fit(X_train, y_train)

# Predict probablities
y_pred_probability=clf.predict_proba(X_test)[:,1]
roc_plot=roc.ROC()
roc_plot.plot(y_test,y_pred_probability,1)

