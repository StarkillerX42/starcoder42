from setuptools import setup, find_packages

setup(
    name='Starcoder42',
    version='3.6.1',
    packages=find_packages(),
    package_data={
        '': ['starcoder42']
    },
    install_requires=[
        'numpy', 'sympy'
    ]
    author='Dylan Gatlin',
    author_email='dgatlin@apo.nmsu.edu',
    description="""This is my own code library. It has many cool functions using
the numpy and sympy libraries. Everything tries to be in snake_case, but
dictionary keys are still in CapitalCase. For more extensions on this involving
sympy, try starcoder42.math. It's recommended you import this via
import starcoder42 as s
import starcoder42.math

Notable features:
s.reload: A function to reload packages
s.estimate_rgb: A function to give a color of a spectra
s.find_index: A function that can find the closest corresponding index, even if
    your guess isn't in the array
s.describe: A function to describe the contents of a multidimensional array
""",
    url='https://github.com/StarkillerX42/starcoder42/',
    classifiers=['License :: GNU Public License '],
    zip_safe=True
)
