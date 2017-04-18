import read_files
import process_data
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.feature_selection import RFE
from sklearn import tree

import warnings
warnings.filterwarnings("ignore")


def do_learning(X_training, Y_training, X_test, Y_test, reference_dic, model_class):

    '''
    With training and testing data select the best
    features with recursive feature elimination method, then
    fit a classifier and return a tuple containing the predicted values on the test data
    and a list of the best features used.
    '''
    
    model = model_class
    # Recursive Feature Elimination
    rfe = RFE(model)
    rfe = rfe.fit(X_training, Y_training)
    
    best_features = rfe.get_support(indices=True)

    best_features_names = [reference_dic[i] for i in best_features]

    predicted = rfe.predict(X_test)
    expected = Y_test

    accuracy = accuracy_score(expected, predicted)
    return (expected, predicted, best_features_names, accuracy)


def plot_confusion_matrix(data, label_list, model_name):
    '''
    Given a pandas dataframe with a confusion confusion_matrix
    and a list of axis lables plot the results
    '''
    sn.set(font_scale=1.4)#for label size

    xticks =  label_list
    yticks =  label_list
    ax = plt.axes()
    sn.heatmap(data, annot=True,annot_kws={"size": 16}, linewidths=.5, xticklabels = xticks,  
              yticklabels = yticks, fmt = '')
    ax.set_title('Confusion Matrix for' + ' ' + model_name)