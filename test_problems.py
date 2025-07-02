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

def test_reverse_number_pattern_5(problems):
    expected = [
        "5 4 3 2 1",
        "4 3 2 1",
        "3 2 1",
        "2 1",
        "1"
    ]
    assert problems.reverse_number_pattern(5) == expected

def test_reverse_number_pattern_3(problems):
    expected = [
        "3 2 1",
        "2 1",
        "1"
    ]
    assert problems.reverse_number_pattern(3) == expected

def test_reverse_number_pattern_1(problems):
    expected = [
        "1"
    ]
    assert problems.reverse_number_pattern(1) == expected