from distutils.core import setup

with open("README.MD", "r") as fh:
    long_description = fh.read()

setup(
  name = 'snakeshell',
  packages = ['snakeshell', 'snakeshell.package', 'snakeshell.utils'],
  version = '0.0.0.4c0',
  license='MIT',
  description = 'A Python library for all kinds of Shell Commands',
  author = 'ofshi',
  author_email = 'spamley101@gmail.com',
  url = 'https://github.com/ofsho/Snakeshell',
  download_url = 'https://github.com/ofsho/Snakeshell',
  keywords = ['SHELL', 'PYTHON', 'LIBRARY', 'TERMINAL'],
  install_requires=[
          'validators',
          'beautifulsoup4',
          'numba',
          'distro'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)