# -*- coding: utf-8 -*-
"""
    Setup file for py_project.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.2.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import sys

from pkg_resources import VersionConflict, require
from setuptools import setup

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":
    setup(use_pyscaffold=True)

setup(name='py-project',
      version='0.1',
      description='Sample of packaging python project',
      url='https://github.com/brightpk/py-project',
      author='Bright Phakamad',
      author_email='bright@example.com',
      license='BrightPK',
      packages=['py_project'],
      zip_safe=False)
