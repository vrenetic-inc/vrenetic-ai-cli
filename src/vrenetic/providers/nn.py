import json
import pprint
from providers.db import localdb
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader


def show(options):
    if options.ann_id:
        for nn in (localdb.getById(options.ann_id)):
            show_print(nn, options)
    else:
        nns = localdb.getAll()
        if options.optionJSONPrintAll == True:
            print(json.dumps(nns))
        else:
            for nn in nns:
                show_print(nn, options)


def run(options):
    configuration = {}
    mapper_inputs = []
    if options.ann_id:
        nn_item = run_get_configuration(options.ann_id)
        if len(nn_item):
            configuration = run_get_configuration(options.ann_id)[0]
        else:
            print('Cannot find neural network by ID')
            exit(1)
    else:
        print('No neural network ID provided')
        exit(1)

    input_dtos = contract_validator(options.ann_dtos)

    if configuration['mappers']:
        mapper_json = configuration['mappers'][0]
        mapper_path = data_get_path(mapper_json['path'])

        nn_mapping_spec = spec_from_loader("module.name", SourceFileLoader("module.name", mapper_path))
        mapping = module_from_spec(nn_mapping_spec)
        nn_mapping_spec = nn_mapping_spec.loader.exec_module(mapping)

        mapper_inputs = mapping.map(input_dtos)

    if configuration['expressions']:
        expression_json = configuration['expressions'][0]
        expression_path = data_get_path(expression_json['path'])

        nn_expression_spec = spec_from_loader("module.name", SourceFileLoader("module.name", expression_path))
        expresion = module_from_spec(nn_expression_spec)
        nn_expression_spec.loader.exec_module(expresion)

        nn_output = expresion.expression(mapper_inputs)
        print(json.dumps(nn_output))


def contract_validator(input_dtos):
    # to be implemented
    # needs storage with contract definitions
    return input_dtos


def run_get_configuration(id):
    return localdb.getById(id)


def data_get_path(path):
    return __basepath_data__ + '/' + path


def show_print(nn, options):
    if options.optionJSONPrintAll == True:
        print(json.dumps(nn))
    else:
        print(nn['id'], "/", nn['version'], " - ", nn['name'])

