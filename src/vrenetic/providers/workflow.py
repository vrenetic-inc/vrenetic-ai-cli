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

    # TODO: validate output based on contract
    layer_output = run_workflow(layers, workflow_dtos)
    return layer_output


def run_workflow(layers, workflow_dtos):
    ann_outputs = []
    ann_last_id = ""
    layer_ann_outputs = None
    for layer in layers:
        # TODO: re-think wiring output to input
        if layer['wiring'] != None:
            for wire in layer['wiring']:
                link = wire.split('---')
                layer_ann_output = link[0].split('::')
                layer_ann_input = link[1].split('::')
                for ann_output in layer_ann_outputs:
                    try:
                        ann_id = layer_ann_output[0]
                        ann_output_name = layer_ann_output[1]
                        output = ann_output[ann_id]
                        try:
                            ann_input_name = layer_ann_input[1]
                            value = output[ann_output_name]
                            workflow_dtos[ann_input_name] = value
                            ann_last_id = ann_id
                        except:
                            None
                    except:
                        None
        layer_ann_outputs = run_workflow_layer(layer, workflow_dtos)
        ann_outputs += layer_ann_outputs

    workflow_output = None
    for ann_output in ann_outputs:
        try:
            workflow_output = ann_output[ann_last_id]
        except:
            None

    return workflow_output


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
                        id = layer['layer']
                    except:
                        print('Layer index is not defined.')
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

