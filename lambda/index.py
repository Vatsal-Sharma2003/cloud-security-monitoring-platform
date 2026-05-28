from flask import Flask, jsonify
from datetime import datetime, UTC
import random

app = Flask(__name__)

@app.route("/")
def home():

    event = {
        "timestamp": str(datetime.now(UTC)),
        "event_type": "UNAUTHORIZED_API_CALL",
        "severity": "HIGH",
        "source_ip": f"192.168.1.{random.randint(1,255)}",
        "username": f"user{random.randint(100,999)}",
        "region": "ap-south-1",
        "message": "Simulated cloud security threat detected"
    }

    return jsonify(event)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)