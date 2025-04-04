# import os
# import subprocess
# import shutil

# # Step 1: Run new.py to generate chunks
# # subprocess.run(["python3", "new.py", "input_  file.txt"])

# # Step 2: Define directories
# chunks_dir = "chunks"
# output_base_dir = "manim_generated"
# manim_video_path = "/home/chetan/Documents/gdg_sol/new/Google_hack2skill/manim_flask/media/videos/generated_scene/480p15/GeneratedScene.mp4"

# # Ensure the output base directory exists
# os.makedirs(output_base_dir, exist_ok=True)

# # Step 3: Process each chunk with new2.py
# if os.path.exists(chunks_dir):
#     for i, chunk in enumerate(sorted(os.listdir(chunks_dir)), start=0):
#         chunk_path = os.path.join(chunks_dir, chunk)
        
#         # Run new2.py on the chunk
#         subprocess.run(["python3", "new2.py", chunk_path])

#         # Define the output directory for this chunk
#         chunk_output_dir = os.path.join(output_base_dir, f"chunk_{i}")
#         os.makedirs(chunk_output_dir, exist_ok=True)

#         # Copy the generated Manim video to the chunk directory
#         if os.path.exists(manim_video_path):
#             shutil.copy(manim_video_path, os.path.join(chunk_output_dir, "GeneratedScene.mp4"))
#         else:
#             print(f"Warning: Manim video not found for {chunk_path}")

# else:
#     print(f"Error: Directory '{chunks_dir}' not found. Ensure new.py ran successfully.")

import os
import subprocess
import shutil
import time

# Step 1: Define directories
chunks_dir = "chunks"
output_base_dir = "manim_generated"
manim_video_path = "/home/chetan/Documents/gdg_sol/new/Google_hack2skill/manim_flask/media/videos/generated_scene/480p15/GeneratedScene.mp4"

# Ensure the output base directory exists
os.makedirs(output_base_dir, exist_ok=True)

# Step 2: Process each chunk with new2.py
if os.path.exists(chunks_dir):
    for i, chunk in enumerate(sorted(os.listdir(chunks_dir)), start=0):
        chunk_path = os.path.join(chunks_dir, chunk)
        
        # Try running new2.py once, and retry if it fails
        attempt = 0
        max_attempts = 2
        while attempt < max_attempts:
            result = subprocess.run(["python3", "new2.py", chunk_path])
            if result.returncode == 0:
                break  # Exit loop if success
            attempt += 1
            print(f"Retrying ({attempt}/{max_attempts}) for {chunk_path}...")
            time.sleep(2)  # Small delay before retry
        
        # Define the output directory for this chunk
        chunk_output_dir = os.path.join(output_base_dir, f"chunk_{i}")
        os.makedirs(chunk_output_dir, exist_ok=True)

        # Move the generated Manim video to the chunk directory
        if os.path.exists(manim_video_path):
            shutil.move(manim_video_path, os.path.join(chunk_output_dir, "GeneratedScene.mp4"))
        else:
            print(f"Warning: Manim video not found for {chunk_path}")

else:
    print(f"Error: Directory '{chunks_dir}' not found. Ensure new.py ran successfully.")
