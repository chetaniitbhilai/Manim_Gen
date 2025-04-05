import os
import shutil

# Directories to clean
UPLOAD_FOLDER = 'media/uploads'
PROCESSED_FOLDER = 'media/videos'
CHUNKS_FOLDER = 'chunks'
MANIM_GENERATED_FOLDER = 'manim_generated'

def clean_directories():
    """Removes all generated files and resets the workspace."""
    for folder in [UPLOAD_FOLDER, PROCESSED_FOLDER, CHUNKS_FOLDER, MANIM_GENERATED_FOLDER]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder, exist_ok=True)

if __name__ == "__main__":
    clean_directories()
    print("Cleanup completed.")
