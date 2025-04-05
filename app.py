import subprocess
import os
import time
from flask import Flask, render_template, request, jsonify, send_file
from threading import Thread

app = Flask(__name__)

PROGRESS_FILE = "progress.txt"
PROCESSED_FOLDER = "static"
MERGED_FILE = os.path.join(PROCESSED_FOLDER, "merged_output.mp4")

# Ensure folders exist
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def run_processing(video_url):
    """ Runs the full processing pipeline using run.py """
    try:
        print("[INFO] Starting processing...")
        process = subprocess.Popen(
            ["python3", "run.py", video_url],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        # Print logs in real-time
        for line in process.stdout:
            print(line.strip())

        process.wait()

        if os.path.exists(MERGED_FILE):
            with open(PROGRESS_FILE, "w") as f:
                f.write("done")
        else:
            print("[ERROR] Processing failed! No merged video found.")
    except Exception as e:
        print(f"[ERROR] run_processing crashed: {e}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    video_url = data.get("video_url")

    if not video_url:
        return jsonify({"error": "No URL provided"}), 400

    thread = Thread(target=run_processing, args=(video_url,))
    thread.start()

    return jsonify({"upload_id": "processing_started"})

@app.route("/check_status")
def check_status():
    if not os.path.exists(PROGRESS_FILE):
        return jsonify({"status": "waiting"})

    with open(PROGRESS_FILE, "r") as f:
        data = f.read().strip()

    if data == "done":
        return jsonify({"status": "complete", "progress": 100})

    return jsonify({"status": "processing", "progress": 50})  # Default midpoint

@app.route("/result")
def result():
    return render_template("result.html", video_id="merged_output")

@app.route("/download/<video_id>")
def download(video_id):
    path = os.path.join(PROCESSED_FOLDER, f"{video_id}.mp4")
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True)
