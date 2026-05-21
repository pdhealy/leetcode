from solution import Solution
from solution import ListNode

if __name__ == "__main__":

    solution = Solution()

    # Function to print the merged linked list
    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

    # Example 1:

    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged_list = solution.mergeTwoLists(list1, list2)

    print_list(merged_list)

    # Example 2:
    list1 = ListNode()
    list2 = ListNode()
    merged_list = solution.mergeTwoLists(list1, list2)
    print_list(merged_list)