#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Other Libs
import sys, os
from IPython import get_ipython

# Owned
__author__ = "Sang T. Truong"
__copyright__ = "Copyright 2021, The incomevis project"
__credits__ = ["Sang T. Truong"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Sang T. Truong"
__email__ = "sttruong@cs.stanford.edu"
__status__ = "Dev"

"""
    Path management between local machine in google colab
"""

sys.path.append(os.path.join(os.path.dirname("__file__"), '..'))
sys.path.append(os.path.join(os.path.dirname("__file__"), '..', '..'))

def get_root_dir():
    """
        Get root directory
    """
    dirname = os.getcwd()
    dirname_split = dirname.split("/")
    index = dirname_split.index("incomevis")
    dirname = "/".join(dirname_split[:index + 1])
    return dirname

if 'google.colab' in str(get_ipython()): root = '/content/incomevis'
else: root = get_root_dir()

SOURCE_DATA_PATH    = root + '/data/source_data/'
BENCHMARK_DATA_PATH = root + '/data/benchmark_data/'
DEFLATED_DATA_PATH  = root + '/data/deflated_data/'
OUTPUT_DATA_PATH    = root + '/data/output_data/'