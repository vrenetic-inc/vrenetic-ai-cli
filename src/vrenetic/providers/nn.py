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

def nn_run_get_configuration(name):
    # get single document from DB by network name
    return {}

def nn_run(options):
    # pprint.pprint(options)

    nn_expression_spec = spec_from_loader("module.name",
        SourceFileLoader("module.name", "./data/assets/06c180564e5934837c7c137d130fdf6d/python/expression.py"))
    nn_mapping_spec = spec_from_loader("module.name",
        SourceFileLoader("module.name", "./data/assets/06c180564e5934837c7c137d130fdf6d/python/mapping.py"))
    
    expresion = module_from_spec(nn_expression_spec)
    mapping = module_from_spec(nn_mapping_spec)
    
    nn_expression_spec.loader.exec_module(expresion)
    nn_mapping_spec.loader.exec_module(mapping)

    inputs = [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    pprint.pprint(expresion.expression(inputs))
    pprint.pprint(mapping.map())