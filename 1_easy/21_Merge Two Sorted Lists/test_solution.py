import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
if "solution" in sys.modules: del sys.modules["solution"]
from solution import Solution, ListNode

def list_to_array(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

def test_mergeTwoLists():
    solution = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged_list = solution.mergeTwoLists(list1, list2)
    assert list_to_array(merged_list) == [1, 1, 2, 3, 4, 4]
