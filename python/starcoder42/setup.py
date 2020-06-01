#!/usr/bin/env python3

from numpy.distutils.core import Extension
from numpy.distutils.core import setup

ftarcoder42 = Extension('ftarcoder42', sources=['ftarcoder42/ftarcoder42.pyf',
                                                'ftarcoder42/constantf.f90',
                                                'ftarcoder42/mathf.f90',
                                                'ftarcoder42/physicf.f90'])
setup(name='ftarcoder42',
      author='Dylan Gatlin',
      author_email='dgatlin@apo.nmsu.edu',
      ext_modules=[ftarcoder42]
)
