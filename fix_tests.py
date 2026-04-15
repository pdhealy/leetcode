import os
import sys

def main():
    base_dir = "/home/pdlhealy/workspace/leetcode/2_medium"
    directories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    for d in directories:
        dir_path = os.path.join(base_dir, d)
        
        # 1. create __init__.py
        init_path = os.path.join(dir_path, "__init__.py")
        if not os.path.exists(init_path):
            with open(init_path, "w") as f:
                pass
                
        # 2. fix test_solution.py path issues
        test_path = os.path.join(dir_path, "test_solution.py")
        if os.path.exists(test_path):
            with open(test_path, "r") as f:
                content = f.read()
            
            if "sys.path.append(os.path.dirname(os.path.abspath(__file__)))" not in content:
                new_lines = [
                    "import sys\n",
                    "import os\n",
                    "sys.path.append(os.path.dirname(os.path.abspath(__file__)))\n"
                ]
                # Insert at the beginning
                content = "".join(new_lines) + content
                with open(test_path, "w") as f:
                    f.write(content)

if __name__ == "__main__":
    main()
