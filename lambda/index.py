import json
import random
from datetime import datetime

events = [
    {"severity": "LOW", "event_type": "NORMAL_LOGIN"},
    {"severity": "MEDIUM", "event_type": "PASSWORD_RESET"},
    {"severity": "HIGH", "event_type": "FAILED_LOGIN"},
    {"severity": "HIGH", "event_type": "UNAUTHORIZED_API_CALL"},
    {"severity": "CRITICAL", "event_type": "MULTIPLE_LOGIN_FAILURES"}
]

def handler(event, context):

    selected = random.choice(events)

    log = {
        "timestamp": str(datetime.utcnow()),
        "severity": selected["severity"],
        "event_type": selected["event_type"],
        "source_ip": f"192.168.1.{random.randint(1,255)}",
        "message": "Simulated cloud security event"
    }

    print(json.dumps(log))

    return {
        "statusCode": 200,
        "body": json.dumps("Security event generated")
    }