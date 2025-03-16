# Weather Station Web Application

This is a Python-based web application that takes in data from a local weather station and displays it in a user-friendly UI. The application uses Flask for the backend and HTML/CSS with a bit of JavaScript for the frontend.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/weather-station-app.git
   cd weather-station-app
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000`.

## Data Format

The weather data should be sent in the following format:
```
timestamp,temperature,pressure,humidity,wind_direction,wind_speed,rainfall
```
Example:
```
1742159448,46.25,1006.6,20.19,NW,0.0,0.0
```
