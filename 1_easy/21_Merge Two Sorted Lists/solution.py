class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val # Intialized as 0 by default
        self.next = next # Intialized as None by default

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create an empty placeholder (dummy) node so that the list is not initially empty
        dummy = ListNode()
        # Set a tail pointer to keep track of the end of the merged list
        tail = dummy

        # Iterate while both lists have nodes
        while l1 and l2:
            # Check if the value in l1 is less than that in l2
            if l1.val < l2.val:
                # If so, append l1's node to the merged list
                tail.next = l1
                # Move l1 to its next node
                l1 = l1.next
            # If l2's value is less than or equal to l1's
            else:
                # Append l2's node to the merged list
                tail.next = l2
                # Move l2 to its next node
                l2 = l2.next
            # Move the tail pointer to the end of the merged list
            tail = tail.next

        # Handles edge cases where one list is longer than the other
        # If l1 still has nodes, append them
        if l1:
            tail.next = l1
        # If l2 still has nodes, append them
        elif l2:
            tail.next = l2

        return dummy.next