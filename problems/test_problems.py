import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from problems.problems import Problems

import pytest

@pytest.fixture
def problems():
    return Problems()

def test_return_true(problems):
    assert problems.returnTrue() == True