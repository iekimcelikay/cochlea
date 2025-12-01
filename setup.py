#!/usr/bin/env python

from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

import numpy

with open('README.rst') as file:
    long_description = file.read()

# Only build zilany2014 extension
extensions = [
    Extension(
        "cochlea.zilany2014._zilany2014",
        [
            "cochlea/zilany2014/_zilany2014.pyx",
            "cochlea/zilany2014/model_IHC.c",
            "cochlea/zilany2014/model_Synapse.c",
            "cochlea/zilany2014/complex.c"
        ],
        define_macros=[
            ('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION'),
            ('CYTHON_CCOMPLEX', '0'),
        ],
        extra_compile_args=['-std=c99']
    ),
]

setup(
    name = "cochlea",
    version = "3",
    author = "Marek Rudnicki",
    author_email = "marek.rudnicki@tum.de",

    description = "Inner ear models in Python",
    license = "GPLv3+",
    url = "https://github.com/mrkrd/cochlea",
    download_url = "https://github.com/mrkrd/cochlea/tarball/master",

    packages = find_packages(),
    scripts = ["scripts/run_zilany2014"],
    package_data = {
        "cochlea. asr": ["*.csv"]
    },
    include_dirs = [numpy.get_include()],
    ext_modules = cythonize(
        extensions,
        compiler_directives={
            'language_level': '3',
            'c_string_type': 'str',
            'c_string_encoding': 'utf8'
        }
    ),
    long_description = long_description,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3. 6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Cython",
        "Programming Language :: C",
    ],

    platforms = ["Linux", "Windows", "FreeBSD", "OSX"],
    install_requires=["numpy", "pandas", "scipy"],
)