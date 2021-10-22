import setuptools
from numpy.distutils.core import setup, Extension
from pathlib import Path

here = Path(__file__).parent.absolute()
changelog = (here / 'CHANGELOG.md').open('r').read()
requirements = (here / 'requirements.txt').open('r').readlines()
version = changelog.split('[')[-1].split(']')[0]
readme = (here / 'README.md').open('r', encoding='utf-8').read()


# ftarcoder42 = Extension('ftarcoder42', [  # 'src/ftarcoder42/ftarcoder42.pyf',
                                        # 'src/ftarcoder42/constantf.f90',
                                        # 'src/ftarcoder42/mathf.f90'])
                                        # 'src/ftarcoder42/physicf.f90'])
# mathtest = Extension('starcoder42.libfib', ['python/starcoder42/libfib.f90'])
print(setuptools.find_packages())
setup(
    name='starcoder42',
    version=version,
    packages=setuptools.find_packages(),
    # ext_modules=[mathtest],
    package_data={
        '': ['*.md']
    },
    description='A set of science and astronomy Python tools',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Dylan Gatlin',
    author_email='dgatlin@apo.nmsu.edu',
    url='https://github.com/StarkillerX42/starcoder42/',
    classifiers=['License :: BSD 3-clause'],
    license='BSD 3-clause',
    license_file='LICENSE.md',
    requirements=requirements,
    zip_safe=True
)
