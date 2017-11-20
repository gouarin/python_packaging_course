from setuptools import setup, find_packages

setup(
    name = "splinart",
    packages = find_packages(exclude=["demos"]),
    entry_points={ 'console_scripts': [
        'splinart=scripts.cli_splinart:main',
        ],
    },
)