from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import subprocess
import json

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file.save(os.path.join('uploads', file.filename))
        return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/analyze', methods=['POST'])
def analyze_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file.save(os.path.join('uploads', file.filename))
        result = subprocess.run(['python', 'analyze.py', os.path.join('uploads', file.filename)], capture_output=True, text=True)
        return jsonify({'result': result.stdout}), 200

if __name__ == '__main__':
    app.run(debug=True)