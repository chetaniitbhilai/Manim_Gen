import os
import subprocess

def get_video_files(directory):
    video_files = []
    for chunk in sorted(os.listdir(directory), key=lambda x: int(x.split('_')[-1])):
        chunk_path = os.path.join(directory, chunk)
        if os.path.isdir(chunk_path):
            for file in sorted(os.listdir(chunk_path)):
                if file.endswith(".mp4"):  # Adjust this if your videos have a different format
                    video_files.append(os.path.join(chunk_path, file))
    return video_files

def create_input_file(video_files, input_file="input.txt"):
    with open(input_file, "w") as f:
        for video in video_files:
            f.write(f"file '{video}'\n")
    return input_file

def merge_videos(input_file, output_file="output.mp4"):
    command = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", input_file, "-c", "copy", output_file]
    subprocess.run(command, check=True)

def main():
    directory = "manim_generated"
    output_file = "merged_output.mp4"
    
    video_files = get_video_files(directory)
    if not video_files:
        print("No video files found!")
        return
    
    input_file = create_input_file(video_files)
    merge_videos(input_file, output_file)
    
    print(f"Videos merged successfully into {output_file}")

if __name__ == "__main__":
    main()
