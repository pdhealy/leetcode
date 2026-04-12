# 21: Merge Two Sorted Lists

## Category: Easy
## Problem Type: Linked List, Recursion
## Link: https://leetcode.com/problems/merge-two-sorted-lists/
## Tutorial: https://www.youtube.com/watch?v=XIdigk956u0&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=6&pp=iAQB

# Approach: Iterative Merging
# Time complexity: O(n + m)
# Space complexity: O(1)


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