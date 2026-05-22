from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None # chained assignment; sets slow.next to None cutting the list in half.
        while second: # same pattern as `206. Reverse Linked List``
            tmp = second.next
            second.next = prev
            prev = second # prev stores head of reversed list
            second = tmp

        # merge two halves
        first, second = head, prev
        while second: # only need to check second because it can be shorter than first.
            tmp1, tmp2 = first.next, second.next
            first.next = second # links current node from first half to current node from second half
            second.next = tmp1
            first, second = tmp1, tmp2

        return head
