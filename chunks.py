import os
import subprocess

def split_video(video_path, chunk_length=300):  # 300 seconds = 5 minutes
    # Create 'chunks' directory if it doesn't exist
    output_dir = "chunks"
    os.makedirs(output_dir, exist_ok=True)
    
    # Get the video filename without extension
    filename = os.path.splitext(os.path.basename(video_path))[0]
    
    # Construct ffmpeg command
    output_pattern = os.path.join(output_dir, f"chunk_%03d.mp4")
    command = [
        "ffmpeg", "-i", video_path,
        "-c", "copy", "-map", "0", 
        "-segment_time", str(chunk_length),
        "-f", "segment", "-reset_timestamps", "1",
        output_pattern
    ]
    
    # Run command
    subprocess.run(command, check=True)
    print(f"Video split into 5-minute chunks in '{output_dir}' directory.")

# Example usage
video_file = "./videos/videoplayback.mp4"  # Replace with your video file
split_video(video_file)
