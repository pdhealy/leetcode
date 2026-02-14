# 167: Two Sum II - Input Array Is Sorted

## Difficulty: Medium
## Category: Array, Two Pointers
## Problem Type: Array, Two Pointers
### Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
## Tutorial: https://www.youtube.com/watch?v=cQ1Oz4ckceM

## Time complexity: O(n)
## Space complexity: O(1)

## Solution:

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        # Use 'len() - 1' to get the index of the last element
        left_ptr, right_ptr = 0, len(numbers) - 1

        # Iterate until the two pointers meet
        while left_ptr < right_ptr:
            # Calculate the current sum of the two pointers
            curSum = numbers[left_ptr] + numbers[right_ptr]

            # Move pointers based on comparison with target
            if curSum > target:
                right_ptr -= 1
            elif curSum < target:
                left_ptr += 1
            # If curSum equals target, return the 1-based (not 0-based) indices
            else:
                return [left_ptr + 1, right_ptr + 1]
            
        return []
    
## Test cases:

if __name__ == "__main__":

    solution = Solution()

    # numbers = [2, 7, 11, 15] # LeetCode example
    
    numbers = [1, 3, 4, 5, 7, 10, 11] # Neetcode example - more comprehensive
    target = 9

    result = solution.twoSum(numbers, target)
    print(f"The indices of the two numbers that add up to {target} are: {result}")