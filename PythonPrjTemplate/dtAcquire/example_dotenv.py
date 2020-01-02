# -*- coding: utf-8 -*-
"""Example example_dotenv.py file.

Author:
    deepVector
        https://github.com/deepVector
License:
    MIT (see LICENSE.md)

Module credits:
    os:
        https://docs.python.org/3/
    dotenv:
        https://saurabh-kumar.com/python-dotenv/
"""

import os

from dotenv import find_dotenv, load_dotenv

"""Adapted from:
    https://drivendata.github.io/cookiecutter-data-science/#directory-structure
"""

# Find .env by walking up directories until it's found
dotenv_path = find_dotenv()

# Load up the entries as environment variables
load_dotenv(dotenv_path)

variable = os.environ.get("VARIABLE")
