from pathlib import Path

def create_project_structure():
    base_path = Path.cwd()  # Use the current working directory
    
    # Define folder structure
    folders = ["data", "notebooks", "scripts", "reports", "docs"]
    files = ["README.md", "requirements.txt", ".gitignore", "LICENSE"]
    
    # Create folders
    for folder in folders:
        (base_path / folder).mkdir(parents=True, exist_ok=True)
    
    # Create empty files
    for file in files:
        (base_path / file).touch()
    
    print(f"Project structure created inside {base_path}")

# Run the function
create_project_structure()