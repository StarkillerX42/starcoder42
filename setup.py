from setuptools import setup, find_packages
# from numpy.distutils.core import setup as npsetup
import python.starcoder42 as s

# npsetup(name='ftarcoder42',
#         )
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
    requirements=open('requirements.txt', 'r').readlines(),
    zip_safe=True
)
