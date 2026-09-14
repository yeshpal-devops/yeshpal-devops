from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify({
        "service": "devops-health-api",
        "status": "running",
        "message": "Containerized DevOps demo service"
    })

@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
