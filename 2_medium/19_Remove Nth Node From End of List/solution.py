from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Solution 1 (NeetCode)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right: # right n steps ahead of left, so gap between left and right is n nodes
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        
        # delete
        left.next = left.next.next
        return dummy.next # returns the node after the dummy (0) node, which is the head of the modified list.


    # Solution 2 (Greg Hogg)
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n + 1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next
        return dummy.next