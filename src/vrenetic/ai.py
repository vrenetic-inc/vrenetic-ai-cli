#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import logging
import pprint
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
from tinydb import TinyDB, Query


__author__ = "kris-lab"
__copyright__ = "VRenetic Inc."
__license__ = "MIT"
__version__ = "0.0.1"

_logger = logging.getLogger(__name__)


def parse_args(args):
    parser = argparse.ArgumentParser(
        description="VRenetic AI Cli")
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '--version',
        action='version',
        version='vrenetic-ai {ver}'.format(ver=__version__))
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    parser_command = parser.add_subparsers(help = 'Sub-command help')
    parser_cmd_nn_run = parser_command.add_parser('nn-run', help='Neural Network Run')
    parser_cmd_nn_show = parser_command.add_parser('nn-show', help='Neural Network Show')
    parser_cmd_nn_show.add_argument(
        '--nn-print-inputs',
        dest="loglevel",
        help="Neural Netowrk Inputs",
        action='store_const',
        const=logging.INFO)
    parser_cmd_nn_show.add_argument(
        '--nn-print-outputs',
        dest="loglevel",
        help="Neural Netowrk Outpus",
        action='store_const',
        const=logging.INFO)
    parser_cmd_nn_show.add_argument(
        '--nn-print-models',
        dest="loglevel",
        help="Neural Netowrk Models",
        action='store_const',
        const=logging.INFO)
    return parser.parse_args(args)


def setup_logging(loglevel):
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")

    # Item = Query()
    # db = TinyDB('./data/db.json')
    # table = db.table('models')
    # pprint.pprint(table.search(Item.app.matches("vre")))
    # table.insert(model)
    # pprint.pprint(table.all())
    # exec(open('./data/assets/06c180564e5934837c7c137d130fdf6d/vresh-feed-relevance-v1.py').read(), globals() )
    # spec = spec_from_loader("module.name",
        # SourceFileLoader("module.name", "./data/assets/06c180564e5934837c7c137d130fdf6d/vresh-feed-relevance-v1.py"))
    # mod = module_from_spec(spec)
    # spec.loader.exec_module(mod)
    # inputs = [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    # pprint.pprint(mod.expression(inputs))
    _logger.info("Script ends here")


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
