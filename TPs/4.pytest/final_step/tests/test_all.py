import os
import splinart as spl
import numpy as np
import json
import pytest
import filecmp

@pytest.fixture()
def datadir(request):
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)
    return test_dir

@pytest.fixture(params=["circle.json"])
def load_json(datadir, request):
    tmp = json.loads(open(datadir + '/' + request.param).read())
    return datadir, tmp

@pytest.mark.long
def test_case(tmpdir, load_json):

    datadir, js = load_json
    np.random.seed(js["seed"])

    img_size, channels = 1000, 4
    img = np.ones((img_size, img_size, channels), dtype=np.float32)

    theta, path = spl.circle(js["center"], js["radius"])

    def xs_func():
        nsamples = 500
        return (np.random.random() + 2 * np.pi * np.linspace(0, 1, nsamples))%(2*np.pi)

    spl.update_img(img, path, xs_func, nrep=js["nrep"], x=theta)

    spl.save_img(img, tmpdir.dirname, 'output.png')

    assert filecmp.cmp(tmpdir.dirname + '/output.png', datadir + "/" + js["output"]) 