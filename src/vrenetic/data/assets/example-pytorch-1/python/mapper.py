#!/usr/bin/python
import json


def map_opencl(input_dtos):
        raise Exception('Not implemented')


def map(input_dtos):
        map = []
        try:
                stdio = input_dtos['stdio']
                try:
                        input = float(stdio['input0'])
                        if input >= 0.5:
                                input = 1.0

                        if input < 0.5:
                                input = 0.0

                        map.append(input)
                except:
                        raise ValueError('Invalid inputs. Use: ' + json.dumps(inputs()))
        except ValueError as error:
                raise ValueError(error)

        return map


def map_inputs(input_dtos):
        return input_dtos


def map_outputs(data):
        return data


def inputs():
        return [
                {
                    "name": "input0",
                    "type": "float",
                    "contract": {
                        "dto": "stdio",
                        "param": "input"
                    }
                }
            ]


def outputs():
        return [
                {
                    "name": "output",
                    "type": "float",
                    "contract": {
                        "dto": "output",
                        "param": "output"
                    }
                }
            ]

