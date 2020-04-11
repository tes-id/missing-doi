# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="doifrombibtex",
    version="0.9",
    author="B. Nennig",
    author_email="benoit.nennig@supmeca.fr",
    description="An utility to parse bibtex files in order to recover the missing DOI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gogs.supmeca.fr:3000/NENNIG/pademe",
    packages=['doifrombibtex'],#setuptools.find_packages(), # we can use find_packages() to automatically discover all packages and subpackages
    package_data={'doifrombibtex': ['examples/*.bib']},
    install_requires=['bibtexparser',
                      'crossrefapi'], # max version for python3.5
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GPL 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5', # tested with python 3.5 may works with previous py3 version...
)