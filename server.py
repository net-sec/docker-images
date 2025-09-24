from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

@app.route('/list')
def bilderliste():
    files = os.listdir('images')
    bilder = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return jsonify(bilder)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)