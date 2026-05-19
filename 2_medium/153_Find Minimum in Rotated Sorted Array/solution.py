from typing import List

class Solution:

    # Solution 1: NeetCode
    def findMin2(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if l is less than r, the subarray is already sorted, so can update the result and break out of the loop
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # floor division to round down to the nearest integer (e.g., 5 // 2 = 2)
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

    # Solution 2: Optimized
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]