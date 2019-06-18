#!/usr/bin/python
import json

def map(input_dtos):
        map = []
        try:
                stdio = input_dtos["stdio"]
                try:
                        input0 = int(stdio["input0"])
                        input1 = int(stdio["input1"])
                        map.append(input0)
                        map.append(input1)
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
                },
                {
                    "name": "input1",
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

