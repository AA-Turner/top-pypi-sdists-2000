#!/usr/bin/env python
# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

import io
import os

import setuptools

# Package metadata.

name = "pandas-gbq"
description = "Google BigQuery connector for pandas"

# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 4 - Beta"
dependencies = [
    "setuptools",
    "db-dtypes >=1.0.4,<2.0.0",
    "numpy >=1.18.1",
    "pandas >=1.1.4",
    "pyarrow >=4.0.0",
    "pydata-google-auth >=1.5.0",
    # Note: google-api-core and google-auth are also included via transitive
    # dependency on google-cloud-bigquery, but this library also uses them
    # directly.
    "google-api-core >= 2.10.2, <3.0.0",
    "google-auth >=2.13.0",
    "google-auth-oauthlib >=0.7.0",
    # Please also update the minimum version in pandas_gbq/features.py to
    # allow pandas-gbq to detect invalid package versions at runtime.
    "google-cloud-bigquery >=3.4.2,<4.0.0",
    "packaging >=22.0.0",
]
extras = {
    "bqstorage": [
        "google-cloud-bigquery-storage >=2.16.2, <3.0.0",
    ],
    "tqdm": ["tqdm>=4.23.0"],
    "geopandas": ["geopandas>=0.9.0", "Shapely>=1.8.4"],
}

# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

version = {}
with open(os.path.join(package_root, "pandas_gbq/version.py")) as fp:
    exec(fp.read(), version)
version = version["__version__"]

# Only include packages under the 'google' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package
    for package in setuptools.find_namespace_packages()
    if package.startswith("pandas_gbq")
]


setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="pandas-gbq authors",
    author_email="googleapis-packages@google.com",
    license="BSD-3-Clause",
    url="https://github.com/googleapis/python-bigquery-pandas",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    install_requires=dependencies,
    extras_require=extras,
    python_requires=">=3.9",
    include_package_data=True,
    zip_safe=False,
)
