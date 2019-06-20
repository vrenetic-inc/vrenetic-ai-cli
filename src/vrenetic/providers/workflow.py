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
            raise ValueError("Cannot find workflow by ID")
    else:
        raise ValueError("No workflow ID provided")

    try:
        validator = workflow_validator(configuration)
    except ValueError as error:
        raise ValueError(error)

    topology = configuration["topology"]
    layers = topology["layers"]

    # TODO: validate output based on contract
    layer_output = run_workflow(layers, workflow_dtos)
    return layer_output


def run_workflow(layers, workflow_dtos):
    ann_outputs = []
    workflow_output = {}

    layer_outputs = None
    for layer in layers:
        if layer["wiring"] != None:
            for wire in layer["wiring"]:
                link = wire.split("---")
                layer_ann_output = link[0].split("::")
                layer_ann_input = link[1].split("::")
                for ann_output in layer_outputs:
                    try:
                        ann_id = layer_ann_output[0]
                        ann_output_name = layer_ann_output[1]
                        output = ann_output[ann_id]
                        try:
                            ann_input_name = layer_ann_input[1]
                            value = output[ann_output_name]
                            workflow_dtos[ann_input_name] = value
                        except:
                            None
                    except:
                        None
        layer_outputs = run_workflow_layer(layer, workflow_dtos)
        ann_outputs += layer_outputs

    for layer in layers:
        if layer["output"] != None:
            for output in layer["output"]:
                link = output.split("---")
                out = link[0].split("::")
                if len(link) == 2:
                    out_alias = link[1]
                else:
                    out_alias = out[1]
                out_id = out[0]
                out_name = out[1]
                for ann_output in ann_outputs:
                    try:
                        workflow_output[out_alias] = (ann_output[out_id][out_name])
                    except:
                        None

    return workflow_output


def run_workflow_layer(layer, workflow_dtos):
    layer_outpus = []

    for ann in layer["ann"]:
        layer_outpus.append({
            ann: run_workflow_layer_ann(ann, workflow_dtos)
        })
    return layer_outpus


def run_workflow_layer_ann(id, workflow_dtos):
    return nn.run(id, workflow_dtos)


def workflow_validator(configuration):
    try:
        topology = configuration["topology"]
        try:
            layers = topology["layers"]
            for layer in layers:
                try:
                    try:
                        id = layer["layer"]
                    except:
                        raise ValueError("Layer index is not defined")
                    try:
                        ann = layer["ann"]
                    except:
                        raise ValueError("Layer ANNs are not defined")
                    try:
                        wiring = layer["wiring"]
                    except:
                        raise ValueError("Layer wiring is not defined")
                    try:
                        output = layer["output"]
                    except:
                        raise ValueError("Layer output is not defined")
                except ValueError as error:
                    raise ValueError(error)
        except ValueError as error:
            raise ValueError(error)
    except ValueError as error:
        raise ValueError(error)
    return True


def run_get_configuration(id):
    return localdb.getWorkflowById(id)


def data_get_path(path):
    return "/".join([__basepath_data__, path])


def show_print(workflow, options):
    if options.optionJSONPrintAll == True:
        print(json.dumps(workflow))
    else:
        print(workflow["id"], "/", workflow["version"], " - ", workflow["name"])

