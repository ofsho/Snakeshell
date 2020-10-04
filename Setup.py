import codecs
import os
import sys

from setuptools import find_packages, setup

setup(
  name = 'snakeshell',
  packages = ['snakeshell', 'snakeshell.package', 'snakeshell.utils', 'snakeshell.developer'],
  version = '0.0.0.4.5',
  license='MIT',
  description = 'A Python library for all kinds of Shell Commands',
  author = 'ofsho',
  author_email = 'ofekbendavid9@gmail.com',
  url = 'https://github.com/ofsho/Snakeshell',
  download_url = 'https://github.com/ofsho/Snakeshell/archive/0.0.4c22.tar.gz',
  keywords=['python', 'shell'],
  install_requires=[
          'validators',
          'beautifulsoup4',
          'numba',
          'distro'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)