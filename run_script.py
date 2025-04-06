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
# manim_video_path = "/home/chetan/tryy/code/media/videos/generated_scene/1080p60/GeneratedScene.mp4"
manim_video_path = "media/videos/generated_scene/1080p60/GeneratedScene.mp4"
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
