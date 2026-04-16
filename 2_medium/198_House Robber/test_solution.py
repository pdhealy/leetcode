import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_rob_1():
    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    assert solution.rob(nums) == 12
