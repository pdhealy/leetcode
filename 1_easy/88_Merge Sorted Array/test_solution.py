import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import pytest
from solution import Solution

def test_solution():
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]

def test_example2():
    solution = Solution()
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]

def test_example3():
    solution = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]
