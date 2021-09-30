'''
decision tree classifier based on ID3 algorithem

'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report

class DecisionTreeClassifier(object):
        
  def fit(self, orginal_data, target):
    data = orginal_data.copy()
    data[target.name] = target
    self.tree = self.decision_tree(data, data, orginal_data.columns, target.name)

  def entropy(self, feature_column):

    values, counts = np.unique(feature_column, return_counts=True)
    entropy_list = []

    for i in range(len(values)):
      probability = counts[i]/np.sum(counts)
      entropy_list.append(-probability*np.log2(probability))

    total_entropy = np.sum(entropy_list)

    return total_entropy

  def information_gain(self, data, feature_name, target_name):
    total_entropy = self.entropy(data[target_name])

    values, counts = np.unique(data[feature_name], return_counts=True)

    weighted_entropy_list = []

    for i in range(len(values)):
      subset_probability = counts[i]/np.sum(counts)
      subset_entropy = self.entropy(data.where(data[feature_name]==values[i]).dropna()[target_name])
      weighted_entropy_list.append(subset_probability*subset_entropy)

    total_weighted_entropy = np.sum(weighted_entropy_list)

    # calculate information gain
    information_gain = total_entropy - total_weighted_entropy

    return information_gain

  def decision_tree(self, data, original_data, feature_names, target_name, parent_node_class=None):

    # if data is pure, return the majority class of subset
    unique_classes = np.unique(data[target_name])

    if len(unique_classes) <= 1:
      return unique_classes[0]

    # if subset is empty, return majority class of original data
    elif len(data) == 0:
      majority_class_index = np.argmax(np.unique(original_data[target_name], return_counts=True)[1])
      return np.unique(original_data[target_name])[majority_class_index]

    # if dataset contains no features to train, return parent node class
    elif len(feature_names) == 0:
      return parent_node_class

    else:
      # determine parent node class
      majority_class_index = np.argmax(np.unique(data[target_name], return_counts=True)[1])
      parent_node_class = unique_classes[majority_class_index]

      # determine information gain and choose feature 
      info_gain_values=[]
      for feature in feature_names:
         info_gain_values.append(self.information_gain(data, feature, target_name))

      best_feature_index = np.argmax(info_gain_values)
      best_feature = feature_names[best_feature_index]

      tree = {best_feature: {}}

      # remove best feature
      # parent node
      feature_names=[]
      for i in feature_names:
        if i != best_feature:
          feature_names.append(i)

      # create nodes under parent node
      parent_feature_values = np.unique(data[best_feature])
      for value in parent_feature_values:
        sub_data = data.where(data[best_feature] == value).dropna()

        subtree = self.decision_tree(sub_data, original_data, feature_names, target_name, parent_node_class)

        # add subtree to original tree
        tree[best_feature][value] = subtree

      return tree
      
  def predict(self, X_test):

    samples = X_test.to_dict(orient='records')
    predictions = []

    for sample in samples:
      predictions.append(self.make_prediction(sample, self.tree, 1.0))

    return predictions

  def make_prediction(self, sample, tree, default=1):

    for feature in list(sample.keys()):
      if feature in list(tree.keys()):
        try:
          result = tree[feature][sample[feature]]
        except:
          return default

        result = tree[feature][sample[feature]]

        if isinstance(result, dict):
          return self.make_prediction(sample, result)
        else:
          return result

if __name__ == '__main__':

    # create categorical dataset
    data = {
    'Weight': ['Low', 'normal','High'],
    'blood_pressure': ['Low', 'normal','High'],
    'blood_lipids': ['Low', 'normal','High'],
    'smoking':['Yes','No'],
    'heartـattack': ['Yes', 'No']}

    data_df = pd.DataFrame(columns=data.keys())

    # randomnly create 1000 samples
    for i in range(1000):
        data_df.loc[i, 'Weight'] = str(np.random.choice(data['Weight'], 1)[0])
        data_df.loc[i, 'blood_pressure'] = str(np.random.choice(data['blood_pressure'], 1)[0])
        data_df.loc[i, 'blood_lipids'] = str(np.random.choice(data['blood_lipids'], 1)[0])
        data_df.loc[i, 'smoking'] = str(np.random.choice(data['smoking'], 1)[0])
        data_df.loc[i, 'heartـattack'] = str(np.random.choice(data['heartـattack'], 1)[0])

    X = data_df.iloc[:,:-1]
    y = data_df["heartـattack"]
    data = {
    'Weight': ['Low', 'normal','High'],
    'blood_pressure': ['Low', 'normal','High'],
    'blood_lipids': ['Low', 'normal','High'],
    'smoking':['Yes','No'],
    'heartـattack': ['Yes', 'No']}

    data_df = pd.DataFrame(columns=data.keys())

    for i in range(1000):
        data_df.loc[i, 'Weight'] = str(np.random.choice(data['Weight'], 1)[0])
        data_df.loc[i, 'blood_pressure'] = str(np.random.choice(data['blood_pressure'], 1)[0])
        data_df.loc[i, 'blood_lipids'] = str(np.random.choice(data['blood_lipids'], 1)[0])
        data_df.loc[i, 'smoking'] = str(np.random.choice(data['smoking'], 1)[0])
        data_df.loc[i, 'heartـattack'] = str(np.random.choice(data['heartـattack'], 1)[0])

    print(data_df.head())
    X = data_df.iloc[:,:-1]
    y = data_df["heartـattack"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    model = DecisionTreeClassifier()
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    print('accuracy = ',accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))