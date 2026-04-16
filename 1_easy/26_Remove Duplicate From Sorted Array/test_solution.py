import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_removeDuplicates_1():
    solution = Solution()
    nums = [1, 1, 2]
    k = solution.removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1, 2]

def test_removeDuplicates_2():
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]
