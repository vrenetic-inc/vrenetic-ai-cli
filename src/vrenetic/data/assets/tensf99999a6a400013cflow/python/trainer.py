#!/usr/bin/python

# https://www.tensorflow.org/tutorials/estimator/linear

import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

from sklearn.metrics import roc_curve
from matplotlib import pyplot as plt

dftrain = pd.DataFrame()
dfeval = pd.DataFrame()


def test_run(options):
    load_data({})
    feature_columns = configure_columns()
    linear_est = train(feature_columns)
    test_eval(linear_est)


def train(options):
    raise ValueError("Not implemented")


def configure_columns():
    # tf.keras.backend.set_floatx('float64')

    CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck', 'embark_town', 'alone']
    NUMERIC_COLUMNS = ['age', 'fare']

    feature_columns = []
    for feature_name in CATEGORICAL_COLUMNS:
        vocabulary = dftrain[feature_name].unique()
        feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

    for feature_name in NUMERIC_COLUMNS:
        feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

    return feature_columns


def train(feature_columns):
    y_train = dftrain.pop('survived')
    dftrain['class'].value_counts().plot(kind='barh')
    pd.concat([dftrain, y_train], axis=1).groupby('sex').survived.mean().plot(kind='barh').set_xlabel('% survive')
    
    train_input_fn = make_input_fn(dftrain, y_train)

    age_x_gender = tf.feature_column.crossed_column(['age', 'sex'], hash_bucket_size=100)
    derived_feature_columns = [age_x_gender]
    linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns+derived_feature_columns)
    linear_est.train(train_input_fn)

    return linear_est


def test_eval(linear_est):
    y_eval = dfeval.pop('survived')
    eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=3, shuffle=False)
    result = linear_est.evaluate(eval_input_fn)
    print("111")
    print_result(result)


def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
    def input_function():
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
        if shuffle:
            ds = ds.shuffle(1000)
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds
    return input_function


def load_data(options):
    global dftrain
    global dfeval
    path = os.path.dirname(__file__)
    dftrain = pd.read_csv("/".join([path, "data/train.csv"]))
    dfeval = pd.read_csv("/".join([path, "/data/eval.csv"]))


def print_result(result):
    clear_output()
    print(result)


def print_metadata():
    print(dftrain.head())
    print(dftrain.describe())
    print(dftrain.shape[0], dfeval.shape[0])
    print(dftrain.age.hist(bins=20))
    print(dftrain.sex.value_counts().plot(kind='barh'))


def plot_results():
    pred_dicts = list(linear_est.predict(eval_input_fn))
    probs = pd.Series([pred['probabilities'][1] for pred in pred_dicts])
    probs.plot(kind='hist', bins=20, title='predicted probabilities')
    fpr, tpr, _ = roc_curve(y_eval, probs)
    plt.plot(fpr, tpr)
    plt.title('ROC curve')
    plt.xlabel('false positive rate')
    plt.ylabel('true positive rate')
    plt.xlim(0,)
    plt.ylim(0,)

