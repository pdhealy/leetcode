import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_isPalindrome_1():
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    if hasattr(solution, "isPalindromeShort"):
        assert solution.isPalindromeShort(s) == True
    if hasattr(solution, "isPalindromeLong"):
        assert solution.isPalindromeLong(s) == True

def test_isPalindrome_2():
    solution = Solution()
    s = "race a car"
    if hasattr(solution, "isPalindromeShort"):
        assert solution.isPalindromeShort(s) == False
    if hasattr(solution, "isPalindromeLong"):
        assert solution.isPalindromeLong(s) == False

def test_isPalindrome_3():
    solution = Solution()
    s = " "
    if hasattr(solution, "isPalindromeShort"):
        assert solution.isPalindromeShort(s) == True
    if hasattr(solution, "isPalindromeLong"):
        assert solution.isPalindromeLong(s) == True
