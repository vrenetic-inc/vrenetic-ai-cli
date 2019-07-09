import json
import pprint
from .db import localdb
from .utils import module

class ANN:
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

        try:
            contract_validator(configuration)
        except ValueError as error:
            raise ValueError(error)

        if configuration["mappers"]:
            mappers = configuration["mappers"]
            mapper_inputs = load_default_mapper(mappers).map(ann_dtos)
            # mapper_inputs = load_default_mapper(mappers).map_opencl(ann_dtos)

        if configuration["expressions"]:
            expressions = configuration["expressions"]
            # nn_output = load_default_expression(expressions).expression_opencl(mapper_inputs)
            # from backends import opencl
            # return opencl.run(nn_output)
            nn_output = load_default_expression(expressions).expression(mapper_inputs)
            return nn_output

        return None


    def load_default_mapper(mappers):
        mapper_config = mappers[0]
        mapper_path = get_path_data_directory(mapper_config["path"])
        return module.load(mapper_path)


    def load_default_expression(expressions):
        expression_config = expressions[0]
        expression_path = get_path_data_directory(expression_config["path"])
        return module.load(expression_path)


    def contract_validator(configuration):
        try:
            try:
                mappers = configuration["mappers"]
                try:
                    default_mapper = mappers[0]
                except:
                    raise ValueError('Missing default mappers configuration')
            except:
                raise ValueError('Missing mappers configuration')
            try:
                expressions = configuration["expressions"]
                try:
                    default_expressions = expressions[0]
                except:
                    raise ValueError('Missing default expression configuration')
            except:
                raise ValueError('Missing expressions configuration')
        except ValueError as error:
            raise ValueError(error)
        return True


    def get_ann_configuration(id):
        return localdb.getANNById(id)


    def get_path_data_directory(path):
        return "/".join([__basepath_data__, path])


    def show_print(nn, options):
        if options.optionJSONPrintAll == True:
            print(json.dumps(nn))
        else:
            print(nn["id"], "/", nn["version"], " - ", nn["name"])

