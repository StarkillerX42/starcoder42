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
    ],
    author='Dylan Gatlin',
    author_email='dgatlin@apo.nmsu.edu',
    description=open('README.md', 'r').readlines(),
    url='https://github.com/StarkillerX42/starcoder42/',
    classifiers=['License :: GNU Public License '],
    zip_safe=True
)
