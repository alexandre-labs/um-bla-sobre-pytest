import sys


import pytest


def should_skip():
    return True


@pytest.mark.skipif('should_skip()')  # shou_skip() is True
def test_skipif():

    phrase = 'should skip'

    assert phrase == 'foo'


@pytest.mark.skipif("sys.version_info.major > 2")
def test_skipif_python3():

   assert 1 == 2
