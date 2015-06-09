import pytest


@pytest.mark.xfail
def test_xfail():
    assert 'Python 2' > 'Python 3'
