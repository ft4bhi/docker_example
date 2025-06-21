from flask import Flask
import grp  

app = Flask(__name__)

@app.route('/')
def hello():
   
    return "🐳 This ONLY runs in Docker (Linux containers)!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
