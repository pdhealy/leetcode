import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_lengthOfLongestSubstring_1():
    solution = Solution()
    s = "abcabcbb"
    assert solution.lengthOfLongestSubstring(s) == 3

def test_lengthOfLongestSubstring_2():
    solution = Solution()
    s = "bbbbb"
    assert solution.lengthOfLongestSubstring(s) == 1

def test_lengthOfLongestSubstring_3():
    solution = Solution()
    s = "pwwkew"
    assert solution.lengthOfLongestSubstring(s) == 3
