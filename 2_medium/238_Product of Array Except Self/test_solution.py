import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_productExceptSelf_1():
    solution = Solution()
    nums = [1, 2, 3, 4]
    assert solution.productExceptSelf(nums) == [24, 12, 8, 6]

def test_productExceptSelf_2():
    solution = Solution()
    nums = [-1, 1, 0, -3, 3]
    assert solution.productExceptSelf(nums) == [0, 0, 9, 0, 0]
