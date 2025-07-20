# observer-agent.py
import time
from utils.signal_utils import broadcast_heartbeat

def observer_loop():
    while True:
        broadcast_heartbeat("Observer Agent active.")
        time.sleep(10)

if __name__ == "__main__":
    observer_loop()
