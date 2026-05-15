from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # checks if the current value is the same as the previous value, if it is, then skip it to avoid duplicates.
            # Example: [-2, -1, -1, 2, 3], when we find the triplet [-2, -1, 3], we want to skip the second -1 to avoid finding the same triplet again.
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            # check if the left and right pointers to the right of `a` are within the bounds of the array.
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # checks if the current value is the same as the previous value, if it is, then skip it to avoid duplicates.
                    # Example: [-2, -1, -1, 2, 3], when we find the triplet [-2, -1, 3], we want to skip the second -1 to avoid finding the same triplet again.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
