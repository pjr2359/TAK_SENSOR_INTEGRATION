import time
import random

def generate_sensor_data():
    """Simulates GPS-enabled sensor data."""
    latitude = random.uniform(34.0, 35.0)  # Mock latitude range
    longitude = random.uniform(-118.0, -117.0)  # Mock longitude range
    speed = random.uniform(0, 100)  # Speed in km/h
    status = random.choice(["OK", "WARNING", "ERROR"])  # Sensor status
    return {
        "latitude": latitude,
        "longitude": longitude,
        "speed": speed,
        "status": status
    }

if __name__ == "__main__":
    while True:
        sensor_data = generate_sensor_data()
        print(f"Generated Sensor Data: {sensor_data}")
        time.sleep(2)  # Generate data every 2 seconds
