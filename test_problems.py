import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from problems import Problems

import pytest

@pytest.fixture
def problems():
    return Problems()

def test_true_case(problems):
    assert problems.send_back_true() == True

