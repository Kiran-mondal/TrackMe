import socket
import os
from flask import Flask, render_template

app = Flask(__name__)

def get_local_ip():
    """Function to find the actual local IP address of the device"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

@app.route('/')
def index():
    return "<h1>OSINT Core is Running Locally!</h1>"

if __name__ == '__main__':
    # Clear the terminal screen before displaying the banner
    os.system('clear')
    
    # Corrected Banner for TRACK ME NOW with spacing
    print("\033[92m" + "="*65)
    print("""
  _____ ___    _    ____ _  __  __ _____    __  __  ___  __    __
 |_   _| _ \  / \  / ___| |/ / |  \/  | ____|  |  \/  |/ _ \ \  / /
   | | | |_) |/ _ \| |   | ' /  | |\/| |  _|    | |\/| | | | \ \/ / 
   | | |  _ < / ___ \ |___| . \  | |  | | |___   | |  | | |_| | /  \ 
   |_| |_| \_\_/   \_\____|_|\_\ |_|  |_|_____|  |_|  |_|\___//_/\_\
    """)
    print(" [*] TRACK ME NOW - Personal OSINT Network Engine v1.0.5 [*]")
    print("="*65 + "\033[0m")
    
    my_ip = get_local_ip()
    
    print("\033[94m[*] Scanning Local Network Interfaces...")
    print("[+] Status: ONLINE and Connected\033[0m")
    print("\n\033[93m===========[ YOUR DEVICE IP INFO ]===========\033[0m")
    print(f" YOUR LOCAL IP  : http://{my_ip}:5000")
    print(f" LOCAL LOOPBACK : http://127.0.0.1:5000")
    print("\033[93m=============================================\033[0m")
    print("\n[*] Running secure local server. Press Ctrl+C to stop.\n")

    app.run(
        host='0.0.0.0', 
        port=5000, 
        debug=False
    )
    
