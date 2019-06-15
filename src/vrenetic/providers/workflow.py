import pprint
import json
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
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
    # print workflow
    return


def run_get_configuration(id):
    return localdb.getById(id)


def data_get_path(path):
    return __basepath_data__ + '/' + path


def show_print(workflow, options):
    if options.optionJSONPrintAll == True:
        print(json.dumps(workflow))
    else:
        print(workflow['id'], "/", workflow['version'], " - ", workflow['name'])

