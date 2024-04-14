from flask import Flask, jsonify, render_template, request
from module.weather import get_weather_by_coordinates
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/current_weather', methods=['GET'])
def current_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    try:
        lat_float = float(lat)
        lon_float = float(lon)
    except ValueError:
        return jsonify({"error": "Invalid latitude or longitude"}), 400

    weather_data = get_weather_by_coordinates(lat_float, lon_float)
    return jsonify(weather_data)

# Check if the run.py file has executed directly and not imported
if __name__ == '__main__':
    # Run the Flask app with debug=True will allow auto-reload during development
    app.run(debug=True)
    
    
    