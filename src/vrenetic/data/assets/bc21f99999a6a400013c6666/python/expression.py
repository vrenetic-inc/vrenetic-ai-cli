#!/usr/bin/python


def expression(inputs):
    return {
        "output": inputs[0] | inputs[1]
    }


def expression_opencl(inputs):
    raise Exception('Not implemented')

