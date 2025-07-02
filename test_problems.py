import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from problems import Problems

import unittest

class TestProblems(unittest.TestCase):
    def setUp(self):
        self.problems = Problems()

    def test_example1(self):
        tickets = [
            ["New York", "Washington"],
            ["Seattle", "Memphis"],
            ["Hawaii", "New York"],
            ["Memphis", "Hawaii"]
        ]
        expected = ["Seattle", "Memphis", "Hawaii", "New York", "Washington"]
        self.assertEqual(self.problems.find_itinerary(tickets), expected)

    def test_example2(self):
        tickets = [
            ["Mumbai", "Delhi"],
            ["Delhi", "Kolkata"]
        ]
        expected = ["Mumbai", "Delhi", "Kolkata"]
        self.assertEqual(self.problems.find_itinerary(tickets), expected)

if __name__ == '__main__':
    unittest.main()