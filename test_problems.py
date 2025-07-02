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

def test_largest_subsequent_difference_basic(problems):
    nums_list = [2, 5, 8, 1, 9, 3, 7]
    assert problems.largest_subsequent_difference(nums_list) == 8  # 9 - 1

def test_largest_subsequent_difference_sorted(problems):
    nums_list = [1, 2, 3, 4, 5]
    assert problems.largest_subsequent_difference(nums_list) == 1  # 2 - 1, 3 - 2, etc.

def test_largest_subsequent_difference_negative(problems):
    nums_list = [-10, -3, -1, -20]
    assert problems.largest_subsequent_difference(nums_list) == 19  # -1 - (-20)

def test_largest_subsequent_difference_single_element(problems):
    nums_list = [5]
    assert problems.largest_subsequent_difference(nums_list) == 0  # No pairs

def test_largest_subsequent_difference_empty(problems):
    nums_list = []
    assert problems.largest_subsequent_difference(nums_list) == 0  # No pairs

def test_best_time_to_buy_and_sell_stock_basic(problems):
    prices = [7, 1, 5, 3, 6, 4]
    assert problems.best_time_to_buy_and_sell_stock(prices) == 5  # Buy at 1, sell at 6

def test_best_time_to_buy_and_sell_stock_no_profit(problems):
    prices = [7, 6, 4, 3, 1]
    assert problems.best_time_to_buy_and_sell_stock(prices) == 0  # No profit possible

def test_best_time_to_buy_and_sell_stock_single_day(problems):
    prices = [5]
    assert problems.best_time_to_buy_and_sell_stock(prices) == 0  # Only one price

def test_best_time_to_buy_and_sell_stock_empty(problems):
    prices = []
    assert problems.best_time_to_buy_and_sell_stock(prices) == 0  # No prices

def test_best_time_to_buy_and_sell_stock_multiple_profits(problems):
    prices = [2, 4, 1, 10]
    assert problems.best_time_to_buy_and_sell_stock(prices) == 9  # Buy at 1, sell at 10