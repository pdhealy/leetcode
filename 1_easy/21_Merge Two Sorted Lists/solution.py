# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode() # head = 0, head.next = None
        tail = dummy # track end of merged list, starting from the dummy node

        while l1 and l2: # checks that l1 and l2 are not None
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Handles edge cases where one list is longer than the other
        # If l1 still has nodes, append them
        if l1:
            tail.next = l1
        # If l2 still has nodes, append them
        elif l2:
            tail.next = l2

        return dummy.next