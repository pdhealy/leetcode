# 21: Merge Two Sorted Lists

from solution import Solution
if __name__ == "__main__":

    solution = Solution()

    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged_list = solution.mergeTwoLists(list1, list2)  # Insert breakpoint here and start debugging

    # Function to print the merged linked list
    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

    print_list(merged_list)