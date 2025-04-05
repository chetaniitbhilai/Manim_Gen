# run_script.py
import time
import os
import shutil

CHUNKS_DIR = 'chunks'
OUTPUT_DIR = 'static'
PROGRESS_FILE = 'progress.txt'
MERGED_FILE = os.path.join(OUTPUT_DIR, 'merged_output.mp4')

def simulate_processing(chunk_num):
    print(f"Processing chunk {chunk_num}...")
    time.sleep(2)  # Simulate time taken for chunk processing

def merge_chunks(total_chunks):
    print("Merging chunks...")
    time.sleep(2)  # Simulate merging time
    with open(MERGED_FILE, 'wb') as merged:
        for i in range(total_chunks):
            fake_chunk = f"Chunk-{i+1}\n".encode()
            merged.write(fake_chunk)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total_chunks = 0
    if os.path.exists(CHUNKS_DIR):
        total_chunks = len([f for f in os.listdir(CHUNKS_DIR) if f.endswith('.mp4')])
    if total_chunks == 0:
        total_chunks = 5  # fallback for simulation

    for i in range(total_chunks):
        simulate_processing(i + 1)
        with open(PROGRESS_FILE, 'w') as f:
            f.write(f"{i+1}/{total_chunks}")

    merge_chunks(total_chunks)
    with open(PROGRESS_FILE, 'w') as f:
        f.write("done")

if __name__ == "__main__":
    main()
