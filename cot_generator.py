import xml.etree.ElementTree as ET
from datetime import datetime

def generate_cot(sensor_data):
    """Converts sensor data into a CoT XML message."""
    root = ET.Element("event", {
        "version": "2.0",
        "uid": "sensor-1234",
        "type": "a-f-G-U-C",
        "how": "m-g",
        "time": datetime.utcnow().isoformat() + "Z",
        "start": datetime.utcnow().isoformat() + "Z",
        "stale": (datetime.utcnow().replace(microsecond=0).isoformat() + "Z"),
    })

    point = ET.SubElement(root, "point", {
        "lat": str(sensor_data["latitude"]),
        "lon": str(sensor_data["longitude"]),
        "hae": "0",  # Height above ellipsoid
        "ce": "9999999",  # Circular error probable
        "le": "9999999",  # Linear error probable
    })

    detail = ET.SubElement(root, "detail")
    status = ET.SubElement(detail, "status")
    status.text = sensor_data["status"]

    speed = ET.SubElement(detail, "speed")
    speed.text = str(sensor_data["speed"])

    return ET.tostring(root, encoding="utf-8", method="xml").decode()

if __name__ == "__main__":
    # Example test
    mock_data = {
        "latitude": 34.12345,
        "longitude": -118.54321,
        "speed": 45.6,
        "status": "OK"
    }
    cot_message = generate_cot(mock_data)
    print(cot_message)
