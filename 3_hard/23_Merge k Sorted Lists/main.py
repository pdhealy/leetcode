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

    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
             ]
    
    merged_list = solution.mergeKLists(lists)
    print_list(merged_list)


    # Example 2:

    lists = [] # list is empty or None
    merged_list = solution.mergeKLists(lists)
    print_list(merged_list)  # Should print "None"


    # Example 3:

    lists = [ListNode(0)]
    merged_list = solution.mergeKLists(lists)
    print_list(merged_list)  # Should print "0 -> None"