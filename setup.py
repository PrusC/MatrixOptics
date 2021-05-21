#
# @File: setup.py.py
#
# Author: Konstantin Prusakov <konstatnin.prusakov@phystech.edu>
#

from setuptools import setup, find_packages

__version__ = 0.2

setup(
    name='MatrixOptics',
    version=__version__,
    description='Matrix Optics',
    author='Konstantin Prusakov',
    author_email='konstatnin.prusakov@phystech.edu',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
)
