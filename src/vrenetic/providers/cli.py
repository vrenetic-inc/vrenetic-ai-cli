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

    parser_cmd_workflow_run = parser_command.add_parser('workflow-run', help='AI Worfklow Run')
    parser_cmd_workflow_run.add_argument('workflow_id', metavar='workflow-id', type=str, help='Workflow Id')

    parser_cmd_workflow_run = parser_command.add_parser('workflow-show', help='AI Worfklow Show')
    parser_cmd_workflow_run.add_argument(
        '--print-json',
        dest="optionJSONPrintAll",
        help="All",
        action='store_const',
        const=True)
    parser_cmd_workflow_run.add_argument(
        '--workflow-id',
        type=str,
        help="AI Workflow ID")

    parser_cmd_ann_run = parser_command.add_parser('ann-run', help='ANN Run')
    parser_cmd_ann_run.add_argument('ann_id', metavar='ann-id', type=str, help='ANN Id')
    parser_cmd_ann_run.add_argument('ann_dtos', metavar='ann-inputs', type=str, nargs='+', help='ANN Input DTOs')

    parser_cmd_ann_show = parser_command.add_parser('ann-show', help='ANN Show')
    parser_cmd_ann_show.add_argument(
        '--ann-id',
        type=str,
        help="Neural Network ID")
    parser_cmd_ann_show.add_argument(
        '--print-json',
        dest="optionJSONPrintAll",
        help="All",
        action='store_const',
        const=True)
    parser_cmd_ann_show.add_argument(
        '--ann-print-metadata',
        dest="optionShowPrintMetadata",
        help="Metadata",
        action='store_const',
        const=logging.INFO)
    parser_cmd_ann_show.add_argument(
        '--ann-print-inputs',
        dest="optionShowPrintInputs",
        help="Inputs",
        action='store_const',
        const=logging.INFO)
    parser_cmd_ann_show.add_argument(
        '--ann-print-outputs',
        dest="optionShowPrintOutputs",
        help="Outputs",
        action='store_const',
        const=logging.INFO)
    parser_cmd_ann_show.add_argument(
        '--ann-print-expressions',
        dest="optionShowPrintExpressions",
        help="Expressions",
        action='store_const',
        const=logging.INFO)
    parser_cmd_ann_show.add_argument(
        '--ann-print-mappers',
        dest="optionShowPrintMAppers",
        help="Mappers",
        action='store_const',
        const=logging.INFO)
    parser_cmd_ann_show.add_argument(
        '--ann-print-projects',
        dest="optionShowPrintProjects",
        help="Projects",
        action='store_const',
        const=logging.INFO)
    return parser