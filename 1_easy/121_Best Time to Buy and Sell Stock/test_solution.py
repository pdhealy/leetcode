import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_maxProfit():
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 5
