from flask import Flask, render_template, request, jsonify

app = Flask(name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.get_json()
    print(f"Received location - Latitude: {data['lat']}, Longitude: {data['lon']}")
    # You can save this data to a file or process it via location_tool.py here
    return jsonify({"status": "success"})

if name == 'main':
    app.run(host='0.0.0.0', port=5000, debug=True)