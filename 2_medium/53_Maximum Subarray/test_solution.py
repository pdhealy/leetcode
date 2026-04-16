import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_maxSubArray_1():
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert solution.maxSubArray(nums) == 6

def test_maxSubArray_2():
    solution = Solution()
    nums = [1]
    assert solution.maxSubArray(nums) == 1

def test_maxSubArray_3():
    solution = Solution()
    nums = [5, 4, -1, 7, 8]
    assert solution.maxSubArray(nums) == 23
