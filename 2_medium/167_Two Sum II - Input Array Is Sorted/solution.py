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