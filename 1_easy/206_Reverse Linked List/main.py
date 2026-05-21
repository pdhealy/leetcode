from solution import Solution
from solution import ListNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(solution.reverseList(head))  # Output: [5,4,3,2,1]

    # Example 2:
    head = ListNode(1, ListNode(2))
    print(solution.reverseList(head))  # Output: [2,1]

    # Example 3:
    head = None
    print(solution.reverseList(head))  # Output: []