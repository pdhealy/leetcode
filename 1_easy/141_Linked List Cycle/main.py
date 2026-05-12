# 141. Linked List Cycle

from solution import Solution
from solution import ListNode
    
if __name__ == "__main__":

    # Example 1:
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    print(f'Example 1 Result: {Solution().hasCycle(head)}')

    # Example 2:
    head = ListNode(1)
    head.next = head

    print(f'Example 2 Result: {Solution().hasCycle(head)}')

    # Example 3:
    head = ListNode(1)
    head.next = None

    print(f'Example 3 Result: {Solution().hasCycle(head)}')