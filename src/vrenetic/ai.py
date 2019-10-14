#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import logging
import pprint
import os

try:
    from .providers import application, cli, nn, workflow
except ModuleNotFoundError:
    from providers import application, cli, nn, workflow

try:
    from .providers.db import localdb
except:
    from providers.db import localdb


__author__ = "kris-lab <krzysztof.piotr.stasiak@gmail.com>"
__copyright__ = "kris-lab"
__license__ = "MIT"
__version__ = "0.0.3"

__basepath__ = os.path.dirname(os.path.realpath(__file__))
__basepath_data__ = __basepath__ + "/data"
__basepath_db__ = __basepath_data__ + "/db.json"
_logger = logging.getLogger(__name__)


def setup_logging(loglevel):
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    modules_init()

    parser = cli.init(__version__, logging)
    args = parser.parse_args(args)
    setup_logging(args.loglevel)

    if args.command == "ann-run":
        try:
            data = json.loads(args.ann_dtos[0])
            results = nn.run(args.ann_id, data)
            print(json.dumps(results))
        except ValueError as error:
            print(error)
            exit(1)
    if args.command == "ann-show":
        nn.show(args)
    if args.command == "workflow-run":
        try:
            data = json.loads(args.workflow_dtos[0])
            results = workflow.run(args.workflow_id, data)
            print(json.dumps(results))
        except ValueError as error:
            print(error)
            exit(1)
    if args.command == "workflow-show":
        workflow.show(args)
    if args.command == "info":
        application.info(args, __version__)


def modules_init():
    nn.__basepath_data__ = __basepath_data__
    localdb.__basepath_db__ = __basepath_db__


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
