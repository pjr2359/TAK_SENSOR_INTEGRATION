import time
import random

"""Simulates GPS-enabled sensor data."""
def generate_sensor_data():
    latitude = random.uniform(34.0, 35.0)  #
    longitude = random.uniform(-118.0, -117.0)  
    speed = random.uniform(0, 100)  #km/h
    status = random.choice(["OK", "WARNING", "ERROR"])  
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
        time.sleep(2)  
