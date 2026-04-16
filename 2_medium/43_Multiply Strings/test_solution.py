import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_multiply_1():
    solution = Solution()
    num1 = "2"
    num2 = "3"
    assert solution.multiply(num1, num2) == "6"

def test_multiply_2():
    solution = Solution()
    num1 = "123"
    num2 = "456"
    assert solution.multiply(num1, num2) == "56088"

def test_multiply_3():
    solution = Solution()
    num1 = "12"
    num2 = "34"
    assert solution.multiply(num1, num2) == "408"
