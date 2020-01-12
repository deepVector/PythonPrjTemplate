#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Example example_dotenv.py file."""

__author__ = "deepVector: https://github.com/deepVector"
__copyright__ = "Copyright 2020-present, deepVector"
__credits__ = ["os: https://docs.python.org/3/",
               "dotenv: https://saurabh-kumar.com/python-dotenv/"]
__license__ = "CC BY-NC"

import os

from dotenv import find_dotenv, load_dotenv

# Find .env then load the entries as environment variables
path_dotenv = find_dotenv()
load_dotenv(path_dotenv)

variable = os.environ.get("VARIABLE")
