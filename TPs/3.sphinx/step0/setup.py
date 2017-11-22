# Author:
#     Loic Gouarin <loic.gouarin@gmail.com>
#
# License: BSD 3 clause
from setuptools import setup, find_packages

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development",
    "Topic :: Scientific/Engineering",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: MacOS"
]

name = "splinart"

MAJOR = 0
MINOR = 1
PATCH = 2
VERSION = "{}.{}.{}".format(MAJOR, MINOR, PATCH)

with open("splinart/version.py", "w") as f:
    f.write("__version__ = '{}'\n".format(VERSION))

setup(
    name = "splinart",
    author = "loic.gouarin@gmail.com",
    description = "spline art generator",
    version = VERSION,
    license = "BSD",
    classifiers = CLASSIFIERS,
    packages = find_packages(exclude=["demos"]),
    install_requires = ["numpy",
                        "matplotlib>=2",
                        "six"],
    entry_points={ 'console_scripts': [
        'splinart=scripts.cli_splinart:main',
        ],
    },
)