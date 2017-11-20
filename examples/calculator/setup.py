from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

extension = [Extension(name = "calculator.cython_mod", 
                       sources = ["calculator/cython_mod.pyx"])
            ]

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Cython",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development",
    "Topic :: Scientific/Engineering",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: MacOS"
]

MAJOR = 0
MINOR = 1
MAINTENANCE = 1
VERSION = "{}.{}.{}".format(MAJOR, MINOR, MAINTENANCE)

with open("calculator/version.py", "w") as f:
    f.write("__version__ = '{}'\n".format(VERSION))

setup(
    name = "calculator",
    author = "loic.gouarin@gmail.com",
    description = "simple calculcator",
    version = VERSION,
    license = "BSD",
    classifiers = CLASSIFIERS,
    packages = find_packages(exclude=['scripts']),
    scripts = ['scripts/calculator'],
    entry_points={
    'console_scripts': [
        'calculator_script=calculator.command_line:main',
        'calculator_script1=scripts.command_line:main',
        ],
    },
    #ext_modules=cythonize(extension),
    #include_package_data = True,
    package_data={'': ['*.txt', 'README', 'data/*'],
                  },
    exclude_package_data={'': ['README']},
)