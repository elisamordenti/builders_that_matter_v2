from flask import Flask, render_template, send_from_directory
from pathlib import Path
import json

app = Flask(__name__)

DATA_DIR = Path(__file__).parent / "data"


def load_json(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)

THESIS = load_json("thesis.json")
STARTUPS = load_json("startups.json")

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html', startups=STARTUPS, thesis=THESIS)

if __name__ == '__main__':
    data_files = [str(p) for p in DATA_DIR.glob("*.json")]
    app.run(debug=True, host='0.0.0.0', port=5000, extra_files=data_files)

