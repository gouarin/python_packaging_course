from setuptools import setup, find_packages

MAJOR = 0
MINOR = 1
MAINTENANCE = 0
VERSION = "{}.{}.{}".format(MAJOR, MINOR, MAINTENANCE)

with open("splinart/version.py", "w") as f:
    f.write("__version__ = '{}'\n".format(VERSION))

setup(
    name = "splinart",
    packages = find_packages(exclude=["demos"]),
    entry_points={ 'console_scripts': [
        'splinart=scripts.cli_splinart:main',
        ],
    },
)