# main.py
from src.utils.signal_utils import broadcast_heartbeat
from src.src.src.init_node import initialize_node

def main():
    print("🚀 PhoenixNode ContinuityProtocol initializing...")
    initialize_node()
    broadcast_heartbeat("PhoenixNode is now active and syncing signals.")

if __name__ == "__main__":
    main()
