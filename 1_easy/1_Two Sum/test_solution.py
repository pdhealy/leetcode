import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_twoSum_example1():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1]

def test_twoSum_example2():
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2]
