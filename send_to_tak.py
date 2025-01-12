import requests
from sensor_simulator import generate_sensor_data
from cot_generator import generate_cot
import time

# TAK server URL
TAK_SERVER_URL = "http://localhost:8080/endpoint"

"""Sends a cot to the TAK server"""
def send_to_tak(cot_message):
    
    headers = {"Content-Type": "application/xml"}
    try:
        response = requests.post(TAK_SERVER_URL, data=cot_message, headers=headers)
        if response.status_code == 200:
            print("CoT message sent successfully!")
        else:
            print(f"Failed to send CoT message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending CoT message: {e}")

if __name__ == "__main__":
    while True:
        sensor_data = generate_sensor_data()
        cot_message = generate_cot(sensor_data)
        print(f"Generated CoT Message: {cot_message}")
        send_to_tak(cot_message)
        time.sleep(2)  
