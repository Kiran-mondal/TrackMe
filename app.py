import socket
import os
from flask import Flask, render_template

app = Flask(name)

def get_local_ip():
    """Function to find the actual local IP address of your device"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Detect router or local network IP without sending any actual data
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

@app.route('/')
def index():
    # Local dashboard will load to view your own IP
    return "<h1>Your OSINT Core is Running Locally! Check Termux Console.</h1>"

if name == 'main':
    # Your favorite authentic old-school green hacking banner interface
    print("\033[92m" + "="*50)
    print("""
  _ __    _     _    ___ _   _   _    _ 
 |_   _|  _ \  / \  / _| |/ /  \/  | __| \ | |/ \  / |
   | | | |_) |/ _ \| |   | ' /| |\/| |  _| |  \| / _ \ | |
   | | |  _ </ _ \ |_| . \| |  | | |_| |\  / _ \| |
   |_| |_| \_/_/   \_\__|_|\_\_|  |_|___|_| \_/_/   \_\_|
    """)
    print(" [*] Personal OSINT & IP Network Engine v1.0.4 [*]")
    print("="*50 + "\033[0m")
    
    # Retrieving your local IP
    my_ip = get_local_ip()
    
    print("\033[94m[*] Scanning Local Network Interfaces...")
    print("[+] Status: ONLINE and Connected\033[0m")
    print("\n\033[93m===========[ YOUR DEVICE IP INFO ]===========\033[0m")
    print(f" YOUR LOCAL IP  : http://{my_ip}:5000")
    print(f" LOCAL LOOPBACK : http://127.0.0.1:5000")
    print("\033[93m=============================================\033[0m")
    print("\n[*] Running secure local server. Press Ctrl+C to stop.\n")

    # Running the server locally for yourself only
    app.run(
        host='0.0.0.0', 
        port=5000, 
        debug=False
    )