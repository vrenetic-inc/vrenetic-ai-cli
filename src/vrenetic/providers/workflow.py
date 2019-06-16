import json
import pprint
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


def run(options):
    configuration = {}
    mapper_inputs = []
    if options.workflow_id:
        workflow_item = run_get_configuration(options.workflow_id)
        if len(workflow_item):
            configuration = run_get_configuration(options.workflow_id)[0]
        else:
            print('Cannot find workflow by ID')
            exit(1)
    else:
        print('No workflow ID provided')
        exit(1)

    validator = workflow_validator(configuration)

    if validator == 0:
        print('Workflow has errors in schema')
        exit(1)

    print(json.dumps({
        "relevancy-index": 0
    }))


def workflow_validator(configuration):
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

