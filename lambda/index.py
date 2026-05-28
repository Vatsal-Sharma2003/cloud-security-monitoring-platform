import json
import random
from datetime import datetime

def handler(event, context):

    attack_types = [
        "FAILED_LOGIN",
        "BRUTE_FORCE_ATTACK",
        "PRIVILEGE_ESCALATION",
        "SUSPICIOUS_IP",
        "MALWARE_ACTIVITY",
        "UNAUTHORIZED_API_CALL",
        "DATA_EXFILTRATION"
    ]

    severity_levels = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

    event_data = {
        "timestamp": str(datetime.utcnow()),
        "event_type": random.choice(attack_types),
        "severity": random.choice(severity_levels),
        "source_ip": f"192.168.1.{random.randint(1,255)}",
        "username": f"user{random.randint(100,999)}",
        "region": "ap-south-1",
        "message": "Simulated cloud security threat detected"
    }

    print(json.dumps(event_data))

    return {
        "statusCode": 200,
        "body": json.dumps("Advanced security event generated")
    }
if __name__ == "__main__":
    handler({}, {})