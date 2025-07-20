# signal_utils.py
import datetime

def broadcast_heartbeat(message):
    timestamp = datetime.datetime.utcnow().isoformat()
    print(f"[{timestamp}] {message}")
