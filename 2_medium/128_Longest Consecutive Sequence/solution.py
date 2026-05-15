from typing import List

class Solution:

    # Neetcode solution
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if it's the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                # check how long the sequence is and update longest
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest

    # Copilot solution
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        longest = 1

        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest
