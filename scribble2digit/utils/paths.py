#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Project path definitions."""

__author__ = "deepVector: https://github.com/deepVector"
__copyright__ = "Copyright 2020-present, deepVector"
__credits__ = ["os: https://docs.python.org"]
__license__ = "cc-by-4.0"

import os

# Get the path of the working (code) directory
DIR_CODE_ROOT = os.getcwd()

# Define the path to project data folder
DIR_DATA_ROOT = os.path.join(DIR_CODE_ROOT + "_data")

# Define a list of subfolder names for the code and data folders
dir_code_subdir_path_ids = ["conf",
                            "docs",
                            "references"]

dir_data_subdir_path_ids = ["dtAcquired",
                            "dtInterim",
                            "dtProcessed",
                            "dtResults",
                            "models",
                            "modelsOutput",
                            "reports",
                            "reportsFig"]

# Assign paths
(DIR_CODE_CONF,
 DIR_CODE_DOCS,
 DIR_CODE_REF) = [
    os.path.join(
        DIR_CODE_ROOT,
        dir_code_subdir_path_id)
    for dir_code_subdir_path_id in dir_code_subdir_path_ids]

(DIR_DATA_ACQUIRED,
 DIR_DATA_INTERIM,
 DIR_DATA_PROCESSED,
 DIR_DATA_RESULTS,
 DIR_DATA_MODELS,
 DIR_DATA_MODELS_OUTPUT,
 DIR_DATA_REPORTS,
 DIR_DATA_REPORTS_FIG) = [
    os.path.join(
        DIR_DATA_ROOT,
        dir_data_subdir_path_id)
    for dir_data_subdir_path_id in dir_data_subdir_path_ids]

DATA_SUBDIR_PATHS = (DIR_DATA_ACQUIRED,
                     DIR_DATA_INTERIM,
                     DIR_DATA_MODELS,
                     DIR_DATA_MODELS_OUTPUT,
                     DIR_DATA_PROCESSED,
                     DIR_DATA_REPORTS,
                     DIR_DATA_REPORTS_FIG,
                     DIR_DATA_RESULTS)
