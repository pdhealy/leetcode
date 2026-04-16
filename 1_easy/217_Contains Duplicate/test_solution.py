import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_containsDuplicate_1():
    solution = Solution()
    nums = [1, 2, 3, 1]
    assert solution.containsDuplicate(nums) == True

def test_containsDuplicate_2():
    solution = Solution()
    nums = [1, 2, 3, 4]
    assert solution.containsDuplicate(nums) == False

def test_containsDuplicate_3():
    solution = Solution()
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert solution.containsDuplicate(nums) == True
