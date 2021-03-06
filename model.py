import pandas as pd
import joblib
from flask import url_for
import pickle

#for preprocessing
from sklearn.preprocessing import StandardScaler

#model
from sklearn.tree import DecisionTreeClassifier


from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, ConfusionMatrixDisplay, f1_score


#for feature selection using feature wrapper
from sklearn.feature_selection import SequentialFeatureSelector as SFS

#Module to compensate for class imbalance using Oversampling
from imblearn.over_sampling import RandomOverSampler

#Data from Kaggle
df = pd.read_csv("C:\\Users\\nikko\\PycharmProjects\\Professional_Portfolio\\Stroke_Prediction-Web_Deployment\\healthcare-dataset-stroke-data.csv")

#Preprocessing
columns_to_onehot = ['gender', 'work_type', 'smoking_status']


def onehot_code(df, columns):
    """Takes a dataframe and a list of columns that are to be onehot coded. Returns a dataframe"""
    for column in columns:
        one_hot = pd.get_dummies(df[[column]], prefix=column, prefix_sep="_")
        df = pd.concat([df, one_hot], axis=1)
        df.drop(column, axis=1, inplace=True)
    return df


def preprocessing(df, target):
    """Takes a dataframe and target to preprocess the healthcare data.
    Returns X_train, X_test, y_train, y_test"""

    # fill null values with median value; another option is imputation by KNNImputer
    df.fillna(df.median(), inplace=True)

    #set ID as index

    # replace to values to binary
    ##convert ever_married values to boolean so it's machine-interpretable
    df.ever_married.replace({'Yes': 1, 'No': 0}, inplace=True)
    df.Residence_type.replace({'Urban': 1, 'Rural': 0}, inplace=True)

    # onehot coding
    df = onehot_code(df.copy(), columns_to_onehot)

    # define X and y data

    X = df.drop([target, 'id'], axis=1)

    y = df[target]

    #To overcome the class imbalance, implement Oversampling
    ros = RandomOverSampler(random_state=0)
    X, y = ros.fit_resample(X, y)

    # train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle=True, random_state=0)

    # scale features
    # scaler = StandardScaler()
    # scaler.fit(X_train)
    # X_train = pd.DataFrame(scaler.transform(X_train), index=X_train.index, columns=X_train.columns)
    # X_test = pd.DataFrame(scaler.transform(X_test), index=X_test.index, columns=X_test.columns)

    return X_train, X_test, y_train, y_test

X_train_oversampled, X_test_oversampled, y_train_oversampled, y_test_oversampled = preprocessing(df, 'stroke')

clf = DecisionTreeClassifier()
clf.fit(X_train_oversampled, y_train_oversampled)

def predict(form_answers : list):
    return clf.predict(form_answers)

pickle.dump(clf, open('model.pkl', 'wb'))

print(X_train_oversampled.columns)