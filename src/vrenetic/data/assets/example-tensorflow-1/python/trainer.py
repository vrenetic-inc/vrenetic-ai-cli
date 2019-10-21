#!/usr/bin/python

# https://www.tensorflow.org/tutorials/estimator/linear
# https://www.tensorflow.org/tutorials/keras/save_and_load#saving_custom_objects
# https://www.tensorflow.org/tutorials/load_data/csv
# https://github.com/tensorflow/tensorflow/issues/31927

import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf
import functools
from tensorflow import keras
from tensorflow.python.keras.models import load_model

print(tf.version.VERSION)

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

from sklearn.metrics import roc_curve
from matplotlib import pyplot as plt

from functools import partial


class PackNumericFeatures(object):
  def __init__(self, names):
    self.names = names

  def __call__(self, features, labels):
    numeric_freatures = [features.pop(name) for name in self.names]
    numeric_features = [tf.cast(feat, tf.float32) for feat in numeric_freatures]
    numeric_features = tf.stack(numeric_features, axis=-1)
    features['numeric'] = numeric_features

    return features, labels


class TensorflowModule(keras.models.Sequential):

    TRAIN_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
    TEST_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"
    
    MEAN = 0
    STD = 0

    NUMERIC_FEATURES = ['age','n_siblings_spouses','parch', 'fare']
    CATEGORIES = {
        'sex': ['male', 'female'],
        'class' : ['First', 'Second', 'Third'],
        'deck' : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'embark_town' : ['Cherbourg', 'Southhampton', 'Queenstown'],
        'alone' : ['y', 'n']
    }

    numeric_columns = []
    categorical_columns = []

    LABEL_COLUMN = 'survived'
    LABELS = [0, 1]

    train_data = ""
    test_data = ""
    train_file_path = ""
    test_file_path = ""

    def __init__(self, **kwargs):
        super(TensorflowModule, self).__init__(**kwargs)
        self.load_module_data()
        self.f_1 = self.preprocessing_layer()
        self.dense_1 = keras.layers.Dense(128, activation='relu')
        self.dense_2 = keras.layers.Dense(128, activation='relu')
        self.output_1 = keras.layers.Dense(1, activation='sigmoid')
        
    def call(self, inputs):
        x = self.f_1(inputs)
        y = self.dense_1(x)
        z = self.dense_2(y)
        return self.output_1(z)
    
    def get_config(self):
        base_config = super().get_config()
        return{**base_config, "output_dim" : 1, "activation": 2}

    def load_module_data(self):
        self.train_file_path = tf.keras.utils.get_file("train.csv", self.TRAIN_DATA_URL)
        self.test_file_path = tf.keras.utils.get_file("eval.csv", self.TEST_DATA_URL)

        raw_train_data = self.get_dataset(self.train_file_path)
        raw_test_data = self.get_dataset(self.test_file_path)

        packed_train_data = raw_train_data.map(PackNumericFeatures(self.NUMERIC_FEATURES))
        packed_test_data = raw_test_data.map(PackNumericFeatures(self.NUMERIC_FEATURES))

        self.train_data = packed_train_data.shuffle(500)
        self.test_data = packed_test_data

    def get_dataset(self, file_path, **kwargs):
        dataset = tf.data.experimental.make_csv_dataset(
            file_path,
            batch_size=5, # Artificially small to make examples easier to show.
            label_name=self.LABEL_COLUMN,
            na_value="?",
            num_epochs=1,
            ignore_errors=True, 
            **kwargs)
        return dataset

    def preprocessing_layer(self):
        print(self.train_file_path)
        desc = pd.read_csv(self.train_file_path)[self.NUMERIC_FEATURES].describe()
        # global MEAN
        # global STD
        self.MEAN = np.array(desc.T['mean'])
        self.STD = np.array(desc.T['std'])

        # global numeric_columns
        numeric_columns = []
        numeric_column = tf.feature_column.numeric_column('numeric', normalizer_fn=self.normalize_numeric_data, shape=[len(self.NUMERIC_FEATURES)])
        numeric_columns = [numeric_column]

        # global categorical_columns
        categorical_columns = []
        for feature, vocab in self.CATEGORIES.items():
            cat_col = tf.feature_column.categorical_column_with_vocabulary_list(
                key=feature, vocabulary_list=vocab)
            categorical_columns.append(tf.feature_column.indicator_column(cat_col))

        preprocessing_layer = tf.keras.layers.DenseFeatures(categorical_columns+numeric_columns)
        return preprocessing_layer

    def normalize_numeric_data(self, data):
        return (data-self.MEAN)/self.STD


def test_run(options):
    model = create_model()
    model.fit(model.train_data, epochs=10)
    model.summary()

    test_loss, test_accuracy = model.evaluate(model.test_data)
    print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))

    predictions = model.predict(model.test_data)
    for prediction, survived in zip(predictions[:10], list(model.test_data)[0][1][:10]):
        print("Predicted survival: {:.2%}".format(prediction[0]),
            " | Actual outcome: ",
            ("SURVIVED" if bool(survived) else "DIED"))

    model.save(get_model_storage_path())

    new_model = load_model(get_model_storage_path(), custom_objects={
                    'PackNumericFeatures': PackNumericFeatures,
                    'normalize_numeric_data': TensorflowModule.normalize_numeric_data,
                    'TensorflowModule': TensorflowModule
            })
    new_model.summary()


def train(options):
    raise ValueError("Not implemented")


def create_model():
    model = TensorflowModule()
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def get_model_storage_path():
    path = os.path.dirname(__file__)
    return "/".join([path, "trained/model.h5"])