#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This code builds a default project data folder.

The project is composed of a code folder and a separate data folder.
The folders are setup as per the following templates:
    https://github.com/deepVector/PythonPrjTemplate
    https://github.com/deepVector/PythonPrjTemplate_data

"""

__author__ = "deepVector: https://github.com/deepVector"
__copyright__ = "Copyright 2020-present, deepVector"
__credits__ = ["itertools: https://docs.python.org",
               "os: https://docs.python.org",
               "shutil: https://docs.python.org"]
__license__ = "CC BY-NC"

import itertools
import os
import shutil

from scribble2digit.utils.paths import (DATA_SUBDIR_PATHS, DIR_CODE_ROOT,
                                        DIR_DATA_ROOT)
from scribble2digit.utils.readme_txt import (README_DATA_BODY,
                                             README_FOOTER_DATA_ROOT,
                                             README_HEADER_DATA_ROOT,
                                             README_HEADER_DATA_SUBDIRS)


def write_readme(dir_path,
                 readme_header,
                 readme_body,
                 readme_footer):
    """Create a README.md file within a folder.

    Args:
        dir_path (str): Folder path.
        readme_header (str): Header of the README.md file.
        readme_body (str): Middle section of the README.md.
        readme_footer (str): Footer section of the README.md.

    Examples:
        >>> write_readme(
                        dir_path=DIR_DATA_ROOT,
                        readme_header=README_HEADER_DATA_ROOT,
                        readme_body=README_DATA_BODY,
                        readme_footer=README_FOOTER_DATA_ROOT)

    """
    readme_path = os.path.join(dir_path, "README.md")

    # Check if a README.md exists in the folder, if not, create one.
    if not os.path.isfile(dir_path):
        with open(readme_path, 'w') as f:
            f.writelines(readme_header)
            f.writelines(readme_body)
            f.writelines(readme_footer)


def build_dir_data_root(dir_data_root,
                        readme_header_data_root,
                        readme_data_body,
                        readme_footer_data_root):
    """Create the root project data folder.

    Args:
        dir_data_root (str): The path to the project data folder.
        readme_header_data_root (str): Header of the README.md file.
        readme_data_body (str): Middle section of the README.md
        readme_footer_data_root (str): Footer section of the README.md

    Returns:
        folder, file: A root project data folder, LICENSE.md, README.md.

    Examples:
        >>> build_dir_data_root(
                dir_data_root=DIR_DATA_ROOT,
                readme_header_data_root=README_HEADER_DATA_ROOT,
                readme_data_body=README_DATA_BODY,
                readme_footer_data_root=README_FOOTER_DATA_ROOT)

    """
    # Check if the root data folder exists, if not, create it.
    if not os.path.isdir(dir_data_root):
        os.mkdir(dir_data_root)

    # Check if the LICENSE file exists, if not, copy it from the code folder
    license_code = os.path.join(DIR_CODE_ROOT, "LICENSE.md")
    license_data = os.path.join(dir_data_root, "LICENSE.md")

    if not os.path.isfile(license_data):
        shutil.copyfile(license_code, license_data)

    # Advise if the source LICENSE.md doesn't exist
    if not os.path.isfile(license_code):
        print("The file: \"" +
              license_code +
              "\" does not exist.")

    # Create a README.md
    write_readme(
        dir_path=dir_data_root,
        readme_header=readme_header_data_root,
        readme_body=readme_data_body,
        readme_footer=readme_footer_data_root)


build_dir_data_root(
    dir_data_root=DIR_DATA_ROOT,
    readme_header_data_root=README_HEADER_DATA_ROOT,
    readme_data_body=README_DATA_BODY,
    readme_footer_data_root=README_FOOTER_DATA_ROOT)


def build_dir_data_subdir(data_subdir_paths):
    """Check if each data subfolder exists, if not, create it.

    Args:
        data_subdir_paths (list): List of subfolder paths.

    Examples:
        >>> build_dir_data_subdir(data_subdir_paths=DATA_SUBDIR_PATHS)

    """
    for data_subdir_path in data_subdir_paths:
        if not os.path.isdir(data_subdir_path):
            os.mkdir(data_subdir_path)


build_dir_data_subdir(data_subdir_paths=DATA_SUBDIR_PATHS)


def build_subdir_readme(data_subdir_paths,
                        readme_header_data_subdirs,
                        readme_data_body,
                        readme_data_footer):
    """Create README.md files in data subdirs.

    Aggregate elements (itertools.zip_longest) from each of the iterables
    (path list and content list) and write the document contents to a
    README.md located in the matching subdirectory.

    Args:
        data_subdir_paths (list): List of paths to data subdirs.
        readme_header_data_subdirs (list): List of data subdir README headers.
        readme_data_body (str): Middle section of the README.md.
        readme_data_footer (str): Footer section of the README.md.

    Examples:
        >>> build_subdir_readme(
                data_subdir_paths=DATA_SUBDIR_PATHS,
                readme_header_data_subdirs=README_HEADER_DATA_SUBDIRS,
                readme_data_body=README_DATA_BODY,
                readme_data_footer=README_DATA_FOOTER)

    """
    for data_subdir_path, readme_header_data_subdir in itertools.zip_longest(
            data_subdir_paths,
            readme_header_data_subdirs):
        write_readme(
            dir_path=data_subdir_path,
            readme_header=readme_header_data_subdir,
            readme_body=readme_data_body,
            readme_footer=readme_data_footer)


build_subdir_readme(
    data_subdir_paths=DATA_SUBDIR_PATHS,
    readme_header_data_subdirs=README_HEADER_DATA_SUBDIRS,
    readme_data_body=README_DATA_BODY,
    readme_data_footer="")
