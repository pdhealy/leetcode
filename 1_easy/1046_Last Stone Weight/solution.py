from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]  # convert to negative for max-heap behavior. converting to negative means larger values will be "smaller" in the heap
        heapq.heapify(stones)

        while len(stones) > 1:  # loop modifies original `stones`
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)  # add a dummy stone with weight 0 to return 0 if there are no stones left
        return abs(stones[0])