from distutils.core import setup

import os
import io

here = os.path.abspath(os.path.dirname(__file__))
DESCRIPTION = 'A Library for Fuzzy Logic and Fuzzy Systems'

try:
    with io.open(os.path.join(here, 'README'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name='pyfuzzy',
    version='0.1dev',
    packages=['pyfuzzy',],
    license='Apache License, Version 2.0',
    long_description=long_description, requires=['numpy']
)
