from functools import wraps

import os
import shutil
import inspect
import tempfile

import pytest

def pytest_addoption(parser):
    group = parser.getgroup("numpy npz comparison")
    group.addoption('--npz', action='store_true',
                    help="Enable comparison of npz files to reference files")
    group.addoption('--npz-build-reference',
                    help="generate reference npz files in reference directory, relative "
                    "to location where pytest is run", action='store_true')

def pytest_configure(config):
    if config.getoption("--npz") or config.getoption("--npz-build-reference") is not None:
        if config.getoption("--npz-build-reference"):
            is_build_ref = True
        else:
            is_build_ref = False
        config.pluginmanager.register(NpzComparison(config, is_build_ref))

    config.addinivalue_line(
        "markers", "npz_compare: compare npz files"
    )

class NpzComparison(object):

    def __init__(self, config, is_build_ref):
        self.config = config
        self.is_build_ref = is_build_ref

    def pytest_runtest_setup(self, item):
        import numpy as np

        compare = item.get_closest_marker('npz_compare')

        if compare is None:
            return

        original = item.function

        @wraps(item.function)
        def item_function_wrapper(*args, **kwargs):

            reference_dir = os.path.join(os.path.dirname(item.fspath.strpath), 'reference')

            # Run test and get arrays
            if inspect.ismethod(original):  # method
                output = original.__func__(*args, **kwargs)
            else:  # function
                output = original(*args, **kwargs)

            # Find test name to use as npz name
            filename = compare.kwargs.get('filename', None)
            if filename is None:
                filename = item.name + '.npz'
                filename = filename.replace('[', '_').replace(']', '_')
                filename = filename.replace('/', '_')
                filename = filename.replace('_.npz', '.npz')

            # What we do now depends on whether we are generating the
            # reference npz files or simply running the test.
            if not self.is_build_ref:

                # Find path to reference npz
                npz_ref_file = os.path.abspath(os.path.join(os.path.dirname(item.fspath.strpath), reference_dir, filename))

                if not os.path.exists(npz_ref_file):
                    pytest.fail(f"npz file not found for comparison test in: "
                                "\n\t{reference_dir}"
                                "\n(This is expected for new tests.)\n", pytrace=False)

                ref_data = np.load(npz_ref_file)
                rel = compare.kwargs.get('rel', 1e-5)
                for i in range(len(ref_data.files)):
                    assert output[i] == pytest.approx(ref_data[f'arr_{i}'], rel=rel)
            else:
                if not os.path.exists(reference_dir):
                    os.makedirs(reference_dir)

                npz_file = os.path.abspath(os.path.join(reference_dir, filename))
                np.savez(npz_file, *output)
                pytest.skip("Skipping test, since generating data")

        if item.cls is not None:
            setattr(item.cls, item.function.__name__, item_function_wrapper)
        else:
            item.obj = item_function_wrapper