# Function to save generated content to markdown files
from pathlib import Path

def save_markdown(output_directory, readme_content, documentation_content):
    with open(Path(output_directory) / 'README.md', 'w') as readme_file:
        readme_file.write(readme_content)

    with open(Path(output_directory) / 'DOCUMENTATION.md', 'w') as doc_file:
        doc_file.write(documentation_content)
