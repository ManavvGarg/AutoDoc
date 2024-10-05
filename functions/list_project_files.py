import os

# Function to upload and list project files, skipping node_modules
def list_project_files(upload_directory):
    files = []
    for root, dirs, filenames in os.walk(upload_directory):
        # Skip the node_modules folder
        if 'node_modules' in dirs:
            dirs.remove('node_modules')  # This prevents os.walk from going into node_modules

        # Add the files to the list
        for filename in filenames:
            files.append(os.path.join(root, filename))
    
    return files
