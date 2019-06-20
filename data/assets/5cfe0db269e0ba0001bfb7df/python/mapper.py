#!/usr/bin/python


def map_opencl(input_dtos):
        raise Exception('Not implemented')


def map(input_dtos):
        # TODO
        # Need to map
        # - categorical inputs
        # - binary inputs
        # - continues inputs
        # for DTOs values into NN inputs
        return [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]


def map_inputs(input_dtos):
        return input_dtos


def map_outputs(data):
        return data


def inputs():
        return [
                {
                    "name": "user_age",
                    "type": "continues",
                    "contract": {
                        "dto": "user",
                        "param": "user-age"
                    }
                },
                {
                    "name": "user_role",
                    "type": "categorical",
                    "contract": {
                        "dto": "user",
                        "param": "user-role"
                    }
                },
                {
                    "name": "content_tags",
                    "type": "binary",
                    "contract": {
                        "dto": "content",
                        "param": "content-tags"
                    }
                }
            ]


def outputs():
        return [
                {
                    "name": "relevancy_index",
                    "type": "float",
                    "contract": {
                        "dto": "relevancy",
                        "param": "relevancy-index"
                    }
                }
            ]

