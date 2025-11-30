from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! 👋 (served from a Docker container)"

if __name__ == "__main__":
    # Listen on all interfaces, port 8080 (matches docker -p mapping)
    app.run(host="0.0.0.0", port=8080)
    

