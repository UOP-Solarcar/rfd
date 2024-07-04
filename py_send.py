import can
import serial
import json
import sys
import time

# File I/O
port_name = ""

if len(sys.argv) == 2:
    port_name = sys.argv[1]
else:
    print("ERROR: INCORRECT INPUT. python3 pySend.py [port]")
    exit()

# CAN bus setup
can_interface = 'can0'  # replace with your CAN interface
bus = can.interface.Bus(can_interface, bustype='socketcan')

try:
    with serial.Serial(port_name, baudrate=57600, timeout=10) as ser:
        ser.flush()
        print(f"Using port: {ser.name}")  # check which port was really used

        while True:
            msg = bus.recv()  # receive a CAN message

            # Create a JSON payload from the CAN message
            can_data = {
                "timestamp": msg.timestamp,
                "id": msg.arbitration_id,
                "data": msg.data.hex()
            }

            # Convert the dictionary to a JSON string
            packet = json.dumps(can_data) + "\n"
            
            # Send the JSON packet over the serial port
            s = ser.write(packet.encode())
            print(f"Packet sent: {packet}")
            print(f"Size of packet sent: {s} bytes")
            
            time.sleep(0.1)  # Adjust the sleep time as necessary
except serial.SerialException as e:
    print(f"Serial exception: {e}")
except can.CanError as e:
    print(f"CAN bus error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
