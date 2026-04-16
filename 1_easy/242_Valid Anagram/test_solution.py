import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_isAnagram1_1():
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    assert solution.isAnagram1(s, t) == True

def test_isAnagram1_2():
    solution = Solution()
    s = "rat"
    t = "car"
    assert solution.isAnagram1(s, t) == False
