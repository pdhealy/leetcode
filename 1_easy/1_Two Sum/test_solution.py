import unittest
from solution import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1 from main.py
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected)

    def test_example2(self):
        # Example 2 from main.py
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()