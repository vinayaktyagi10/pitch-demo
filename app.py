from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>🚀 Testing automatic deployment</h1><p>The demo is working perfectly!</p>"

if __name__ == "__main__":
    # Critical: Listen on 0.0.0.0 and Port 8000
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
