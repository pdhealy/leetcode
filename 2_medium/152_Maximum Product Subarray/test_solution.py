import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_maxProduct_1():
    solution = Solution()
    nums = [2, 3, -2, 4]
    assert solution.maxProduct(nums) == 6

def test_maxProduct_2():
    solution = Solution()
    nums = [-2, 0, -1]
    assert solution.maxProduct(nums) == 0

def test_maxProduct_3():
    solution = Solution()
    nums = [-2, 3, -4]
    assert solution.maxProduct(nums) == 24
