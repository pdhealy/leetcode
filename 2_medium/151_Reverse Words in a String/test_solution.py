import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_reverseWords_1():
    solution = Solution()
    s = "the sky is blue"
    if hasattr(solution, "reverseWords_short"):
        assert solution.reverseWords_short(s) == "blue is sky the"
    elif hasattr(solution, "reverseWords"):
        assert solution.reverseWords(s) == "blue is sky the"

def test_reverseWords_2():
    solution = Solution()
    s = "  hello world  "
    if hasattr(solution, "reverseWords_short"):
        assert solution.reverseWords_short(s) == "world hello"
    elif hasattr(solution, "reverseWords"):
        assert solution.reverseWords(s) == "world hello"

def test_reverseWords_3():
    solution = Solution()
    s = "a good   example"
    if hasattr(solution, "reverseWords_short"):
        assert solution.reverseWords_short(s) == "example good a"
    elif hasattr(solution, "reverseWords"):
        assert solution.reverseWords(s) == "example good a"
