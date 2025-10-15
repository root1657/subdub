from flask import Flask, send_from_directory
from src.api.endpoints import api_bp
from src.api.storage_controller import storage_bp
import os
from pathlib import Path

app = Flask(__name__)

# Register blueprints
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(storage_bp, url_prefix='/api')

@app.route('/api/health')
def health():
    return {
        'status': 'healthy',
        'version': '1.0.0',
        'volumes': {
            'input': os.path.exists('/app/input-videos'),
            'output': os.path.exists('/app/output-subtitles')
        }
    }

@app.route('/')
def web_ui():
    return send_from_directory('../web-ui/build', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../web-ui/build', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)