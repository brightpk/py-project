# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = 'py-project'
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = '0.0.1'
finally:
    del get_distribution, DistributionNotFound

from .skeleton import greeting

def hello():
    print("hello world")