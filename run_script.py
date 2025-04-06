import os
import subprocess
import shutil
import time
import json
import sys

# Get upload ID if provided
upload_id = sys.argv[1] if len(sys.argv) > 1 else "default"
progress_file = f"progress_{upload_id}.txt"

# Paths and setup
chunks_dir = "chunks"
output_base_dir = "manim_generated"
manim_video_path = "/home/chetan/tryy/code/media/videos/generated_scene/1080p60/GeneratedScene.mp4"
merged_output_path = "media/videos/merged_output.mp4"
output_videos = []

# Ensure output directories exist
os.makedirs(output_base_dir, exist_ok=True)

# Setup progress data
progress_data = {   
    'chunks_processed': 0,
    'total_chunks': 0,
    'current_chunk_progress': 0
}

# Load previous progress if available
if os.path.exists(progress_file):
    try:
        with open(progress_file, 'r') as f:
            content = f.read().strip()
            if content:
                progress_data = json.loads(content)
    except Exception as e:
        print(f"Error reading progress file: {e}")

# Check for chunks
if not os.path.exists(chunks_dir):
    print(f"Error: Directory '{chunks_dir}' not found. Ensure new.py ran successfully.")
    sys.exit(1)

chunks = sorted(os.listdir(chunks_dir))
total_chunks = len(chunks)
progress_data['total_chunks'] = total_chunks

# Save initial progress
with open(progress_file, 'w') as f:
    json.dump(progress_data, f)

chunks = list(chunks)
size = len(chunks)

# Process chunks
for i, chunk in enumerate(chunks):
    chunk_path = os.path.join(chunks_dir, chunk)

    attempt = 0
    max_attempts = 2
    while attempt < max_attempts:
        try:
            result = subprocess.run(["python3", "new2.py", chunk_path], check=True)
            break
        except subprocess.CalledProcessError as e:
            attempt += 1
            print(f"Retrying ({attempt}/{max_attempts}) for {chunk_path} due to error: {e}")
            time.sleep(2)

    # Move generated video if exists
    chunk_output_dir = os.path.join(output_base_dir, f"chunk_{i}")
    os.makedirs(chunk_output_dir, exist_ok=True)

    if os.path.exists(manim_video_path):
        output_path = os.path.join(chunk_output_dir, "GeneratedScene.mp4")
        shutil.move(manim_video_path, output_path)
        output_videos.append(output_path)
    else:
        print(f"Warning: Manim video not found for {chunk_path}")

    # Update progress after chunk is completed
    progress_data['chunks_processed'] = i + 1
    progress_data['current_chunk_progress'] = 100%size
    with open(progress_file, 'w') as f:
        json.dump(progress_data, f)

# Merge all videos if any were generated
if output_videos:
    print("Merging all videos...")

    with open("video_list.txt", "w") as f:
        for video in output_videos:
            f.write(f"file '{video}'\n")

    subprocess.run([
        "ffmpeg", "-f", "concat", "-safe", "0",
        "-i", "video_list.txt", "-c", "copy", merged_output_path
    ], check=True)

    # os.remove("video_list.txt")
    print(f"Merged video saved to: {merged_output_path}")
    subprocess.run(['python', 'clean_up.py'])
else:
    print("No videos to merge.")


# import os
# import subprocess
# import shutil
# import time
# import json
# import sys

# # Get upload ID if provided
# upload_id = sys.argv[1] if len(sys.argv) > 1 else "default"
# progress_file = f"progress_{upload_id}.txt"

# # Step 1: Define directories
# chunks_dir = "chunks"
# output_base_dir = "manim_generated"
# manim_video_path = "/home/chetan/tryy/code/media/videos/generated_scene/1080p60/GeneratedScene.mp4"
# output_videos = []

# # Ensure the output base directory exists
# os.makedirs(output_base_dir, exist_ok=True)

# # Read initial progress data
# progress_data = {
#     'chunks_processed': 0,
#     'total_chunks': 0,
#     'current_chunk_progress': 0
# }

# if os.path.exists(progress_file):
#     try:
#         with open(progress_file, 'r') as f:
#             content = f.read().strip()
#             if content:
#                 progress_data = json.loads(content)
#     except Exception as e:
#         print(f"Error reading progress file: {str(e)}")

# # Count total chunks
# total_chunks = 0
# if os.path.exists(chunks_dir):
#     chunks = sorted(os.listdir(chunks_dir))
#     total_chunks = len(chunks)
#     progress_data['total_chunks'] = total_chunks

# # Update progress file
# with open(progress_file, 'w') as f:
#     json.dump(progress_data, f)

# # Step 2: Process each chunk with new2.py
# if os.path.exists(chunks_dir):
#     chunks = sorted(os.listdir(chunks_dir))
    
#     for i, chunk in enumerate(chunks):
#         chunk_path = os.path.join(chunks_dir, chunk)
        
#         # Update progress - starting a new chunk
#         progress_data['chunks_processed'] = i
#         progress_data['current_chunk_progress'] = 0
#         with open(progress_file, 'w') as f:
#             json.dump(progress_data, f)
        
#         # Try running new2.py once, and retry if it fails

#         attempt = 0
#         max_attempts = 2

#         while attempt < max_attempts:
#             # Run the process and wait for it to finish
#             process = subprocess.run(
#                 ["python3", "new2.py", chunk_path],
#                 stdout=subprocess.PIPE,
#                 stderr=subprocess.STDOUT,
#                 text=True
#             )

#             # Process output line by line after process finishes
#             if process.stdout:
#                 for line in process.stdout.splitlines():
#                     print(line)

#                     # Simulate progress update
#                     progress_data['current_chunk_progress'] += 5
#                     if progress_data['current_chunk_progress'] > 100:
#                         progress_data['current_chunk_progress'] = 95

#                     with open(progress_file, 'w') as f:
#                         json.dump(progress_data, f)

#                     time.sleep(0.5)  # Simulate time for processing

#             # Check if process was successful
#             if process.returncode == 0:
#                 break
#             else:
#                 attempt += 1
#                 print(f"Retrying ({attempt}/{max_attempts}) for {chunk_path}...")
#                 time.sleep(2)

        
#         # Mark chunk as complete
#         progress_data['current_chunk_progress'] = 100
#         with open(progress_file, 'w') as f:
#             json.dump(progress_data, f)
        
#         # Define the output directory for this chunk
#         chunk_output_dir = os.path.join(output_base_dir, f"chunk_{i}")
#         os.makedirs(chunk_output_dir, exist_ok=True)

#         # Move the generated Manim video to the chunk directory
#         if os.path.exists(manim_video_path):
#             output_path = os.path.join(chunk_output_dir, "GeneratedScene.mp4")
#             shutil.move(manim_video_path, output_path)
#             output_videos.append(output_path)
#         else:
#             print(f"Warning: Manim video not found for {chunk_path}")

#     # Update progress - finished processing chunks
#     progress_data['chunks_processed'] = total_chunks
#     progress_data['current_chunk_progress'] = 100
#     with open(progress_file, 'w') as f:
#         json.dump(progress_data, f)

#     # Merge all generated videos if there are any
#     if output_videos:
#         print("Merging generated videos...")
        
#         # Create a file list for ffmpeg
#         with open('video_list.txt', 'w') as f:
#             for video in output_videos:
#                 f.write(f"file '{video}'\n")
        
#         # Use ffmpeg to concatenate the videos
#         merged_output = "media/videos/merged_output.mp4"
#         subprocess.run([
#             "ffmpeg", "-f", "concat", "-safe", "0", 
#             "-i", "video_list.txt", "-c", "copy", merged_output
#         ], check=True)
        
#         print(f"Videos merged successfully to {merged_output}")
        
#         # Cleanup
#         os.remove('video_list.txt')
#     else:
#         print("No videos to merge")

# else:
#     print(f"Error: Directory '{chunks_dir}' not found. Ensure new.py ran successfully.")


# import os
# import subprocess
# import shutil
# import time

# # Step 1: Define directories
# chunks_dir = "chunks"
# output_base_dir = "manim_generated"
# manim_video_path = "/home/chetan/tryy/code/media/videos/generated_scene/480p15/GeneratedScene.mp4"

# # Ensure the output base directory exists
# os.makedirs(output_base_dir, exist_ok=True)

# # Step 2: Process each chunk with new2.py
# if os.path.exists(chunks_dir):
#     for i, chunk in enumerate(sorted(os.listdir(chunks_dir)), start=0):
#         chunk_path = os.path.join(chunks_dir, chunk)
        
#         # Try running new2.py once, and retry if it fails
#         attempt = 0
#         max_attempts = 2
#         while attempt < max_attempts:
#             result = subprocess.run(["python3", "new2.py", chunk_path])
#             if result.returncode == 0:
#                 break  # Exit loop if success
#             attempt += 1
#             print(f"Retrying ({attempt}/{max_attempts}) for {chunk_path}...")
#             time.sleep(2)  # Small delay before retry
        
#         # Define the output directory for this chunk
#         chunk_output_dir = os.path.join(output_base_dir, f"chunk_{i}")
#         os.makedirs(chunk_output_dir, exist_ok=True)

#         # Move the generated Manim video to the chunk directory
#         if os.path.exists(manim_video_path):
#             shutil.move(manim_video_path, os.path.join(chunk_output_dir, "GeneratedScene.mp4"))
#         else:
#             print(f"Warning: Manim video not found for {chunk_path}")

# else:
#     print(f"Error: Directory '{chunks_dir}' not found. Ensure new.py ran successfully.")