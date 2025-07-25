from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask App inside Docker + K8s!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
