import pprint
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
from providers.db import localdb


def nn_show(options):
    # pprint.pprint(options)
    if options.nn_id:
        for nn in (localdb.getById(options.nn_id)):
            nn_show_print(nn, options)
    else:
        for nn in (localdb.getAll()):
            nn_show_print(nn, options)

def nn_show_print(nn, options):
    if options.nnShowPrintAll == True:
        pprint.pprint(nn)
    else:
        print(nn['id'], "/", nn['version'], " - ", nn['name'])

def nn_run_get_configuration(id):
    return localdb.getById(id)

def nn_run(options):
    # pprint.pprint(options)

    nn_configuration = {}
    mapper_inputs = []
    if options.nn_id:
        nn_item = nn_run_get_configuration(options.nn_id)
        if len(nn_item):
            nn_configuration = nn_run_get_configuration(options.nn_id)[0]
        else:
            print('Cannot find network by ID')
            exit(1)
    else:
        print('No network ID provided')
        exit(1)

    if nn_configuration['mappers']:
        mapper_json = nn_configuration['mappers'][0]
        mapper_path = './data/' + mapper_json['path']

        nn_mapping_spec = spec_from_loader("module.name", SourceFileLoader("module.name", mapper_path))
        mapping = module_from_spec(nn_mapping_spec)
        nn_mapping_spec = nn_mapping_spec.loader.exec_module(mapping)

        mapper_inputs = mapping.map()

    if nn_configuration['expressions']:
        expression_json = nn_configuration['expressions'][0]
        expression_path = './data/' + expression_json['path']

        nn_expression_spec = spec_from_loader("module.name", SourceFileLoader("module.name", expression_path))
        expresion = module_from_spec(nn_expression_spec)
        nn_expression_spec.loader.exec_module(expresion)

        nn_output = expresion.expression(mapper_inputs)
        pprint.pprint(nn_output)
