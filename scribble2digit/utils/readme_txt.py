#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file contains project-wide variables."""

__author__ = "deepVector: https://github.com/deepVector"
__copyright__ = "Copyright 2020-present, deepVector"
__credits__ = [""]
__license__ = "cc-by-4.0"

from scribble2digit.utils.functions import get_metadata

# Header of the README.md
README_HEADER_DATA_ROOT = "Project data repository."

readme_header_data_acquired = "The original, immutable input data."

readme_header_data_interim = ("Intermediate, cleaned version " +
                              "of raw input data.")

readme_header_data_models = "Trained models."

readme_header_data_models_output = "Model output."

readme_header_data_processed = ("The final data sets " +
                                "for modelling.")

readme_header_data_reports = "Generated analysis."

readme_header_data_reports_fig = ("Generated graphics " +
                                  "for use in reporting.")

readme_header_data_results = "Final results."

README_HEADER_DATA_SUBDIRS = (
    readme_header_data_acquired,
    readme_header_data_interim,
    readme_header_data_models,
    readme_header_data_models_output,
    readme_header_data_processed,
    readme_header_data_reports,
    readme_header_data_reports_fig,
    readme_header_data_results)

# Middle section of the README.md: same for all files.
README_DATA_BODY = [
    "\n",
    "\n",
    "# Project ID",
    "\n",
    "\n",
    get_metadata(envar="PRJ_ID"),
    "\n",
    "\n",
    "# Authorship information",
    "\n",
    "_Author_: [deepVector](https://github.com/deepVector)",
    "\n",
    "\n",
    "# Licence",
    "\n",
    "This project and its associated data (excluding external input ",
    "data located in the folder _dtAcquired_) are licensed under the ",
    "terms of the ",
    "_Creative Commons Attribution 4.0 International_ ",
    "license (cc-by-4.0; see _LICENSE.md_)."]

# Foter of the README.md: Only for the data root README.
README_FOOTER_DATA_ROOT = [
    "\n",
    "\n",
    "# Credits",
    "\n",
    "Directory structure adapted from ",
    "[Cookiecutter Data Science]",
    "(https://drivendata.github.io",
    "/cookiecutter-data-science/#directory-structure)."]
