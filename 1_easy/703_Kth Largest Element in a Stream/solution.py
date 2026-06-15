import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with k largest integers
        # in a heap, smaller elements are always at the root of the heap, so the kth largest element will be at the root of the heap
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) #  heapify transforms list into a heap, in-place, in linear time
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) #  heappop removes and returns smallest element from heap, which is the kth largest element in this case

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #  heappush uses formula k(n) = 2k + 1 for left child and k(n) = 2k + 2 for right child to maintain the heap property
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) #  heappop removes and returns smallest element from heap, which is the kth largest element in this case
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)