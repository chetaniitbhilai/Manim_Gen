from flask import Flask, render_template, request, jsonify, session, send_from_directory, redirect, url_for
import uuid
import os
from threading import Thread
import subprocess
import sys
import json
import glob

app = Flask(__name__)
app.secret_key = '12345'

UPLOAD_FOLDER = 'media/uploads'
PROCESSED_FOLDER = 'media/videos'
CHUNKS_DIR = 'chunks'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def count_total_chunks():
    if os.path.exists(CHUNKS_DIR):
        return len(glob.glob(os.path.join(CHUNKS_DIR, '*')))
    return 0

def get_current_chunk_progress():
    try:
        # Look for progress files that might be created during processing
        progress_files = glob.glob('progress_*.txt')
        if progress_files:
            # Sort to get the latest one
            latest_file = sorted(progress_files)[-1]
            with open(latest_file, 'r') as f:
                data = f.read().strip()
                if data.isdigit():
                    return int(data)
        return 0
    except Exception as e:
        print(f"Error reading progress: {str(e)}")
        return 0

def process_video(video_url, upload_id):
    try:
        output_path = os.path.abspath(os.path.join(PROCESSED_FOLDER, f'{upload_id}.mp4'))
        
        # Create a progress status file for this process
        status_file = f"progress_{upload_id}.txt"
        with open(status_file, 'w') as f:
            f.write("0")
        
        process = subprocess.Popen(
            [sys.executable, 'run.py', video_url, upload_id],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=os.getcwd()
        )
        
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(f"[PROCESSING LOG] {output.strip()}")
        
        if process.returncode == 0:
            generated_path = os.path.abspath(os.path.join('media', 'videos', 'merged_output.mp4'))
            if os.path.exists(generated_path):
                os.rename(generated_path, output_path)
                
                # Save manim code to a file that can be accessed later
                manim_code_path = os.path.abspath(os.path.join('media', 'videos', f'{upload_id}_manim_code.txt'))
                if os.path.exists('generated_scene.py'):
                    with open('generated_scene.py', 'r') as src, open(manim_code_path, 'w') as dst:
                        dst.write(src.read())
                
                return True
        return False
    except Exception as e:
        print(f"Error processing video: {str(e)}")
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    video_url = data.get('video_url')

    if not video_url:
        return jsonify({'error': 'No video URL provided'}), 400
    
    print(f"Received video URL: {video_url}")

    upload_id = str(uuid.uuid4())
    session['upload_id'] = upload_id
    session['processing'] = True
    
    thread = Thread(target=process_video, args=(video_url, upload_id))
    thread.start()
    
    return jsonify({'message': 'Processing started', 'upload_id': upload_id})

@app.route('/check_status', methods=['GET'])
def check_status():
    upload_id = session.get('upload_id')
    if upload_id:
        output_path = os.path.join(PROCESSED_FOLDER, f'{upload_id}.mp4')
        
        if os.path.exists(output_path):
            session['processing'] = False
            return {'status': 'complete'}
        
        # Get the progress data
        total_chunks = count_total_chunks()
        current_progress = 0
        chunks_processed = 0
        
        # Check if we have chunks to process
        if total_chunks > 0:
            # Look for the progress file specific to this upload
            progress_file = f"progress_{upload_id}.txt"
            if os.path.exists(progress_file):
                try:
                    with open(progress_file, 'r') as f:
                        progress_data = f.read().strip()
                        data = json.loads(progress_data)
                        chunks_processed = data.get('chunks_processed', 0)
                        current_chunk_progress = data.get('current_chunk_progress', 0)
                        
                        # Calculate overall progress
                        if total_chunks > 0:
                            overall_progress = int((chunks_processed * 100 + current_chunk_progress) / total_chunks)
                            return {
                                'status': 'processing',
                                'progress': overall_progress,
                                'chunks_processed': chunks_processed,
                                'total_chunks': total_chunks,
                                'current_chunk_progress': current_chunk_progress
                            }
                except Exception as e:
                    print(f"Error reading progress file: {str(e)}")
        
        # Default response if we couldn't get detailed progress
        return {
            'status': 'processing',
            'progress': 10,  # Default progress indicator
            'chunks_processed': 0,
            'total_chunks': total_chunks or 1,
            'current_chunk_progress': 0
        }
    
    return {'status': 'processing', 'progress': 0}

@app.route('/processing')
def processing_page():
    return render_template('processing.html')

@app.route('/result')
def result():
    upload_id = session.get('upload_id')
    if not upload_id:
        return redirect(url_for('index'))
    
    # Get manim code if available
    manim_code = ""
    manim_code_path = os.path.join('media', 'videos', f'{upload_id}_manim_code.txt')
    if os.path.exists(manim_code_path):
        with open(manim_code_path, 'r') as f:
            manim_code = f.read()
    
    return render_template('result.html', video_id=upload_id , manim_code  = manim_code)

@app.route('/download/<video_id>')
def download(video_id):
    return send_from_directory(PROCESSED_FOLDER, f'{video_id}.mp4', as_attachment=True)

@app.route('/get_manim_code/<video_id>')
def get_manim_code(video_id):
    manim_code_path = os.path.join('media', 'videos', f'{video_id}_manim_code.txt')
    if os.path.exists(manim_code_path):
        with open(manim_code_path, 'r') as f:
            manim_code = f.read()
        return jsonify({'manim_code': manim_code})
    return jsonify({'manim_code': 'No code available'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False, use_reloader=False)