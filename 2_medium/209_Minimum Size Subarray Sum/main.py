# 209. Minimum Size Subarray Sum

## Difficulty: Medium
## Category: Sliding Window
### Link: https://leetcode.com/problems/minimum-size-subarray-sum
## Tutorial: https://www.youtube.com/watch?v=aYqYMIqZx5s

## Solution

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Initialize the left pointer and total sum
        left_ptr: int = 0
        total: int = 0
        # Initialize the result to infinity, which will be updated with the minimum length of the subarray
        result: float = float("inf")

        # Iterate through the array with the right pointer
        for right_ptr in range(len(nums)):
            # Add the current number to the total sum
            total += nums[right_ptr]
            # While the total sum is greater than or equal to the target, update the result and move the left pointer
            
            while total >= target:
                result = min(right_ptr - left_ptr + 1, result)
                # Subtract the number at the left pointer from the total sum (because the total sum is already greater than or equal to the target - we want it to be less than or equal to the target) and move the left pointer to the right.
                total -= nums[left_ptr]
                left_ptr += 1

        # If the result is still infinity, it means no valid subarray was found, so return 0. Otherwise, return the result.
        return 0 if result == float("inf") else result # type: ignore
    
## Test Cases

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    # target = 7
    # nums = [2,3,1,2,4,3]
    # assert solution.minSubArrayLen(target, nums) == 2

    # Example 2:
    target = 4
    nums = [1,4,4]

    # Example 3:
    # target = 11
    # nums = [1,1,1,1,1,1,1,1]

    output = solution.minSubArrayLen(target, nums)
    print(f"The minimum size of a contiguous subarray of which the sum is at least {target} is: {output}")