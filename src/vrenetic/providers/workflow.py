import json
import pprint
import providers.nn as nn
from providers.db import localdb


def show(options):
    if options.workflow_id:
        for workflow in (localdb.getWorkflowById(options.workflow_id)):
            show_print(workflow, options)
    else:
        workflows = localdb.getWorkflowAll()
        if options.optionJSONPrintAll == True:
            print(json.dumps(workflows))
        else:
            for workflow in workflows:
                show_print(workflow, options)


def run(workflow_id, workflow_dtos):
    configuration = {}
    mapper_inputs = []
    if workflow_id:
        workflow_item = run_get_configuration(workflow_id)
        if len(workflow_item):
            configuration = run_get_configuration(workflow_id)[0]
        else:
            # TODO: return exception and don't use print
            print('Cannot find workflow by ID')
            exit(1)
    else:
        # TODO: return exception and don't use print
        print('No workflow ID provided')
        exit(1)

    validator = workflow_validator(configuration)

    if validator == 0:
        # TODO: return exception and don't use print
        print('Workflow has errors in schema')
        exit(1)

    topology = configuration['topology']
    layers = topology['layers']

    layer_output = run_workflow(layers, workflow_dtos)
    return layer_output


def run_workflow(layers, workflow_dtos):
    layer_output = []
    for layer in layers:
        layer_output += run_workflow_layer(layer, workflow_dtos)
        # extend workflow_dtos with layer_output
    return layer_output


def run_workflow_layer(layer, workflow_dtos):
    layer_outpus = []
    for ann in layer['ann']:
        layer_outpus.append({
            ann: run_workflow_layer_ann(ann, workflow_dtos)
        })
    return layer_outpus

def run_workflow_layer_ann(id, workflow_dtos):
    return nn.run(id, workflow_dtos)

def workflow_validator(configuration):
    # TODO: return exception and don't use print
    try:
        topology = configuration['topology']
        try:
            layers = topology['layers']
            for layer in layers:
                try:
                    try:
                        id = layer['id']
                    except:
                        print('Layer ID is not defined.')
                        return 0

                    try:
                        ann = layer['ann']
                    except:
                        print('Layer ANNs are not defined.')
                        return 0

                    try:
                        wiring = layer['wiring']
                    except:
                        print('Layer wiring is not defined.')
                        return 0

                    try:
                        output = layer['output']
                    except:
                        print('Layer output is not defined.')
                        return 0
                except:
                    print('Layer generic error.')
                    return 0
        except:
            print("Layers in topology are not defined.")
            return 0
    except:
        print("Topology in workflow is not defined.")
        return 0

    return 1


def run_get_configuration(id):
    return localdb.getWorkflowById(id)


def data_get_path(path):
    return __basepath_data__ + '/' + path


def show_print(workflow, options):
    if options.optionJSONPrintAll == True:
        print(json.dumps(workflow))
    else:
        print(workflow['id'], "/", workflow['version'], " - ", workflow['name'])

