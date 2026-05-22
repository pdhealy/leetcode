from solution import Solution
from solution import ListNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    print(solution.reorderList(head))

    # Example 2:

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print(solution.reorderList(head))