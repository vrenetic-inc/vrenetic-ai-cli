#!/usr/bin/python

try:
    import tensorflow as tf
except Exception as error:
    raise Exception('TensorFlow not supported')


def expression(inputs):

    return {
        "output": inputs[0]
    }

