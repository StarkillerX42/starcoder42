#!/usr/bin/env python3

import starcoder42 as s
import subprocess as sub
from pathlib import Path
import sys

sources = ['ftarcoder42/ftarcoder42.pyf', 'ftarcoder42/constantf.f90',
           'ftarcoder42/mathf.f90', 'ftarcoder42/physicf.f90']
if 'build' in sys.argv:
    args = ['f2py', '-m', 'ftarcoder42', '-c', *sources]
    sub.call(' '.join(args), shell=True)
    sub.call('mv *.so starcoder42', shell=True)


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('starcoder42', parent_package, top_path)
    config.get_version(version_variable=s.__version__)
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(configuration=configuration,
          install_requires=['numpy', 'sympy'],
          author='Dylan Gatlin',
          author_email='dgatlin@apo.nmsu.edu',
          description=open('README.md', 'r').readlines(),
          url='https://github.com/StarkillerX42/starcoder42/',
          classifiers=['License :: GNU Public License '],
          zip_safe=True
          )
