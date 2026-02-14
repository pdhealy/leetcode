# 560. Subarray Sum Equals K

## Difficulty: Medium
## Category: Array, Hash Table, Prefix Sum
## Link: https://leetcode.com/problems/subarray-sum-equals-k/
## Tutorial: https://www.youtube.com/watch?v=fFVZt-6sgyo
## Space Complexity: O(N) where N is the length of the input array. This is because we are storing the prefix sums in a hash map, and in the worst case, we may store all prefix sums if they are unique.
## Time Complexity: O(N) where N is the length of the input array. This is because we are iterating through the input array once to calculate the prefix sums and check for the required sums in the hash map.

## Solution:

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize the result variable to store the count of subarrays that sum to k
        result = 0
        # Initialize a variable to keep track of the current prefix sum and a hash map to store the frequency of prefix sums
        prefix_sum = 0
        # Initialize the hash map with a prefix sum of 0 occurring once, to account for subarrays that start from the beginning of the array
        prefix_sum_count = {0: 1}

        # Iterate through each number in the input array
        for num in nums:
            # Update the current prefix sum by adding the current number
            prefix_sum += num
            # Calculate the difference between the current prefix sum and k, which represents the required prefix sum that would make the subarray sum to k
            diff = prefix_sum - k

            # Update result if diff already exists in the hash map, which means there are subarrays that sum to k
            result += prefix_sum_count.get(diff, 0)
            # Update the hash map with the current prefix sum, incrementing its count
            prefix_sum_count[prefix_sum] = 1 + prefix_sum_count.get(prefix_sum, 0)

        return result

## Test cases:

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    # nums = [1, 1, 1]
    # k = 2
    # Output: 2

    # Example 2:
    # nums = [1, 2, 3]
    # k = 3
    # Output: 2

    # Example 3: Custom
    nums = [1, 2, -1, 3]
    k = 3
    # Output: 2

    output = solution.subarraySum(nums, k)
    print(f"The number of subarrays that sum to {k} is: {output}")