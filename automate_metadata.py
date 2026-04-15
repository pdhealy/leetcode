import os
import re

base_dir = '/home/pdlhealy/workspace/leetcode/2_medium/'

for root, dirs, files in os.walk(base_dir):
    if 'main.py' in files and 'README.md' in files:
        main_py_path = os.path.join(root, 'main.py')
        readme_path = os.path.join(root, 'README.md')
        
        with open(main_py_path, 'r', encoding='utf-8') as f:
            main_py_content = f.read()
            
        metadata = {}
        
        # Define patterns - capture trailing newline to remove the whole line
        patterns = {
            'Difficulty': re.compile(r'^##\s*Difficulty:\s*(.*)$', re.MULTILINE | re.IGNORECASE),
            'Category': re.compile(r'^##\s*(?:Category|Problem Type):\s*(.*)$', re.MULTILINE | re.IGNORECASE),
            'Link': re.compile(r'^##\s*(?:Link|URL):\s*(.*)$', re.MULTILINE | re.IGNORECASE),
            'Tutorial': re.compile(r'^##\s*Tutorial:\s*(.*)$', re.MULTILINE | re.IGNORECASE),
        }
        
        # Extract metadata
        for key, pattern in patterns.items():
            match = pattern.search(main_py_content)
            if match:
                metadata[key] = match.group(1).strip()
        
        if not metadata:
            continue
            
        # Patterns for removal (includes trailing optional newline and any leading spaces on that line if any, but we know it's ^##)
        remove_patterns = [
            re.compile(r'^##\s*Difficulty:\s*.*$\n?', re.MULTILINE | re.IGNORECASE),
            re.compile(r'^##\s*(?:Category|Problem Type):\s*.*$\n?', re.MULTILINE | re.IGNORECASE),
            re.compile(r'^##\s*(?:Link|URL):\s*.*$\n?', re.MULTILINE | re.IGNORECASE),
            re.compile(r'^##\s*Tutorial:\s*.*$\n?', re.MULTILINE | re.IGNORECASE),
        ]
        
        # Remove matching lines
        new_main_py_content = main_py_content
        for pattern in remove_patterns:
            new_main_py_content = pattern.sub('', new_main_py_content)
            
        # Clean up empty line gaps left behind.
        # This replaces 3 or more consecutive newlines with exactly 2 (which is one blank line).
        # We can also handle the case where the lines were at the very beginning of the file.
        # Let's remove any spaces on blank lines first
        new_main_py_content = re.sub(r'^[ \t]+$', '', new_main_py_content, flags=re.MULTILINE)
        # Then replace multiple blank lines with at most one blank line
        new_main_py_content = re.sub(r'\n{3,}', '\n\n', new_main_py_content)
        # If it left blank lines at the start of the file, remove them
        new_main_py_content = new_main_py_content.lstrip('\n')
        
        # Write back main.py
        with open(main_py_path, 'w', encoding='utf-8') as f:
            f.write(new_main_py_content)
            
        # Format metadata
        metadata_lines = []
        if 'Difficulty' in metadata:
            metadata_lines.append(f"- **Difficulty:** {metadata['Difficulty']}")
        if 'Category' in metadata:
            metadata_lines.append(f"- **Category:** {metadata['Category']}")
        if 'Link' in metadata:
            metadata_lines.append(f"- **Link:** {metadata['Link']}")
        if 'Tutorial' in metadata:
            metadata_lines.append(f"- **Tutorial:** {metadata['Tutorial']}")
            
        metadata_block = '\n'.join(metadata_lines) + '\n'
        
        # Update README.md
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_lines = f.readlines()
            
        new_readme_lines = []
        inserted = False
        for line in readme_lines:
            new_readme_lines.append(line)
            if not inserted and line.startswith('# '):
                new_readme_lines.append('\n' + metadata_block)
                inserted = True
                
        # Write back README.md
        if inserted:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.writelines(new_readme_lines)

print("Done")
