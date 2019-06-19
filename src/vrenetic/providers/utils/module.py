from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader


def load(path):
    spec = spec_from_loader("module.name", SourceFileLoader("module.name", path))
    module = module_from_spec(spec)
    spec = spec.loader.exec_module(module)
    return module

