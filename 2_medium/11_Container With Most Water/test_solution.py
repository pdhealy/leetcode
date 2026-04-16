import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_maxArea_1():
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solution.maxArea(height) == 49

def test_maxArea_2():
    solution = Solution()
    height = [1, 1]
    assert solution.maxArea(height) == 1
