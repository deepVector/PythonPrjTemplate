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

# Find .env then load the entries as environment variables
path_dotenv = find_dotenv()
load_dotenv(path_dotenv)

variable = os.environ.get("VARIABLE")
