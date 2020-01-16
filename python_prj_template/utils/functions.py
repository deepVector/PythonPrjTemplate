#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file contains project-wide utility functions."""

__author__ = "deepVector: https://github.com/deepVector"
__copyright__ = "Copyright 2020-present, deepVector"
__credits__ = ["os: https://docs.python.org",
               "shutil: https://docs.python.org",
               "dotenv: https://github.com/theskumar/python-dotenv",
               "mdutils: https://github.com/didix21/mdutils"]
__license__ = "CC BY-NC"

import os

from dotenv import find_dotenv, load_dotenv


def get_metadata(ENVAR):
    """Load the .env data as environment variables.

    This function uses the find_dotenv() module to walk accross the project
    folder until the .env file is found.  It then uses the load_dotenv() to
    load the .env variables as environment variables.

    Credits:
        https://github.com/theskumar/python-dotenv

    Args:
        ENVAR (str): Name of a variables defined in the .env file.

    Returns:
        str: Variable from the .env file.

    Examples:
        Retrieve the project ID, stored as .env variable.
        >>> prj_id = get_metadata(ENVAR="PRJ_ID")

    """
    load_dotenv(find_dotenv())
    envar = os.environ.get(ENVAR)
    return envar
