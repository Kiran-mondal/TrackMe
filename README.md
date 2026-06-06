# TrackMe 🌐

## 🎯 Secure OSINT Location Tracking Engine v1.0.4

A real-time location tracking application using HTML5 Geolocation API and Flask backend. Track and view your GPS position on an interactive map with live updates. Features self-signed SSL/TLS encryption, reverse geocoding, and real-time telemetry logging.

---

## ⚡ Quick Start (One Command)

```bash
git clone https://github.com/Kiran-mondal/TrackMe.git && cd TrackMe && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && chmod +x generate_cert.sh && ./generate_cert.sh && python app.py
```

**Windows PowerShell**:
```bash
git clone https://github.com/Kiran-mondal/TrackMe.git; cd TrackMe; python3 -m venv venv; venv\Scripts\Activate.ps1; pip install -r requirements.txt; .\generate_cert.sh; python app.py
```

---

## ✨ Features

- 🗺️ **Real-time GPS Tracking** - Browser-based geolocation tracking
- 📍 **Live Map Updates** - Interactive map with location visualization
- 🚀 **Simple Flask Backend** - Lightweight and easy-to-deploy server
- 📱 **Mobile-Friendly** - Responsive design for all devices
- ⚡ **Real-time Updates** - Instant position synchronization with payload logging
- 🔐 **Secure HTTPS/SSL** - Self-signed certificates with TLS encryption
- 🌍 **Reverse Geocoding** - Converts GPS coordinates to actual street addresses
- 🎨 **Ethical Hacking Theme** - Professional ANSI colored output and targeting logs
- 📲 **Termux Compatible** - Auto-detects Termux environment for mobile deployment

---

## 📋 System Prerequisites

- **Python** 3.7+
- **pip** (Python package manager)
- **Git** (for cloning repository)
- **OpenSSL** (usually pre-installed on Linux/Mac)
- **Bash** (for running certificate generation script)
- Modern web browser with Geolocation API support

### Verify Prerequisites:
```bash
python3 --version && pip --version && git --version && openssl version
```

---

## 🚀 Installation Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/Kiran-mondal/TrackMe.git
cd TrackMe
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate    # Linux/Mac
# venv\Scripts\activate     # Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Generate SSL Certificates
```bash
chmod +x generate_cert.sh
./generate_cert.sh
```

### Step 5: Launch the Application
```bash
python app.py
```

---

## 📸 Screenshots

### Console Output - Live Location Tracking
![TrackMe Console Output](https://github.com/Kiran-mondal/TrackMe/raw/main/screenshots/console-output.png)

*Real-time console showing IP information, targeting links, and location capture telemetry*

### Web Interface - Location Map
*[Add your web interface screenshot here]*

### Live Location Data
*[Add your location tracking screenshot here]*

### Mobile (Termux) Deployment
*[Add your mobile deployment screenshot here]*

---

## 💻 Usage

### Access the Application:
After launching `python app.py`, open your browser:

- **Local Access**: `https://127.0.0.1:5000`
- **LAN Access**: `https://<YOUR_LOCAL_IP>:5000`

### How to Use:
1. Allow location permission when browser asks
2. Your GPS location appears on the interactive map
3. Tracker updates in real-time as you move
4. Check terminal for live telemetry logs

---

## 📁 Project Structure

```
TrackMe/
├── app.py                 # Main Flask application with SSL/TLS
├── generate_cert.sh       # Certificate generation script
├── location_tool.py       # Location utility functions
├── requirements.txt       # Python dependencies
├── templates/index.html   # Frontend HTML with geolocation
├── static/                # CSS, JavaScript, Images
├── screenshots/           # Screenshot directory
├── README.md             # This file
├── LICENSE               # GPL-3.0 License
└── .gitignore           # Git ignore rules
```

---

## 🏗️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend** | Flask 3.0.2 (Python) | Web server & API endpoints |
| **Frontend** | HTML5, CSS3, JavaScript | User interface |
| **Geolocation** | HTML5 Geolocation API | GPS coordinate retrieval |
| **Mapping** | Leaflet.js | Interactive map visualization |
| **Real-time** | WebSockets / AJAX | Live location updates |
| **Geocoding** | geopy (Nominatim) | Reverse geocoding |
| **Security** | OpenSSL/SSL-TLS | HTTPS encryption |

---

## ⚙️ Configuration

### Default Settings (in `app.py`):
```python
host='0.0.0.0'           # Listen on all interfaces
port=5000                # Port number
debug=True               # Development mode
ssl_context=(cert_path, key_path)  # Self-signed certificates
```

### Change Port:
Edit `app.py` and modify the port number from 5000 to your desired port.

---

## 🌍 API Endpoints

### Main Route
**GET** `/`
- Returns the main tracking interface (index.html)

### Location Update Endpoint
**POST** `/update_location`
- Receives GPS coordinates from frontend
- Performs reverse geocoding
- Logs telemetry with ANSI colors
- **Request Body**: `{"lat": 40.7128, "lon": -74.0060}`

---

## 🔐 SSL/TLS & Security

### Certificate Details:
- **Type**: Self-signed X.509 certificate
- **Key Size**: RSA 4096-bit encryption
- **Validity**: 365 days from generation
- **Files**: `cert.pem` (certificate) + `key.pem` (private key)

### Security Features:
✅ HTTPS/TLS encryption for data in transit  
✅ Self-signed certificates for development  
✅ Privacy-focused location tracking  
✅ No external service dependencies for HTTPS  

---

## 🐛 Troubleshooting

### Certificate Generation Failed
```bash
openssl req -x509 -newkey rsa:4096 -nodes \
    -out cert.pem -keyout key.pem -days 365 \
    -subj "/CN=localhost"
```

### Port Already in Use
```bash
lsof -i :5000           # macOS/Linux
netstat -ano | grep 5000  # Windows
# Edit app.py to use a different port
```

### Location Not Updating
- ✅ Check browser console (F12) for errors
- ✅ Verify browser geolocation permission
- ✅ Ensure HTTPS is being used (not HTTP)
- ✅ Enable location services on device
- ✅ Try in incognito/private mode

---

## 📱 Mobile Deployment (Termux)

```bash
pkg install python git openssl
git clone https://github.com/Kiran-mondal/TrackMe.git
cd TrackMe
pip install -r requirements.txt
chmod +x generate_cert.sh
./generate_cert.sh
python app.py
```

Access from another device: `https://<ANDROID_DEVICE_IP>:5000`

---

## 🛡️ Privacy & Ethics

⚠️ **IMPORTANT**: This project is for **educational and authorized testing only**.

- Only track locations with **explicit user consent**
- Use for **authorized security testing** only
- Comply with local laws and regulations
- Respect user privacy and data protection

---

## 📝 License

This project is licensed under the **GNU General Public License v3.0** (GPL-3.0)

See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 👨‍💻 Author

**Kiran Mondal**  
📱 GitHub: [@Kiran-mondal](https://github.com/Kiran-mondal)  
🌐 Repository: [TrackMe](https://github.com/Kiran-mondal/TrackMe)

---

## 📧 Support & Issues

For issues, questions, bugs, or suggestions:
- 🐛 Open an [Issue](https://github.com/Kiran-mondal/TrackMe/issues)
- 💬 Check existing issues for solutions
- 📮 Contact via GitHub

---

## 🙏 Acknowledgments

- **Flask** - Micro web framework for Python
- **geopy** - Reverse geocoding library (Nominatim)
- **Leaflet.js** - Interactive mapping library
- **HTML5 Geolocation API** - Browser location access
- **OpenSSL** - SSL/TLS certificate generation
- Community feedback and contributions

---

**Last Updated**: June 2026  
**Version**: 1.0.4  
**Status**: ✅ Active & Maintained  
**License**: GPL-3.0  

🚀 **Ready to Deploy!**
