import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_minSubArrayLen_1():
    solution = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    assert solution.minSubArrayLen(target, nums) == 2

def test_minSubArrayLen_2():
    solution = Solution()
    target = 4
    nums = [1, 4, 4]
    assert solution.minSubArrayLen(target, nums) == 1

def test_minSubArrayLen_3():
    solution = Solution()
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    assert solution.minSubArrayLen(target, nums) == 0
