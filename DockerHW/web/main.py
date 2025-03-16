from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker!"

if __name__ == '__main__':
    # Flask runs on host='0.0.0.0' to be accessible inside the container
    app.run(host='0.0.0.0', port=5000)
