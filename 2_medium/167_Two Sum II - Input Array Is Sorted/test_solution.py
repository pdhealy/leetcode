import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_twoSum_1():
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(numbers, target) == [1, 2]

def test_twoSum_2():
    solution = Solution()
    numbers = [1, 3, 4, 5, 7, 10, 11]
    target = 9
    assert solution.twoSum(numbers, target) == [3, 4]
