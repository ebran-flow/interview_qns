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

def test_find_itinerary_example1(problems):
    tickets = [
        ["New York", "Washington"],
        ["Seattle", "Memphis"],
        ["Hawaii", "New York"],
        ["Memphis", "Hawaii"]
    ]
    expected = ["Seattle", "Memphis", "Hawaii", "New York", "Washington"]
    assert problems.find_itinerary(tickets) == expected

def test_find_itinerary_example2(problems):
    tickets = [
        ["Mumbai", "Delhi"],
        ["Delhi", "Kolkata"]
    ]
    expected = ["Mumbai", "Delhi", "Kolkata"]
    assert problems.find_itinerary(tickets) == expected

def test_find_itinerary_single_ticket(problems):
    tickets = [
        ["A", "B"]
    ]
    expected = ["A", "B"]
    assert problems.find_itinerary(tickets) == expected