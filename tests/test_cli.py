from vrenetic import ai
from vrenetic.providers import nn


class Options:
    ann_id = '123'
    optionJSONPrintAll = True


def test_version():
    assert ai.__version__ == '0.0.2'


def test_cli_dry_run():
    assert ai.main([]) == None

