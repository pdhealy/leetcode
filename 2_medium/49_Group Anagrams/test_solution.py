import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution

def test_groupAnagrams_1():
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    
    if hasattr(solution, "groupAnagrams_fast"):
        output = solution.groupAnagrams_fast(strs)
        assert sorted([sorted(g) for g in output]) == sorted([sorted(g) for g in expected])
        
    if hasattr(solution, "groupAnagrams_complex"):
        output = solution.groupAnagrams_complex(strs)
        assert sorted([sorted(g) for g in output]) == sorted([sorted(g) for g in expected])

def test_groupAnagrams_2():
    solution = Solution()
    strs = [""]
    expected = [[""]]
    
    if hasattr(solution, "groupAnagrams_fast"):
        output = solution.groupAnagrams_fast(strs)
        assert sorted([sorted(g) for g in output]) == sorted([sorted(g) for g in expected])

def test_groupAnagrams_3():
    solution = Solution()
    strs = ["a"]
    expected = [["a"]]
    
    if hasattr(solution, "groupAnagrams_fast"):
        output = solution.groupAnagrams_fast(strs)
        assert sorted([sorted(g) for g in output]) == sorted([sorted(g) for g in expected])
