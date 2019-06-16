#!/usr/bin/python


def map(input_dtos):
        map = []
        try:
                stdio = input_dtos['stdio']
                try:
                        input = float(stdio['input'])
                        if input >= 0.5:
                                input = 1.0

                        if input < 0.5:
                                input = 0.0

                        map.append(input)
                except:
                        None
        except:
                return None

        return map


def map_inputs(input_dtos):
        return input_dtos


def map_outputs(data):
        return data


def inputs():
        return [
                {
                    "name": "input",
                    "type": "float",
                    "contract": {
                        "dto": "input",
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

