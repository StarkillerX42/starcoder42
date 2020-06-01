from setuptools import setup, find_packages
import python.starcoder42 as s

setup(
    name='starcoder42',
    version=s.__version__,
    package_dir={'': 'python'},
    packages=find_packages('python'),
    author='Dylan Gatlin',
    author_email='dgatlin@apo.nmsu.edu',
    description=open('README.md', 'r').readlines(),
    url='https://github.com/StarkillerX42/starcoder42/',
    classifiers=['License :: GNU Public License '],
    zip_safe=True
)
