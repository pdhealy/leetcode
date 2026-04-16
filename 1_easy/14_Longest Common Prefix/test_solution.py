import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_longestCommonPrefix_1():
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    assert solution.longestCommonPrefix(strs) == "fl"

def test_longestCommonPrefix_2():
    solution = Solution()
    strs = ["dog", "racecar", "car"]
    assert solution.longestCommonPrefix(strs) == ""
