from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Sample data structure to store weather data
weather_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json
    timestamp, temperature, pressure, humidity, wind_direction, wind_speed, rainfall = data.split(',')
    weather_entry = {
        'timestamp': datetime.datetime.fromtimestamp(int(timestamp)),
        'temperature': float(temperature),
        'pressure': float(pressure),
        'humidity': float(humidity),
        'wind_direction': wind_direction,
        'wind_speed': float(wind_speed),
        'rainfall': float(rainfall)
    }
    weather_data.append(weather_entry)
    return jsonify({'status': 'success'})

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
