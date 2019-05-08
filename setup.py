from __future__ import print_function
from setuptools import setup, find_packages
import io
import codecs
import os
import sys

import solaredge_local

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

setup(
    name='solaredge_local',
    version="0.1.3",
    url='https://github.com/drobtravels/solaredge-local',
    license='MIT License',
    author='David Roberts',
    author_email="",
    description='API wrapper to communicate locally with SolarEdge Inverters',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['solaredge_local'],
    include_package_data=True,
    platforms='any',
    python_requires='>=3.0',
    install_requires=[
        'uplink',
        'uplink-protobuf'
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
