# TrackMeNow 🌐

## Live Location Tracker

A real-time location tracking application using HTML5 Geolocation API and Flask backend. Track and view your GPS position on an interactive map with live updates.

---

## ✨ Features

- 🗺️ **Real-time GPS Tracking** - Browser-based geolocation tracking
- 📍 **Live Map Updates** - Interactive map with location visualization
- 🚀 **Simple Flask Backend** - Lightweight and easy-to-deploy server
- 📱 **Mobile-Friendly** - Responsive design for all devices
- ⚡ **Real-time Updates** - Instant position synchronization
- 🔐 **Secure** - Privacy-focused location tracking

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7+
- pip (Python package manager)
- Git
- Modern web browser with Geolocation API support

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kiran-mondal/TrackMeNow.git
cd TrackMeNow
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000` (or the configured port)

---

## 💻 Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Allow the browser to access your location when prompted
3. Your current location will appear on the map
4. The map updates in real-time as you move

---

## 📁 Project Structure

```
TrackMeNow/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   └── images/           # Images and assets
└── README.md             # This file
```

---

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Geolocation**: HTML5 Geolocation API
- **Mapping**: Leaflet.js / Google Maps API
- **Real-time Updates**: WebSockets / AJAX

---

## ⚙️ Configuration

Update configuration in `app.py`:

```python
DEBUG = True              # Development mode
HOST = '0.0.0.0'        # Server host
PORT = 5000             # Server port
```

---

## 🌍 API Endpoints

### GET /
Returns the main tracking interface

### GET /api/location
Returns the current user location

### POST /api/location
Updates location data

---

## 📸 Screenshots

[Add screenshots of your application here]

---

## 🐛 Troubleshooting

### Location not updating
- Check browser permissions for geolocation
- Ensure HTTPS is used (required for secure contexts)
- Verify browser support for Geolocation API

### Server not starting
- Verify Python is installed: `python --version`
- Check if port 5000 is available
- Ensure all dependencies are installed

### Map not loading
- Check browser console for errors (F12)
- Verify internet connection for map tiles
- Check API keys if using external map service

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Kiran Mondal**  
GitHub: [@Kiran-mondal](https://github.com/Kiran-mondal)

---

## 📧 Support

For issues, questions, or suggestions, please open an [Issue](https://github.com/Kiran-mondal/TrackMeNow/issues) on GitHub.

---

## 🙏 Acknowledgments

- Flask documentation
- Leaflet.js mapping library
- HTML5 Geolocation API

---

**Last Updated**: June 2026  
**Version**: 1.0.0
