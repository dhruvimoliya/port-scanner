"""
Simple Port Scanner
Author: Mirage43
"""

import socket

def scan_port(target, port):
    """Check if a port is open on the target."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except:
        return False

if __name__ == "__main__":
    target = "127.0.0.1"
    port = 80
    if scan_port(target, port):
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")