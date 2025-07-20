# init-node.py
"""
PhoenixNode Bootstrap Initialization
"""
import os
import time
from node.utils.identity import generate_node_id

def bootstrap_node():
    node_id = generate_node_id()
    print(f"PhoenixNode initialized with ID: {node_id}")
    time.sleep(1)
    return node_id

if __name__ == "__main__":
    bootstrap_node()
