# LeetCode Practice

A personal repository for solving and documenting [LeetCode](https://leetcode.com/) problems, focusing on data structures and algorithms mastery.

## 📖 About

This workspace serves as a structured environment for:
- **Algorithm Practice**: Implementing solutions to LeetCode problems across varying difficulty levels
- **Self-Study**: Tracking learning progress and solution approaches
- **Local Testing**: Debugging and validating solutions before submission

## 📁 Repository Structure

Problems are organized by difficulty level:

```
leetcode/
├── 1_easy/          # Easy difficulty problems
├── 2_medium/        # Medium difficulty problems
└── 3_hard/          # Hard difficulty problems
```

### Problem Folder Structure

Each problem directory follows a consistent layout:

```
<problem_number>_<problem_name>/
├── solution.py      # Solution implementation (Solution class)
├── main.py          # Test runner with example test cases
└── README.md        # Problem description and notes (optional)
```

## 🚀 Usage

### Running a Solution

Navigate to any problem directory and execute the main script:

```bash
cd 2_medium/49_Group\ Anagrams/
python3 main.py
```

### Structure of Solution Files

**solution.py** - Contains the `Solution` class:
```python
class Solution:
    def problemMethod(self, param):
        # Implementation here
        pass
```

**main.py** - Imports and tests the solution:
```python
from solution import Solution

if __name__ == "__main__":
    solution = Solution()
    result = solution.problemMethod(test_input)
    print(result)
```

## 🛠️ Technologies

- **Language**: Python 3
- **Focus Areas**: Arrays, Strings, Hash Tables, Trees, Graphs, Dynamic Programming, and more

## 📝 Notes

- Solutions may include multiple approaches (brute force, optimized, etc.)
- Time and space complexity analysis included where applicable
- Comments explain key algorithmic decisions

## 🤝 Contributing

This is a personal learning repository. Feel free to fork and use the structure for your own practice!

## 📄 License

This project is open source and available for educational purposes.
