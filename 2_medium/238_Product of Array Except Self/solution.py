from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1s to hold the products
        res = [1] * (len(nums))
        # Initialize prefix product to 1 to calculate the product of elements to the left of the current index
        prefix = 1

        # Calculate the product of elements to the left of the current index and store it in the result array
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1

        # Calculate the product of elements to the right of the current index and multiply it with the existing value in the result array
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res