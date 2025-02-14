import os
from pathlib import Path
from datetime import datetime

def generate_tree(startpath, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = {'.git', '__pycache__', 'health_connect_venv', '.pytest_cache'}
    
    tree = []
    for root, dirs, files in os.walk(startpath):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level)  # Using original Unicode character
        tree.append(f'{indent}├── {os.path.basename(root)}/')  # Using original Unicode characters
        
        subindent = '│   ' * (level + 1)
        for file in sorted(files):
            if not file.startswith('.'):
                tree.append(f'{subindent}├── {file}')  # Using original Unicode characters
    
    return '\n'.join(tree)

def update_structure_doc():
    project_root = Path(__file__).parent
    docs_dir = project_root / 'docs'
    structure_file = docs_dir / 'current_project_structure.md'  # Changed filename
    
    # Generate the new tree structure
    tree = generate_tree(str(project_root))
    
    # Create the new content
    new_content = f"""# Health Connect - Current Project Structure

## Directory Structure as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
```
health_connect/
{tree}
```
"""
    
    # Create or update the file
    docs_dir.mkdir(exist_ok=True)
    with open(structure_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Current project structure saved to current_project_structure.md!")

if __name__ == "__main__":
    update_structure_doc()
