import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_moveZeros_1():
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    output = solution.moveZeros(nums)
    if output is not None:
        assert output == [1, 3, 12, 0, 0]
    else:
        assert nums == [1, 3, 12, 0, 0]

def test_moveZeros_2():
    solution = Solution()
    nums = [0]
    output = solution.moveZeros(nums)
    if output is not None:
        assert output == [0]
    else:
        assert nums == [0]
