from flask import Flask
import grp  # Linux-specific module (will fail on Windows)

app = Flask(__name__)

@app.route('/')
def hello():
    # This will ONLY work in Docker/Linux thanks to 'grp' import
    return "🐳 This ONLY runs in Docker (Linux containers)!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)