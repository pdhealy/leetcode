from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize result with the maximum number in the array to handle cases where all numbers are negative or zero, ensuring we return the correct maximum product even if it's a single element
        result = max(nums)
        # Initialize current minimum and maximum product to 1 so that they don't affect the product calculation initially (i.e., 1 is the multiplicative identity)
        curMin, curMax = 1, 1

        for n in nums:
            # Edge case: reset when n is 0 because any product involving 0 will be 0, and we need to start fresh for the next subarray
            if n == 0:
                # Reset current min and max product
                curMin, curMax = 1, 1
                # Guard Clause to reduce indentation below
                continue

            # Store current max before updating it to use for curMin calculation
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            # Update result with the maximum product found so far
            result = max(result, curMax)

        return result