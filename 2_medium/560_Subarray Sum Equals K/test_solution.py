import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_subarraySum_1():
    solution = Solution()
    nums = [1, 1, 1]
    k = 2
    assert solution.subarraySum(nums, k) == 2

def test_subarraySum_2():
    solution = Solution()
    nums = [1, 2, 3]
    k = 3
    assert solution.subarraySum(nums, k) == 2

def test_subarraySum_3():
    solution = Solution()
    nums = [1, 2, -1, 3]
    k = 3
    assert solution.subarraySum(nums, k) == 2
