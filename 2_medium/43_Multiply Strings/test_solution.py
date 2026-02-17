import unittest
from solution import Solution

class TestMultiplyStrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1 from main.py
        num1 = "2"
        num2 = "3"
        expected = "6"
        result = self.solution.multiply(num1, num2)
        self.assertEqual(result, expected)

    def test_example2(self):
        # Example 2 from main.py (commented out in main.py, but included for completeness)
        num1 = "123"
        num2 = "456"
        expected = "56088"
        result = self.solution.multiply(num1, num2)
        self.assertEqual(result, expected)

    def test_custom(self):
        # Custom example from main.py
        num1 = "12"
        num2 = "34"
        expected = "408"
        result = self.solution.multiply(num1, num2)
        self.assertEqual(result, expected)

    def test_zero(self):
        # Edge case: one number is zero
        num1 = "0"
        num2 = "12345"
        expected = "0"
        result = self.solution.multiply(num1, num2)
        self.assertEqual(result, expected)

        num1 = "6789"
        num2 = "0"
        expected = "0"
        result = self.solution.multiply(num1, num2)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
