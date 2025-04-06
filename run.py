import subprocess
import sys
import json
import os



if len(sys.argv) < 2:
    print("Usage: python run.py <YouTube_URL> [upload_id]")
    sys.exit(1)

video_url = sys.argv[1]  # Get YouTube link from command line
upload_id = sys.argv[2] if len(sys.argv) > 2 else "default"

# Create a progress file for tracking
progress_file = f"progress_{upload_id}.txt"
with open(progress_file, 'w') as f:
    progress_data = {
        'chunks_processed': 0,
        'total_chunks': 0,
        'current_chunk_progress': 0
    }
    json.dump(progress_data, f)

# Step 1: Run the YouTube downloader script with the URL
print("Downloading YouTube video...")
subprocess.run(["python", "yt_video_downloader.py", video_url], check=True)
print("Download complete.\n")

# Step 2: Run the video chunking script
print("Chunking the video...")
subprocess.run(["python", "chunks.py"], check=True)
print("Chunking complete.\n")

# Count total chunks for progress calculation
chunks_dir = "chunks"
total_chunks = 0
if os.path.exists(chunks_dir):
    total_chunks = len(os.listdir(chunks_dir))

# Update progress file with total chunks
with open(progress_file, 'w') as f:
    progress_data = {
        'chunks_processed': 0,
        'total_chunks': total_chunks,
        'current_chunk_progress': 0
    }
    json.dump(progress_data, f)

# Step 3: Run the modified run_script that reports progress
print("Running final script...")
# subprocess.run(["python", "run_script.py", upload_id], check=True)
os.system(f"python run_script.py {upload_id}")
print("All scripts executed successfully.")