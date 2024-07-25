#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'bikeshare_model'
DESCRIPTION = "Titanic dataset classification model package "
EMAIL = "------"
AUTHOR = "----------"
REQUIRES_PYTHON = ">=3.7.0"


# The rest no need to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# Trove Classifiers: https://pypi.org/classifiers/

long_description = DESCRIPTION

# Load the package's VERSION file as a dictionary.
about = {}
ROOT_DIR = Path(__file__).parent
print(ROOT_DIR)
REQUIREMENTS_DIR = ROOT_DIR / 'requirements'
PACKAGE_DIR = ROOT_DIR / 'bikeshare_model'

# with open(PACKAGE_DIR / "VERSION") as f:
#     print("********* side version file")
#     _version = f.read().strip()
#     print("******VERSION is ", _version)
#     about["__version__"] = _version
about["__version__"]="0.0.1"


# What packages are required for this module to be executed?
# def list_reqs(fname="requirements.txt"):
#     with open(REQUIREMENTS_DIR / fname) as fd:
#        print ("REQUIREMENTS ARE ", fd.read().splitlines())
#        return fd.read().splitlines()

# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=("tests",)),
    package_data={"regression_model": ["0.0.1"]},
    # install_requires=list_reqs(),
    # install_requires = ['numpy>=1.21.0,<2.0.0', 'pandas>=1.3.5,<2.0.0', 'pydantic>=1.8.1,<2.0.0', 'scikit-learn==1.3.0', 'strictyaml>=1.3.2,<2.0.0', 'ruamel.yaml>=0.16.12,<1.0.0', 'joblib>=1.0.1,<2.0.0 '],
    extras_require={},
    include_package_data=True,
    license="BSD-3",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)

print("***************** SETUP COMPLETED")