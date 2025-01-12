This project shows the integration of sensor data into a TAK common operating picture. It simulates a GPS-enabled sensor, generates cot messages, and sends them to a TAK server.


Files:
- `sensor_simulator.py`: Simulates sensor data.
- `cot_generator.py`: Converts sensor data into CoT XML messages.
- `send_to_tak.py`: Sends CoT messages to a TAK server.
- `requirements.txt`: Python dependencies.

Setup:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt