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


def run(ann_id, ann_dtos):
    configuration = {}
    mapper_inputs = []
    if ann_id:
        nn_item = run_get_configuration(ann_id)
        if len(nn_item):
            configuration = run_get_configuration(ann_id)[0]
        else:
            # TODO: return exception and don't use print
            print('Cannot find neural network by ID')
            exit(1)
    else:
        # TODO: return exception and don't use print
        print('No neural network ID provided')
        exit(1)

    input_dtos = contract_validator(ann_dtos)

    if configuration['mappers']:
        mapper_json = configuration['mappers'][0]
        mapper_path = data_get_path(mapper_json['path'])

        nn_mapping_spec = spec_from_loader("module.name", SourceFileLoader("module.name", mapper_path))
        mapping = module_from_spec(nn_mapping_spec)
        nn_mapping_spec = nn_mapping_spec.loader.exec_module(mapping)

        mapper_inputs = mapping.map(input_dtos)

        if mapper_inputs == None:
            print('Invalid inputs provided for neural network.')
            exit(1)

    if configuration['expressions']:
        expression_json = configuration['expressions'][0]
        expression_path = data_get_path(expression_json['path'])

        nn_expression_spec = spec_from_loader("module.name", SourceFileLoader("module.name", expression_path))
        expresion = module_from_spec(nn_expression_spec)
        nn_expression_spec.loader.exec_module(expresion)

        nn_output = expresion.expression(mapper_inputs)
        return nn_output

    return None


def contract_validator(input_dtos):
    # TODO: move inputs/outputs definition for json db to mapper.py files
    # TODO: move contract definition into mappers section
    # TODO: to be implemented
    # TODO: needs storage with contract definitions
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

