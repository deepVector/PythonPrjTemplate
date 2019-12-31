# -*- coding: utf-8 -*-
"""Example example_dotenv.py file.

Adapted from:
        https://drivendata.github.io/cookiecutter-data-science/#directory-structure

Module credits:
    os:
        https://docs.python.org/3/
    dotenv:
        https://saurabh-kumar.com/python-dotenv/
"""

import os

from dotenv import find_dotenv, load_dotenv

__author__ = 'deepVector'
__copyright__ = 'Copyright 2020-present, deepVector'
__credits__ = ['']
__license__ = 'MIT'
__version__ = '1.0.1'
__maintainer__ = 'deepVector'
__email__ = 'd33pv3ct0r@gmail.com'
__status__ = 'Dev'

# Find .env by walking up directories until it's found
dotenv_path = find_dotenv()

# Load up the entries as environment variables
load_dotenv(dotenv_path)

variable = os.environ.get("VARIABLE")
