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