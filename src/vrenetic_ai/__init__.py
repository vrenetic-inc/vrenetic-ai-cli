# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    dist_name = 'vrenetic-ai'
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = '0.0.0'
finally:
    del get_distribution, DistributionNotFound
