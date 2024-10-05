import os
from pathlib import Path

# Function to upload and list project files
def list_project_files(upload_directory):
    files = []
    for root, dirs, filenames in os.walk(upload_directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files
