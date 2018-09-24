from sklearn import tree, preprocessing
from numpy import array
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


def encode_row(row):
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(row)
    return integer_encoded


def train_predict(features, labels, prediction):
    cls = tree.DecisionTreeClassifier()
    cls.fit(features, labels)
    return cls.predict(prediction)
