from solution import MedianFinder

if __name__ == "__main__":
    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()

    # Example 1:

    obj.addNum(1)
    obj.addNum(2)
    print(f"Example 1 (findMedian 1): {obj.findMedian()}")
    obj.addNum(3)
    print(f"Example 1 (findMedian 2): {obj.findMedian()}")