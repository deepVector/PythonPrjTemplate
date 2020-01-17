#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Project-wide utility functions."""

__author__ = "deepVector: https://github.com/deepVector"
__copyright__ = "Copyright 2020-present, deepVector"
__credits__ = ["os: https://docs.python.org",
               "shutil: https://docs.python.org",
               "dotenv: https://github.com/theskumar/python-dotenv",
               "mdutils: https://github.com/didix21/mdutils"]
__license__ = "cc-by-4.0"

import os

from dotenv import find_dotenv, load_dotenv


def get_metadata(envar):
    """Load the .env data as environment variables.

    This function uses the find_dotenv() module to walk accross the project
    folder until the .env file is found.  It then uses the load_dotenv() to
    load the .env variables as environment variables.

    Credits:
        https://github.com/theskumar/python-dotenv

    Args:
        envar (str): Name of a variables defined in the .env file.

    Returns:
        str: Variable from the .env file.

    Examples:
        Retrieve the project ID, stored as .env variable.
        >>> prj_id = get_metadata(envar="PRJ_ID")

    """
    load_dotenv(find_dotenv())
    environ_var = os.environ.get(envar)
    return environ_var
