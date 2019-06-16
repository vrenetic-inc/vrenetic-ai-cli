#!/usr/bin/python


def map(input_dtos):
        map = []

        try:
                input = float(input_dtos['input'])
                if input >= 0.5:
                        input = 1.0

                if input < 0.5:
                        input = 0.0

                map.append(input)
        except:
                return None

        return map

def map_inputs(input_dtos):
        return input_dtos


def map_outputs(data):
        return data

def inputs():
        return []

def outputs():
        return []

