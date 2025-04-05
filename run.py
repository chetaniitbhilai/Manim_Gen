import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python run_all.py <YouTube_URL>")
    sys.exit(1)

video_url = sys.argv[1]  # Get YouTube link from command line

# Step 1: Run the YouTube downloader script with the URL
print("Downloading YouTube video...")
subprocess.run(["python", "yt_video_downloader.py", video_url], check=True)
print("Download complete.\n")

# Step 2: Run the video chunking script
print("Chunking the video...")
subprocess.run(["python", "chunks.py"], check=True)
print("Chunking complete.\n")

# Step 3: Run the final script
print("Running final script...")
subprocess.run(["python", "run_script.py"], check=True)
print("All scripts executed successfully.")
