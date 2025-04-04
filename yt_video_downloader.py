import sys
import os
import yt_dlp

def download_video(video_url):
    try:
        output_folder = "videos"  # Folder to store videos
        os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist
        
        output_path = os.path.join(output_folder, "videoplayback.mp4")  # Fixed filename
        
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  
            'outtmpl': output_path,  # Save as 'videoplayback.mp4'
            'merge_output_format': 'mp4',  # Ensure the output is in MP4 format
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        
        print(f"Download complete! Video saved as '{output_path}'")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python yt_video_downloader.py <YouTube_URL>")
        sys.exit(1)

    video_url = sys.argv[1]
    download_video(video_url)
