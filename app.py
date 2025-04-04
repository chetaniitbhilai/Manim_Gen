from flask import Flask, render_template, request, jsonify, session, send_from_directory, redirect, url_for
import uuid
import os
from threading import Thread
import subprocess
import sys

app = Flask(__name__)
app.secret_key = '12345'

UPLOAD_FOLDER = 'media/uploads'
PROCESSED_FOLDER = 'media/videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def process_video(video_url, upload_id):
    try:
        output_path = os.path.abspath(os.path.join(PROCESSED_FOLDER, f'{upload_id}.mp4'))
        
        process = subprocess.Popen(
            [sys.executable, 'script-code.py', video_url],
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
            generated_path = os.path.abspath(os.path.join('media', 'videos', 'GeneratedScene.mp4'))
            if os.path.exists(generated_path):
                os.rename(generated_path, output_path)
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
    return {'status': 'processing'}

@app.route('/result')
def result():
    upload_id = session.get('upload_id')
    if not upload_id:
        return redirect(url_for('index'))
    return render_template('result.html', video_id=upload_id)

@app.route('/download/<video_id>')
def download(video_id):
    return send_from_directory(PROCESSED_FOLDER, f'{video_id}.mp4', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False, use_reloader=False)
