from solution import KthLargest

if __name__ == "__main__":

    # Example 1:

    print("Example 1:")
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))  # return 4
    print(kthLargest.add(5))  # return 5
    print(kthLargest.add(10)) # return 5
    print(kthLargest.add(9))  # return 8
    print(kthLargest.add(4))  # return 8

    # Example 2:

    print("\nExample 2:")
    kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
    print(kthLargest.add(2))  # return 7
    print(kthLargest.add(10)) # return 7
    print(kthLargest.add(9))  # return 7
    print(kthLargest.add(9))  # return 8