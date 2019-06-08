#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
import pprint

from providers import nn, cli


__author__ = "kris-lab <krzysztof.piotr.stasiak@gmail.com>"
__copyright__ = "VRenetic, Inc."
__license__ = "MIT"
__version__ = "0.0.2"

_logger = logging.getLogger(__name__)


def setup_logging(loglevel):
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    parser = cli.init(__version__, logging)
    args = parser.parse_args(args)
    setup_logging(args.loglevel)

    if args.command == 'nn-run':
        nn.nn_run(args)
    if args.command == 'nn-show':
        nn.nn_show(args)


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
