import subprocess
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python run.py <YouTube_URL>")
    sys.exit(1)

video_url = sys.argv[1]

def run_command(command, description):
    """ Run a subprocess and log any errors """
    try:
        print(f"\n[INFO] {description}...")
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {description} failed: {e.stderr}")
        sys.exit(1)

# Step 1: Clean previous data
run_command(["python3", "clean.py"], "Cleaning previous files")

# Step 2: Download YouTube video
run_command(["python3", "yt_video_downloader.py", video_url], "Downloading YouTube video")

# Step 3: Chunk the video
run_command(["python3", "chunks.py"], "Chunking the video")

# Step 4: Run final processing script
run_command(["python3", "run_script.py"], "Running final processing")

print("\n✅ All scripts executed successfully.")
