# TrackMeNow 🌐

## 🎯 Secure OSINT Location Tracking Engine v1.0.2

A real-time location tracking application using HTML5 Geolocation API and Flask backend. Track and view your GPS position on an interactive map with live updates. Features self-signed SSL/TLS encryption and reverse geocoding capabilities.

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

Before you begin, ensure you have the following installed:
- **Python** 3.7+
- **pip** (Python package manager)
- **Git** (for cloning repository)
- **OpenSSL** (usually pre-installed on Linux/Mac, included in Windows Python)
- **Bash** (for running certificate generation script)
- Modern web browser with Geolocation API support

### Verify Prerequisites:
```bash
python3 --version    # Check Python
pip --version        # Check pip
git --version        # Check Git
openssl version      # Check OpenSSL
```

---

## 🚀 Quick Installation (One Command)

### Complete Installation & Launch:

```bash
# Clone the repository
git clone https://github.com/Kiran-mondal/TrackMeNow.git

# Navigate to project directory
cd TrackMeNow

# Create virtual environment (optional but recommended)
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

# Make the certificate generation script executable
chmod +x generate_cert.sh

# Generate SSL/TLS self-signed certificates
./generate_cert.sh

# Launch the application with HTTPS
python app.py
```

---

## 📦 Detailed Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/Kiran-mondal/TrackMeNow.git
cd TrackMeNow
```

### Step 2: Create a Virtual Environment (Recommended)

Creating a virtual environment isolates project dependencies and prevents conflicts.

```bash
# Create virtual environment
python3 -m venv venv

# Activate it:
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# On Windows PowerShell:
venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **Flask 3.0.2** - Web framework for backend server
- **Werkzeug 3.0.1** - WSGI utilities and HTTP parsing
- **Jinja2 3.1.3** - Template engine for HTML rendering
- **MarkupSafe 2.1.5** - HTML/XML handling utilities
- **itsdangerous 2.1.2** - Secure payload serialization
- **click 8.1.7** - CLI utilities
- **geopy 2.4.1** - Reverse geocoding (converts coordinates to addresses)

### Step 4: Generate SSL/TLS Certificates

The project requires self-signed certificates for HTTPS/SSL encryption.

#### Make script executable:
```bash
chmod +x generate_cert.sh
```

#### Generate certificates:
```bash
./generate_cert.sh
```

This script:
- Auto-detects Termux environment (for mobile deployment)
- Creates `cert.pem` (SSL certificate) - valid for 365 days
- Creates `key.pem` (private key) - RSA 4096-bit encryption
- Validates successful file creation

#### Verify certificate generation:
```bash
# Check if certificates were created
ls -l cert.pem key.pem

# Output should show:
# -rw-r--r-- 1 user group XXXX cert.pem
# -rw-r--r-- 1 user group XXXX key.pem
```

**Note**: Certificates are self-signed for development/testing. Browsers will show a security warning (normal behavior - bypass with "Advanced" > "Proceed").

### Step 5: Launch the Application

```bash
python app.py
```

The application will:
1. Display the TrackMeNow banner
2. Initialize SSL/TLS encryption
3. Show targeting links
4. Listen for incoming connections

---

## 💻 Usage

### Access the Application:

After launching `python app.py`, open your browser and navigate to:

- **Local Access**: `https://127.0.0.1:5000`
- **LAN Access**: `https://<YOUR_LOCAL_IP>:5000`

### How to Use:

1. Open the URL in your web browser
2. Browser will ask for location permission - **Allow**
3. Your GPS location will appear on the interactive map
4. The tracker updates in real-time as you move
5. Check terminal/console for live telemetry logs:
   ```
   [🎯] TARGET COMPROMISED - NEW LOCATION CAPTURED!
   LATITUDE  : XX.XXXXX
   LONGITUDE : XX.XXXXX
   ADDRESS   : Street, City, Country
   STATUS    : Data successfully intercepted & parsed.
   ```

---

## 📁 Project Structure

```
TrackMeNow/
├── app.py                    # Main Flask application with SSL/TLS
├── generate_cert.sh          # Certificate generation script
├── location_tool.py          # Location utility functions
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html           # Frontend HTML with geolocation
├── static/
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files
│   └── images/              # Images and assets
├── README.md                # This file
├── LICENSE                  # GPL-3.0 License
└── .gitignore              # Git ignore rules
```

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend** | Flask 3.0.2 (Python) | Web server & API endpoints |
| **Frontend** | HTML5, CSS3, JavaScript | User interface |
| **Geolocation** | HTML5 Geolocation API | GPS coordinate retrieval |
| **Mapping** | Leaflet.js / Mapping Library | Interactive map visualization |
| **Real-time** | WebSockets / AJAX | Live location updates |
| **Geocoding** | geopy (Nominatim) | Reverse geocoding (coords → addresses) |
| **Security** | OpenSSL/SSL-TLS | HTTPS encryption, self-signed certs |

---

## ⚙️ Configuration

### Default Configuration (in `app.py`):

```python
# Server Configuration
host='0.0.0.0'           # Listen on all interfaces
port=5000                # Port number
debug=True               # Development mode (auto-reload)

# SSL/TLS Configuration
ssl_context=(cert_path, key_path)  # Use self-signed certificates
```

### To Change Port:
Edit `app.py` line 96:
```python
app.run(
    host='0.0.0.0', 
    port=8080,              # Change from 5000 to desired port
    debug=True, 
    ssl_context=(cert_path, key_path)
)
```

### Environment Variables:
```bash
# Set debug mode
export FLASK_ENV=development

# Run with specific host
export FLASK_HOST=0.0.0.0

# Run with specific port
export FLASK_PORT=5000
```

---

## 🌍 API Endpoints

### Main Route
**GET** `/`
- Returns the main tracking interface (index.html)
- **Response**: HTML interface with geolocation form

### Location Update Endpoint
**POST** `/update_location`
- Receives GPS coordinates from frontend
- Performs reverse geocoding
- Logs telemetry with ANSI colors
- **Request Body**:
  ```json
  {
    "lat": 40.7128,
    "lon": -74.0060
  }
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "message": "Location updated"
  }
  ```
- **Error Response**:
  ```json
  {
    "status": "error",
    "message": "Error description"
  }
  ```

---

## 🔐 SSL/TLS & Security

### Certificate Details:
- **Type**: Self-signed X.509 certificate
- **Key Size**: RSA 4096-bit encryption
- **Validity**: 365 days from generation
- **CN (Common Name)**: localhost
- **Files**: `cert.pem` (certificate) + `key.pem` (private key)

### Security Features:
✅ HTTPS/TLS encryption for data in transit  
✅ Self-signed certificates for development  
✅ Privacy-focused location tracking  
✅ No external service dependencies for HTTPS  

### Browser Security Warning:
When accessing `https://127.0.0.1:5000`:
1. Browser shows "Your connection is not private"
2. This is **normal** for self-signed certificates
3. Click **Advanced** → **Proceed to 127.0.0.1** (or equivalent)
4. Connection is still encrypted, just self-signed

---

## 🐛 Troubleshooting

### Issue: Certificate Files Not Created
```bash
# Error: "Failed to compile credentials"

# Solution:
# 1. Check OpenSSL is installed
openssl version

# 2. Manual certificate generation
openssl req -x509 -newkey rsa:4096 -nodes \
    -out cert.pem -keyout key.pem -days 365 \
    -subj "/CN=localhost"

# 3. Verify files
ls -l cert.pem key.pem
```

### Issue: "Port 5000 Already in Use"
```bash
# Find process using port 5000
lsof -i :5000           # macOS/Linux
netstat -ano | grep 5000  # Windows

# Kill the process or use different port
# Edit app.py, change port to 5001, 8000, etc.
```

### Issue: Location Not Updating
- ✅ Check browser console (F12) for JavaScript errors
- ✅ Verify browser has geolocation permission
- ✅ Check HTTPS is being used (not HTTP)
- ✅ Ensure location services are enabled on device
- ✅ Try in incognito/private mode (clear permissions)

### Issue: "Address Lookup Timeout"
```bash
# geopy reverse geocoding failed (slow network)
# Solution: Check internet connection, try again
# The app will show "Failed to resolve address (Network Timeout)"
```

### Issue: Server Not Starting with Flask
```bash
# Error: "Address already in use"

# Check if port is available
# Kill process or use different port
python app.py  # Will auto-generate certs if missing
```

### Issue: Certificate Errors on Windows
```bash
# Windows may require specific OpenSSL path
# Ensure Python's OpenSSL is used:
pip install --upgrade pyopenssl

# Or generate certificates manually:
python -m OpenSSL.crypto
```

---

## 📱 Mobile Deployment (Termux)

The project auto-detects and works on Termux (Android terminal emulator):

```bash
# In Termux:
pkg install python git openssl
git clone https://github.com/Kiran-mondal/TrackMeNow.git
cd TrackMeNow
pip install -r requirements.txt
chmod +x generate_cert.sh
./generate_cert.sh  # Auto-detects Termux environment
python app.py
```

Then access from another device on same WiFi:
```
https://<ANDROID_DEVICE_LOCAL_IP>:5000
```

---

## 🎨 Understanding the Output

When you run `python app.py`, you'll see:

```
[+] Secure OSINT Location Tracking Engine v1.0.2
[*] Initializing SSL/TLS layer with self-signed certificates...
[+] Framework status: ACTIVE and listening for incoming payloads...

==========[ TARGETING LINKS ]==========
 LOCAL LOOPBACK : https://127.0.0.1:5000
 LAN CAPTURE IP : https://100.73.179.109:5000
=====================================
[*] Awaiting target interaction. Live logs will stream below...

[🎯] TARGET COMPROMISED - NEW LOCATION CAPTURED!
    LATITUDE  : 40.7128
    LONGITUDE : -74.0060
    ADDRESS   : New York City, USA
    STATUS    : Data successfully intercepted & parsed.
```

**Color Legend**:
- 🟢 **GREEN**: Success status, active services
- 🔵 **CYAN**: Information, connection details
- 🟡 **YELLOW**: Coordinates and location data
- 🔴 **RED**: Errors and warnings

---

## 📊 Performance

- **Response Time**: < 500ms for location update
- **Reverse Geocoding**: 2-10s (depends on network)
- **Max Concurrent Users**: Limited by Flask/system resources
- **Memory Usage**: ~50-100MB running
- **CPU Usage**: Minimal (event-driven)

---

## 🛡️ Privacy & Ethics

⚠️ **IMPORTANT**: This project is for **educational and authorized testing only**.

- Only track locations with **explicit user consent**
- Use for **authorized security testing** only
- Comply with local laws and regulations
- Respect user privacy and data protection
- Do not track without permission

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
🌐 Repository: [TrackMeNow](https://github.com/Kiran-mondal/TrackMeNow)

---

## 📧 Support & Issues

For issues, questions, bugs, or suggestions:
- 🐛 Open an [Issue](https://github.com/Kiran-mondal/TrackMeNow/issues)
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

## 📚 Quick Reference

### Installation One-Liner:
```bash
git clone https://github.com/Kiran-mondal/TrackMeNow.git && cd TrackMeNow && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && chmod +x generate_cert.sh && ./generate_cert.sh && python app.py
```

### Common Commands:
```bash
# Start server
python app.py

# Check certificates
ls -l cert.pem key.pem

# Regenerate certificates
./generate_cert.sh

# Install dependencies
pip install -r requirements.txt

# Deactivate virtual environment
deactivate

# Check running processes
ps aux | grep python
```

---

**Last Updated**: June 2026  
**Version**: 1.0.2  
**Status**: ✅ Active & Maintained  
**License**: GPL-3.0  

🚀 **Ready to Deploy!**
