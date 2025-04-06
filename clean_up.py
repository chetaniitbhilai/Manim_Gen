import os
import shutil

# File extensions to delete
file_extensions = ['.pdf', '.aux', '.log']

# Directory names to delete
dirs_to_delete = ['videos', 'chunks', '__pycache__']

def delete_files_with_extensions(extensions):
    for file in os.listdir('.'):
        if any(file.endswith(ext) for ext in extensions):
            try:
                os.remove(file)
                print(f"Deleted file: {file}")
            except Exception as e:
                print(f"Could not delete file {file}: {e}")

def delete_directories(dir_names):
    for dir_name in dir_names:
        if os.path.isdir(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"Deleted directory: {dir_name}")
            except Exception as e:
                print(f"Could not delete directory {dir_name}: {e}")

if __name__ == '__main__':
    delete_files_with_extensions(file_extensions)
    delete_directories(dirs_to_delete)
