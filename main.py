import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello f rom Fly.io!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use port from Fly.io
    app.run(host="0.0.0.0", port=port)        # Listen on public address
