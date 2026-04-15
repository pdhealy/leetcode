import os
import re
import requests
import markdownify
import sys

def get_leetcode_description(title_slug):
    url = "https://leetcode.com/graphql/"
    payload = {
        "query": "query questionData($titleSlug: String!) { question(titleSlug: $titleSlug) { title content } }",
        "variables": {"titleSlug": title_slug},
        "operationName": "questionData"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "question" in data["data"] and data["data"]["question"]:
            content = data["data"]["question"]["content"]
            title = data["data"]["question"]["title"]
            if content:
                md_content = markdownify.markdownify(content)
                return f"# {title}\n\n" + md_content
    return None

def main():
    base_dir = "/home/pdlhealy/workspace/leetcode/2_medium"
    directories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    for d in directories:
        dir_path = os.path.join(base_dir, d)
        m = re.match(r'^\d+_(.*)$', d)
        if not m:
            continue
            
        title_raw = m.group(1)
        # Fix for some slugs
        title_slug = title_raw.lower().replace(" ", "-").replace("'", "").replace(",", "")
        
        # known custom fixes
        if title_slug == "remove-duplicate-from-sorted-array":
            title_slug = "remove-duplicates-from-sorted-array"
        if title_slug == "two-sum-ii---input-array-is-sorted":
            title_slug = "two-sum-ii-input-array-is-sorted"
            
        print(f"Processing {d} (slug: {title_slug})")
        
        # 1. Fetch README.md
        readme_path = os.path.join(dir_path, "README.md")
        desc = get_leetcode_description(title_slug)
        if desc:
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(desc)
        else:
            print(f"  -> Failed to fetch README for {title_slug}")

        # 2. Split main.py into solution.py and main.py
        main_path = os.path.join(dir_path, "main.py")
        solution_path = os.path.join(dir_path, "solution.py")
        test_path = os.path.join(dir_path, "test_solution.py")
        
        if not os.path.exists(main_path):
            print(f"  -> main.py not found in {d}")
            continue
            
        with open(main_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        # If main.py already imports from solution, it means it's already split
        already_split = False
        for line in lines:
            if "from solution import Solution" in line:
                already_split = True
                break
                
        if already_split:
            print(f"  -> {d} is already split.")
            # Ensure test_solution exists
            if not os.path.exists(test_path):
                with open(test_path, "w", encoding="utf-8") as f:
                    f.write("import pytest\nfrom solution import Solution\n\ndef test_solution():\n    solution = Solution()\n    assert solution is not None\n")
            continue
            
        imports = []
        headers = []
        solution_code = []
        main_code = []
        
        state = "header"
        for line in lines:
            if line.startswith("class Solution"):
                state = "solution"
                solution_code.append(line)
            elif line.startswith("if __name__ =="):
                state = "main"
                main_code.append(line)
            elif state == "header":
                if line.startswith("import ") or line.startswith("from "):
                    imports.append(line)
                else:
                    headers.append(line)
            elif state == "solution":
                if line.startswith("import ") or line.startswith("from "):
                    imports.append(line)
                elif line.startswith("if __name__ =="):
                    state = "main"
                    main_code.append(line)
                else:
                    solution_code.append(line)
            elif state == "main":
                main_code.append(line)
                
        if solution_code:
            with open(solution_path, "w", encoding="utf-8") as f:
                for imp in imports:
                    f.write(imp)
                if imports:
                    f.write("\n")
                for sol in solution_code:
                    f.write(sol)
                    
            with open(main_path, "w", encoding="utf-8") as f:
                for h in headers:
                    f.write(h)
                f.write("\nfrom solution import Solution\n")
                for imp in imports:
                    f.write(imp)
                if imports:
                    f.write("\n")
                for m in main_code:
                    f.write(m)
                    
        # 3. Create basic test_solution.py
        if not os.path.exists(test_path):
            with open(test_path, "w", encoding="utf-8") as f:
                f.write("import pytest\nfrom solution import Solution\n\ndef test_solution():\n    solution = Solution()\n    assert solution is not None\n")
        else:
            # Check if it's unittest, maybe replace? The prompt says "update them if necessary"
            # It already has a test_solution.py in 1_Two Sum which uses unittest. We can leave it since pytest supports it.
            pass

if __name__ == "__main__":
    main()
