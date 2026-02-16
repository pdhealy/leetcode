import unittest
from solution import Solution

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_group_anagrams_example1(self):
        # Example 1 from main.py
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [
            ["bat"],
            ["nat", "tan"],
            ["ate", "eat", "tea"]
        ]
        # Since order of groups and order within groups does not matter, sort for comparison
        result = self.solution.groupAnagrams_complex(strs)
        self.assertCountEqual([sorted(group) for group in result], [sorted(group) for group in expected])
        result_fast = self.solution.groupAnagrams_fast(strs)
        self.assertCountEqual([sorted(group) for group in result_fast], [sorted(group) for group in expected])

if __name__ == "__main__":
    unittest.main()
