
import pytest

@pytest.fixture()
def tmpfile():
    with open("tmp_fixture.txt", "w") as f:
        yield f

def test_file(tmpfile):
    print(dir(tmpfile))
    tmpfile.write("temporary file : " + tmpfile.name)
    assert True