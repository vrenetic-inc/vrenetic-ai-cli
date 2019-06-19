import json
import pprint
from providers.db import localdb
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader


def show(options):
    if options.ann_id:
        for nn in (localdb.getANNById(options.ann_id)):
            show_print(nn, options)
    else:
        nns = localdb.getANNAll()
        if options.optionJSONPrintAll == True:
            print(json.dumps(nns))
        else:
            for nn in nns:
                show_print(nn, options)


def run(ann_id, ann_dtos):
    configuration = {}
    mapper_inputs = []
    if ann_id:
        nn_item = get_ann_configuration(ann_id)
        if len(nn_item):
            configuration = get_ann_configuration(ann_id)[0]
        else:
            raise ValueError("Cannot find neural network by ID")
    else:
        raise ValueError("No neural network ID provided")

    input_dtos = contract_validator(ann_dtos)

    if configuration["mappers"]:
        mapper_json = configuration["mappers"][0]
        mapper_path = get_path_data_directory(mapper_json["path"])

        nn_mapping_spec = spec_from_loader("module.name", SourceFileLoader("module.name", mapper_path))
        mapping = module_from_spec(nn_mapping_spec)
        nn_mapping_spec = nn_mapping_spec.loader.exec_module(mapping)

        mapper_inputs = mapping.map(input_dtos)

    if configuration["expressions"]:
        expression_json = configuration["expressions"][0]
        expression_path = get_path_data_directory(expression_json["path"])

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


def get_ann_configuration(id):
    return localdb.getANNById(id)


def get_path_data_directory(path):
    return "/".join([__basepath_data__, path])


def show_print(nn, options):
    if options.optionJSONPrintAll == True:
        print(json.dumps(nn))
    else:
        print(nn["id"], "/", nn["version"], " - ", nn["name"])

