import argparse

def init(version, logging):
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
        version='vrenetic-ai {ver}'.format(ver=version))
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    
    parser_command = parser.add_subparsers(help = 'Commands help', dest='command')

    parser_cmd_nn_run = parser_command.add_parser('nn-run', help='Neural Network Run')
    parser_cmd_nn_run.add_argument('nn_id', metavar='nn-id', type=str, help='NN Id')
    parser_cmd_nn_run.add_argument('nn_dtos', metavar='nn-inputs', type=str, nargs='+', help='NN Input DTOs')

    parser_cmd_nn_show = parser_command.add_parser('nn-show', help='Neural Network Show')
    parser_cmd_nn_show.add_argument(
        '--nn-id',
        type=str,
        help="Neural Network ID")
    parser_cmd_nn_show.add_argument(
        '--nn-print-all',
        dest="nnShowPrintAll",
        help="All",
        action='store_const',
        const=True)
    parser_cmd_nn_show.add_argument(
        '--nn-print-metadata',
        dest="nnShowPrintMetadata",
        help="Metadata",
        action='store_const',
        const=logging.INFO)
    parser_cmd_nn_show.add_argument(
        '--nn-print-inputs',
        dest="nnShowPrintInputs",
        help="Inputs",
        action='store_const',
        const=logging.INFO)
    parser_cmd_nn_show.add_argument(
        '--nn-print-outputs',
        dest="nnShowPrintOutputs",
        help="Outputs",
        action='store_const',
        const=logging.INFO)
    parser_cmd_nn_show.add_argument(
        '--nn-print-expressions',
        dest="nnShowPrintExpressions",
        help="Expressions",
        action='store_const',
        const=logging.INFO)
    parser_cmd_nn_show.add_argument(
        '--nn-print-mappers',
        dest="nnShowPrintMAppers",
        help="Mappers",
        action='store_const',
        const=logging.INFO)
    parser_cmd_nn_show.add_argument(
        '--nn-print-projects',
        dest="nnShowPrintProjects",
        help="Projects",
        action='store_const',
        const=logging.INFO)
    return parser